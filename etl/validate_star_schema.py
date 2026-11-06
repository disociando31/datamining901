#!/usr/bin/env python3
"""Valida integridad del modelo estrella y conciliación contra el CSV."""

from __future__ import annotations

import argparse
import csv
import sqlite3
import sys
from collections import Counter
from decimal import Decimal, InvalidOperation
from pathlib import Path

from load_star_schema import (
    DEFAULT_CSV,
    DEFAULT_DB,
    DIMENSIONS,
    DIMENSION_SOURCE_COLUMNS,
    EXPECTED_COLUMNS,
    UNKNOWN_KEY,
    fingerprint,
)


def source_integer(row: dict[str, str], column: str) -> int | None:
    value = row.get(column)
    if value is None or not value.strip():
        return None
    try:
        number = Decimal(value)
    except InvalidOperation as error:
        raise ValueError(f"{column}: valor no numérico {value!r}") from error
    if not number.is_finite() or number != number.to_integral_value():
        raise ValueError(f"{column}: se esperaba un entero, se recibió {value!r}")
    return int(number)


def collect_source(csv_path: Path) -> tuple[int, list[dict[str, str]], int]:
    with csv_path.open("r", encoding="utf-8-sig", newline="") as source:
        reader = csv.DictReader(source)
        columns = reader.fieldnames or []
        if len(columns) != len(set(columns)) or set(columns) != EXPECTED_COLUMNS:
            missing = sorted(EXPECTED_COLUMNS - set(columns))
            unexpected = sorted(set(columns) - EXPECTED_COLUMNS)
            raise ValueError(
                "El esquema del CSV no coincide con el esperado. "
                f"Faltantes: {missing}; inesperadas: {unexpected}"
            )
        rows = list(reader)
    unique_rows: list[dict[str, str]] = []
    seen: set[str] = set()
    for row in rows:
        row_fingerprint = fingerprint(row, columns)
        if row_fingerprint not in seen:
            seen.add(row_fingerprint)
            unique_rows.append(row)
    return len(rows), unique_rows, len(rows) - len(unique_rows)


def validate(csv_path: Path, database_path: Path) -> list[str]:
    if not csv_path.is_file():
        raise FileNotFoundError(f"No existe el CSV: {csv_path}")
    if not database_path.is_file():
        raise FileNotFoundError(f"No existe la base SQLite: {database_path}")
    source_count, source_rows, exact_duplicates = collect_source(csv_path)
    errors: list[str] = []
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    try:
        metadata = connection.execute(
            "SELECT * FROM etl_carga WHERE carga_key = 1"
        ).fetchone()
        if metadata is None:
            errors.append("No se encontró el registro de auditoría de la carga.")
        elif (
            metadata["registros_csv"] != source_count
            or metadata["registros_hecho"] != len(source_rows)
            or metadata["duplicados_exactos_omitidos"] != exact_duplicates
        ):
            errors.append(
                "La auditoría de carga no coincide con el CSV "
                f"(CSV={source_count}, esperado hecho={len(source_rows)}, "
                f"duplicados={exact_duplicates})."
            )

        actual_fact_count = connection.execute(
            "SELECT COUNT(*) FROM fact_proceso"
        ).fetchone()[0]
        if actual_fact_count != len(source_rows):
            errors.append(
                f"Conteo del hecho: esperado {len(source_rows)}, "
                f"encontrado {actual_fact_count}."
            )

        # Comprobación 1: claves primarias y claves naturales dimensionales.
        for table, (key_column, _) in DIMENSIONS.items():
            duplicate_surrogates = connection.execute(
                f"SELECT COUNT(*) FROM ("
                f"SELECT {key_column} FROM {table} GROUP BY {key_column} "
                f"HAVING COUNT(*) > 1)"
            ).fetchone()[0]
            duplicate_natural = connection.execute(
                f"SELECT COUNT(*) FROM ("
                f"SELECT clave_natural FROM {table} GROUP BY clave_natural "
                f"HAVING COUNT(*) > 1)"
            ).fetchone()[0]
            if duplicate_surrogates or duplicate_natural:
                errors.append(f"Hay claves duplicadas en {table}.")

        # Comprobación 2: claves foráneas sin huérfanos.
        foreign_key_errors = connection.execute(
            "PRAGMA foreign_key_check"
        ).fetchall()
        if foreign_key_errors:
            errors.append(
                f"Se encontraron {len(foreign_key_errors)} violaciones de FK."
            )

        # Comprobación 3: huellas únicas en el hecho.
        duplicate_facts = connection.execute(
            """
            SELECT COUNT(*) FROM (
                SELECT huella_origen FROM fact_proceso
                GROUP BY huella_origen HAVING COUNT(*) > 1
            )
            """
        ).fetchone()[0]
        if duplicate_facts:
            errors.append(f"Hay {duplicate_facts} huellas repetidas en el hecho.")

        # Comprobación 4: existe un miembro desconocido en cada dimensión.
        for table, (key_column, _) in DIMENSIONS.items():
            unknown_members = connection.execute(
                f"SELECT * FROM {table} WHERE {key_column} = ?",
                (UNKNOWN_KEY,),
            ).fetchall()
            if len(unknown_members) != 1:
                errors.append(
                    f"{table} debe tener exactamente un miembro Desconocido."
                )
            else:
                unknown_member = unknown_members[0]
                attribute_columns = DIMENSIONS[table][1]
                invalid_labels = [
                    column
                    for column in attribute_columns
                    if unknown_member[column] != "Desconocido"
                    and not (
                        table == "dim_tiempo"
                        and column in {"anio", "trimestre", "mes", "dia"}
                        and unknown_member[column] is None
                    )
                ]
                if invalid_labels:
                    errors.append(
                        f"El miembro Desconocido de {table} tiene atributos "
                        f"inesperados: {invalid_labels}."
                    )
            source_columns = DIMENSION_SOURCE_COLUMNS[table]
            expected_unknown = sum(
                all(
                    not (row.get(column) or "").strip()
                    for column in source_columns
                )
                for row in source_rows
            )
            foreign_key = table.removeprefix("dim_") + "_key"
            actual_unknown = connection.execute(
                f"SELECT COUNT(*) FROM fact_proceso WHERE {foreign_key} = ?",
                (UNKNOWN_KEY,),
            ).fetchone()[0]
            if actual_unknown != expected_unknown:
                errors.append(
                    f"Manejo de faltantes inconsistente en {table}: "
                    f"esperado {expected_unknown} hechos desconocidos, "
                    f"encontrado {actual_unknown}."
                )

        # Conciliación de medidas sobre filas no duplicadas exactamente.
        expected_base_sum = sum(
            source_integer(row, "precio_base") or 0 for row in source_rows
        )
        expected_awarded_sum = sum(
            source_integer(row, "valor_total_adjudicacion") or 0
            for row in source_rows
        )
        actual_sums = connection.execute(
            """
            SELECT
                COALESCE(SUM(precio_base_cop), 0) AS precio_base_cop,
                COALESCE(SUM(valor_total_adjudicacion_cop), 0)
                    AS valor_total_adjudicacion_cop
            FROM fact_proceso
            """
        ).fetchone()
        if actual_sums["precio_base_cop"] != expected_base_sum:
            errors.append(
                "La suma de precio_base no concilia: "
                f"CSV sin duplicados={expected_base_sum}, "
                f"hecho={actual_sums['precio_base_cop']}."
            )
        if actual_sums["valor_total_adjudicacion_cop"] != expected_awarded_sum:
            errors.append(
                "La suma de valor_total_adjudicacion no concilia: "
                f"CSV sin duplicados={expected_awarded_sum}, "
                f"hecho={actual_sums['valor_total_adjudicacion_cop']}."
            )

        # Comprobación 5: conteo por modalidad, incluida la categoría nula.
        expected_by_modality = Counter(
            row.get("modalidad_de_contratacion") for row in source_rows
        )
        actual_by_modality = {
            row["modalidad_de_contratacion"]: row["cantidad"]
            for row in connection.execute(
                """
                SELECT c.modalidad_de_contratacion, COUNT(*) AS cantidad
                FROM fact_proceso f
                JOIN dim_contratacion c
                    ON c.contratacion_key = f.contratacion_key
                GROUP BY c.modalidad_de_contratacion
                """
            )
        }
        if dict(expected_by_modality) != actual_by_modality:
            errors.append(
                "El conteo por modalidad no concilia entre CSV y hecho."
            )

        expected_unique_processes = len(
            {
                row.get("id_del_proceso")
                for row in source_rows
                if row.get("id_del_proceso")
            }
        )
        actual_unique_processes = connection.execute(
            "SELECT COUNT(DISTINCT id_del_proceso) FROM fact_proceso"
        ).fetchone()[0]
        if actual_unique_processes != expected_unique_processes:
            errors.append(
                "El conteo distinto de id_del_proceso no concilia: "
                f"CSV={expected_unique_processes}, hecho={actual_unique_processes}."
            )

        print(f"Registros CSV: {source_count}")
        print(f"Duplicados exactos excluidos: {exact_duplicates}")
        print(f"Filas esperadas en el hecho: {len(source_rows)}")
        print(f"Filas actuales en el hecho: {actual_fact_count}")
        print(f"Procesos únicos esperados / hecho: {expected_unique_processes} / {actual_unique_processes}")
        print(f"Suma precio_base esperada / hecho (COP): {expected_base_sum} / {actual_sums['precio_base_cop']}")
        print(
            "Suma valor adjudicado esperada / hecho (COP): "
            f"{expected_awarded_sum} / "
            f"{actual_sums['valor_total_adjudicacion_cop']}"
        )
        print("Conteo por modalidad: " + ("coincide" if dict(expected_by_modality) == actual_by_modality else "no coincide"))
        print("Integridad de claves foráneas: " + ("correcta" if not foreign_key_errors else "con errores"))
        if errors:
            print("\nVALIDACIÓN FALLIDA")
            for error in errors:
                print(f"- {error}")
        else:
            print("\nVALIDACIÓN CORRECTA")
    finally:
        connection.close()
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    args = parser.parse_args()
    try:
        errors = validate(args.csv, args.db)
    except (OSError, sqlite3.Error, ValueError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1) from error
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
