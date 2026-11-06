#!/usr/bin/env python3
"""Carga idempotente del CSV tratado en el modelo estrella de la Etapa 5."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sqlite3
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CSV = ROOT / "dataset" / "processed" / "secop_ii_nacional.csv"
DEFAULT_DB = ROOT / "data" / "etapa5.sqlite"
SCHEMA_FILE = ROOT / "sql" / "schema.sql"
UNKNOWN_KEY = -1
UNKNOWN_LABEL = "Desconocido"

EXPECTED_COLUMNS = {
    "entidad",
    "nit_entidad",
    "departamento_entidad",
    "ciudad_entidad",
    "ordenentidad",
    "id_del_proceso",
    "referencia_del_proceso",
    "nombre_del_procedimiento",
    "descripci_n_del_procedimiento",
    "fase",
    "fecha_de_publicacion_del",
    "precio_base",
    "modalidad_de_contratacion",
    "duracion",
    "unidad_de_duracion",
    "ciudad_de_la_unidad_de",
    "proveedores_invitados",
    "proveedores_con_invitacion",
    "respuestas_al_procedimiento",
    "conteo_de_respuestas_a_ofertas",
    "proveedores_unicos_con",
    "numero_de_lotes",
    "estado_del_procedimiento",
    "adjudicado",
    "departamento_proveedor",
    "ciudad_proveedor",
    "valor_total_adjudicacion",
    "nombre_del_proveedor",
    "nit_del_proveedor_adjudicado",
    "codigo_principal_de_categoria",
    "tipo_de_contrato",
    "subtipo_de_contrato",
    "urlproceso",
    "codigo_entidad",
}

DIMENSIONS = {
    "dim_tiempo": (
        "tiempo_key",
        ("fecha_publicacion", "anio", "trimestre", "mes", "dia"),
    ),
    "dim_entidad": (
        "entidad_key",
        ("codigo_entidad", "nit_entidad", "nombre_entidad", "orden_entidad"),
    ),
    "dim_territorio": (
        "territorio_key",
        ("departamento_entidad", "ciudad_entidad"),
    ),
    "dim_contratacion": (
        "contratacion_key",
        (
            "modalidad_de_contratacion",
            "tipo_de_contrato",
            "subtipo_de_contrato",
            "fase",
            "estado_del_procedimiento",
            "adjudicado",
        ),
    ),
    "dim_proveedor": (
        "proveedor_key",
        (
            "nit_del_proveedor_adjudicado",
            "nombre_del_proveedor",
            "departamento_proveedor",
            "ciudad_proveedor",
        ),
    ),
}

DIMENSION_SOURCE_COLUMNS = {
    "dim_tiempo": ("fecha_de_publicacion_del",),
    "dim_entidad": ("codigo_entidad", "nit_entidad", "entidad", "ordenentidad"),
    "dim_territorio": ("departamento_entidad", "ciudad_entidad"),
    "dim_contratacion": (
        "modalidad_de_contratacion",
        "tipo_de_contrato",
        "subtipo_de_contrato",
        "fase",
        "estado_del_procedimiento",
        "adjudicado",
    ),
    "dim_proveedor": (
        "nit_del_proveedor_adjudicado",
        "nombre_del_proveedor",
        "departamento_proveedor",
        "ciudad_proveedor",
    ),
}


def canonical_key(values: tuple[Any, ...]) -> str:
    return json.dumps(values, ensure_ascii=False, separators=(",", ":"))


def fingerprint(row: dict[str, str], columns: list[str]) -> str:
    payload = json.dumps(
        [row.get(column, "") for column in columns],
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def source_text(row: dict[str, str], column: str) -> str | None:
    value = row.get(column)
    if value is None or not value.strip():
        return None
    return value


def integer_value(row: dict[str, str], column: str) -> int | None:
    value = source_text(row, column)
    if value is None:
        return None
    try:
        number = Decimal(value)
    except InvalidOperation as error:
        raise ValueError(f"{column}: valor no numérico {value!r}") from error
    if not number.is_finite() or number != number.to_integral_value():
        raise ValueError(f"{column}: se esperaba un entero, se recibió {value!r}")
    return int(number)


def time_attributes(row: dict[str, str]) -> tuple[Any, ...] | None:
    value = source_text(row, "fecha_de_publicacion_del")
    if value is None:
        return None
    try:
        published = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise ValueError(
            f"fecha_de_publicacion_del inválida: {value!r}"
        ) from error
    date = published.date()
    return (
        date.isoformat(),
        date.year,
        (date.month - 1) // 3 + 1,
        date.month,
        date.day,
    )


def dimension_attributes(
    table: str, row: dict[str, str]
) -> tuple[Any, ...] | None:
    if table == "dim_tiempo":
        return time_attributes(row)
    return tuple(
        source_text(row, column) for column in DIMENSION_SOURCE_COLUMNS[table]
    )


def dimension_key(
    connection: sqlite3.Connection,
    table: str,
    row: dict[str, str],
    cache: dict[tuple[str, tuple[Any, ...]], int],
) -> int:
    key_column, attribute_columns = DIMENSIONS[table]
    attributes = dimension_attributes(table, row)
    if attributes is None or all(value is None for value in attributes):
        return UNKNOWN_KEY

    cache_key = (table, attributes)
    if cache_key in cache:
        return cache[cache_key]

    natural_key = canonical_key(attributes)
    cursor = connection.execute(
        f"INSERT INTO {table} (clave_natural, "
        + ", ".join(attribute_columns)
        + ") VALUES ("
        + ", ".join("?" for _ in range(len(attribute_columns) + 1))
        + ")",
        (natural_key, *attributes),
    )
    surrogate_key = int(cursor.lastrowid)
    cache[cache_key] = surrogate_key
    return surrogate_key


def seed_unknown_members(connection: sqlite3.Connection) -> None:
    unknown_rows = {
        "dim_tiempo": (
            "tiempo_key",
            "clave_natural, fecha_publicacion, anio, trimestre, mes, dia",
            ("Desconocido", UNKNOWN_LABEL, None, None, None, None),
        ),
        "dim_entidad": (
            "entidad_key",
            "clave_natural, codigo_entidad, nit_entidad, nombre_entidad, orden_entidad",
            ("Desconocido", UNKNOWN_LABEL, UNKNOWN_LABEL, UNKNOWN_LABEL, UNKNOWN_LABEL),
        ),
        "dim_territorio": (
            "territorio_key",
            "clave_natural, departamento_entidad, ciudad_entidad",
            ("Desconocido", UNKNOWN_LABEL, UNKNOWN_LABEL),
        ),
        "dim_contratacion": (
            "contratacion_key",
            "clave_natural, modalidad_de_contratacion, tipo_de_contrato, "
            "subtipo_de_contrato, fase, estado_del_procedimiento, adjudicado",
            (
                "Desconocido",
                UNKNOWN_LABEL,
                UNKNOWN_LABEL,
                UNKNOWN_LABEL,
                UNKNOWN_LABEL,
                UNKNOWN_LABEL,
                UNKNOWN_LABEL,
            ),
        ),
        "dim_proveedor": (
            "proveedor_key",
            "clave_natural, nit_del_proveedor_adjudicado, nombre_del_proveedor, "
            "departamento_proveedor, ciudad_proveedor",
            (
                "Desconocido",
                UNKNOWN_LABEL,
                UNKNOWN_LABEL,
                UNKNOWN_LABEL,
                UNKNOWN_LABEL,
            ),
        ),
    }
    for table, (key_column, columns, values) in unknown_rows.items():
        placeholders = ", ".join("?" for _ in range(len(values) + 1))
        connection.execute(
            f"INSERT INTO {table} ({key_column}, {columns}) "
            f"VALUES ({placeholders})",
            (UNKNOWN_KEY, *values),
        )


def load(csv_path: Path, database_path: Path) -> tuple[int, int, int]:
    if not csv_path.is_file():
        raise FileNotFoundError(f"No existe el CSV de entrada: {csv_path}")
    if not SCHEMA_FILE.is_file():
        raise FileNotFoundError(f"No existe el esquema SQL: {SCHEMA_FILE}")

    database_path.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(database_path)
    connection.execute("PRAGMA foreign_keys = ON")
    try:
        connection.executescript(
            SCHEMA_FILE.read_text(encoding="utf-8")
        )
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

        with connection:
            for table in (
                "fact_proceso",
                "dim_tiempo",
                "dim_entidad",
                "dim_territorio",
                "dim_contratacion",
                "dim_proveedor",
                "etl_carga",
            ):
                connection.execute(f"DELETE FROM {table}")
            seed_unknown_members(connection)

            cache: dict[tuple[str, tuple[Any, ...]], int] = {}
            seen_fingerprints: set[str] = set()
            duplicates = 0
            loaded = 0
            for record_number, row in enumerate(rows, start=1):
                row_fingerprint = fingerprint(row, columns)
                if row_fingerprint in seen_fingerprints:
                    duplicates += 1
                    continue
                seen_fingerprints.add(row_fingerprint)

                keys = {
                    table: dimension_key(connection, table, row, cache)
                    for table in DIMENSIONS
                }
                connection.execute(
                    """
                    INSERT INTO fact_proceso (
                        numero_registro_origen, huella_origen,
                        tiempo_key, entidad_key, territorio_key,
                        contratacion_key, proveedor_key,
                        id_del_proceso, referencia_del_proceso,
                        nombre_del_procedimiento, descripcion_del_procedimiento,
                        duracion, unidad_de_duracion, ciudad_de_la_unidad_de,
                        precio_base_cop, proveedores_invitados,
                        proveedores_con_invitacion, respuestas_al_procedimiento,
                        conteo_de_respuestas_a_ofertas, proveedores_unicos_con,
                        numero_de_lotes, valor_total_adjudicacion_cop,
                        codigo_principal_de_categoria, urlproceso
                    ) VALUES (
                        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                        ?, ?, ?, ?, ?
                    )
                    """,
                    (
                        record_number,
                        row_fingerprint,
                        keys["dim_tiempo"],
                        keys["dim_entidad"],
                        keys["dim_territorio"],
                        keys["dim_contratacion"],
                        keys["dim_proveedor"],
                        source_text(row, "id_del_proceso"),
                        source_text(row, "referencia_del_proceso"),
                        source_text(row, "nombre_del_procedimiento"),
                        source_text(row, "descripci_n_del_procedimiento"),
                        integer_value(row, "duracion"),
                        source_text(row, "unidad_de_duracion"),
                        source_text(row, "ciudad_de_la_unidad_de"),
                        integer_value(row, "precio_base"),
                        integer_value(row, "proveedores_invitados"),
                        integer_value(row, "proveedores_con_invitacion"),
                        integer_value(row, "respuestas_al_procedimiento"),
                        integer_value(row, "conteo_de_respuestas_a_ofertas"),
                        integer_value(row, "proveedores_unicos_con"),
                        integer_value(row, "numero_de_lotes"),
                        integer_value(row, "valor_total_adjudicacion"),
                        source_text(row, "codigo_principal_de_categoria"),
                        source_text(row, "urlproceso"),
                    ),
                )
                loaded += 1

            connection.execute(
                """
                INSERT INTO etl_carga (
                    carga_key, archivo_origen, registros_csv, registros_hecho,
                    duplicados_exactos_omitidos, cargado_en_utc
                ) VALUES (1, ?, ?, ?, ?, ?)
                """,
                (
                    str(csv_path.resolve()),
                    len(rows),
                    loaded,
                    duplicates,
                    datetime.now(timezone.utc).isoformat(),
                ),
            )
        return len(rows), loaded, duplicates
    finally:
        connection.close()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--csv", type=Path, default=DEFAULT_CSV)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB)
    args = parser.parse_args()
    source_count, loaded_count, duplicate_count = load(args.csv, args.db)
    print(f"Registros CSV leídos: {source_count}")
    print(f"Registros cargados al hecho: {loaded_count}")
    print(f"Duplicados exactos omitidos: {duplicate_count}")
    print(f"Base SQLite: {args.db.resolve()}")


if __name__ == "__main__":
    main()
