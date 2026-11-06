"""Consultas OLAP parametrizadas sobre el esquema estrella de la Etapa 5."""

from __future__ import annotations

import sqlite3
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATABASE = ROOT / "data" / "etapa5.sqlite"
NULL_FILTER = "__valor_nulo__"

DIMENSIONS = {
    "anio": {
        "label": "Año de publicación",
        "expression": "t.anio",
        "dimension": "Tiempo",
    },
    "trimestre": {
        "label": "Trimestre de publicación",
        "expression": "t.trimestre",
        "dimension": "Tiempo",
    },
    "mes": {
        "label": "Mes de publicación",
        "expression": "t.mes",
        "dimension": "Tiempo",
    },
    "dia": {
        "label": "Día de publicación",
        "expression": "t.dia",
        "dimension": "Tiempo",
    },
    "orden": {
        "label": "Orden de la entidad",
        "expression": "e.orden_entidad",
        "dimension": "Entidad",
    },
    "entidad": {
        "label": "Código y nombre de la entidad",
        "expression": (
            "COALESCE(e.codigo_entidad, 'Sin código') || ' · ' || "
            "COALESCE(e.nombre_entidad, 'Sin nombre')"
        ),
        "dimension": "Entidad",
    },
    "departamento": {
        "label": "Departamento de la entidad",
        "expression": "r.departamento_entidad",
        "dimension": "Territorio",
    },
    "ciudad": {
        "label": "Ciudad de la entidad",
        "expression": "r.ciudad_entidad",
        "dimension": "Territorio",
    },
    "modalidad": {
        "label": "Modalidad de contratación",
        "expression": "c.modalidad_de_contratacion",
        "dimension": "Contratación",
    },
    "tipo_contrato": {
        "label": "Tipo de contrato",
        "expression": "c.tipo_de_contrato",
        "dimension": "Contratación",
    },
    "estado": {
        "label": "Estado del procedimiento",
        "expression": "c.estado_del_procedimiento",
        "dimension": "Contratación",
    },
    "adjudicado": {
        "label": "Adjudicado",
        "expression": "c.adjudicado",
        "dimension": "Contratación",
    },
    "departamento_proveedor": {
        "label": "Departamento del proveedor",
        "expression": "p.departamento_proveedor",
        "dimension": "Proveedor",
    },
    "ciudad_proveedor": {
        "label": "Ciudad del proveedor",
        "expression": "p.ciudad_proveedor",
        "dimension": "Proveedor",
    },
    "proveedor": {
        "label": "Proveedor adjudicado",
        "expression": "p.nombre_del_proveedor",
        "dimension": "Proveedor",
    },
    "proveedor_identificado": {
        "label": "Identificación del proveedor",
        "expression": (
            "CASE WHEN p.nit_del_proveedor_adjudicado IS NULL "
            "OR p.nit_del_proveedor_adjudicado = 'No Definido' "
            "THEN 'No identificado en la fuente' "
            "ELSE 'NIT reportado' END"
        ),
        "dimension": "Proveedor",
    },
}

VIEWS = {
    "composicion": {
        "title": "Composición y distribución",
        "question": (
            "¿Cómo se distribuyen los registros y el valor adjudicado por "
            "modalidad y tipo de contrato al cruzar orden de entidad y "
            "departamento de la entidad?"
        ),
        "dimensions": ["Contratación", "Entidad", "Territorio"],
        "measures": [
            "Registros",
            "Procesos únicos",
            "Valor adjudicado (COP)",
            "Precio base promedio (COP)",
        ],
        "continuity": (
            "En la Etapa 4, dos modalidades reunían el 84,94 % de la muestra "
            "y prestación de servicios representaba el 67,31 % de las filas. "
            "Esta vista amplía ese conteo cruzando modalidad y tipo de "
            "contrato con el territorio y el orden de la entidad, y permite "
            "comparar también procesos distintos y valores adjudicados. "
            "Modalidad y tipo son categorías cruzadas, no niveles de una "
            "jerarquía."
        ),
        "drill_path": ["departamento", "ciudad"],
        "secondary": "tipo_contrato",
        "matrix": ("modalidad", "tipo_contrato"),
        "hierarchies": [
            "Departamento de la entidad → ciudad de la entidad."
        ],
        "filters": (
            ("departamento", "Departamento de la entidad"),
            ("estado", "Estado del procedimiento"),
        ),
        "insights": (
            {
                "dimension": "modalidad",
                "group_dimensions": ["modalidad", "departamento"],
                "metric": "rows",
                "question": (
                    "¿Qué combinación de modalidad y departamento concentra "
                    "más registros?"
                ),
                "procedure": (
                    "Cruzar modalidad con departamento de entidad y contar "
                    "las filas del hecho; la participación del grupo superior "
                    "se divide entre todas las filas visibles tras los filtros."
                ),
                "interpretation": (
                    "El resultado describe el peso de la categoría dentro "
                    "del corte filtrado; no explica por qué se eligió esa "
                    "modalidad ni mide competencia efectiva."
                ),
                "utility": (
                    "Apoya la priorización de una revisión documental de las "
                    "categorías de mayor volumen."
                ),
                "limitation": (
                    "El conteo es de filas depuradas exactamente, no de "
                    "contratos firmados ni de procesos únicos."
                ),
            },
            {
                "dimension": "tipo_contrato",
                "group_dimensions": ["tipo_contrato", "orden"],
                "metric": "awarded",
                "question": (
                    "¿Qué combinación de tipo contractual y orden de entidad "
                    "reúne más valor adjudicado?"
                ),
                "procedure": (
                    "Cruzar tipo de contrato con orden de entidad y sumar "
                    "valor adjudicado; el denominador es el valor total "
                    "visible tras los filtros activos."
                ),
                "interpretation": (
                    "La asociación muestra dónde se registra el mayor monto; "
                    "no demuestra calidad, irregularidad ni ejecución del "
                    "gasto."
                ),
                "utility": (
                    "Ayuda a seleccionar expedientes de mayor monto para "
                    "verificar su soporte y trazabilidad."
                ),
                "limitation": (
                    "Los montos son sumas por fila del dataset y pueden "
                    "reflejar varias filas distintas del mismo ID de proceso."
                ),
            },
        ),
    },
    "territorio": {
        "title": "Comparación territorial",
        "question": (
            "¿Cómo cambian el volumen de registros y el valor adjudicado "
            "entre departamentos y ciudades según el orden de entidad y "
            "el estado del procedimiento?"
        ),
        "dimensions": ["Territorio", "Entidad", "Contratación"],
        "hierarchies": ["Departamento de la entidad → ciudad de la entidad."],
        "measures": [
            "Registros",
            "Procesos únicos",
            "Valor adjudicado (COP)",
            "Precio base promedio (COP)",
        ],
        "continuity": (
            "La Etapa 4 mostró que las entidades territoriales aportaban "
            "6.199 de 10.000 filas y concentraban el 58,10 % del valor "
            "adjudicado de aquella muestra. Esta vista profundiza la "
            "comparación con el nivel departamento → ciudad, el estado de "
            "adjudicación y medidas recalculadas sobre el CSV tratado de "
            "esta etapa; las bases de filas difieren porque aquí se excluyen "
            "79 duplicados exactos."
        ),
        "drill_path": ["departamento", "ciudad"],
        "secondary": "orden",
        "matrix": ("departamento", "orden"),
        "filters": (
            ("orden", "Orden de la entidad"),
            ("adjudicado", "Adjudicado"),
        ),
        "insights": (
            {
                "dimension": "departamento",
                "group_dimensions": ["departamento", "orden"],
                "metric": "rows",
                "question": (
                    "¿Qué combinación de departamento y orden de entidad "
                    "concentra más registros?"
                ),
                "procedure": (
                    "Cruzar departamento de entidad con orden de entidad y "
                    "contar filas; la participación se calcula sobre todas "
                    "las filas del corte, incluyendo 'No Definido'."
                ),
                "interpretation": (
                    "La ubicación con mayor volumen es una concentración "
                    "descriptiva, no evidencia de mayor necesidad, calidad "
                    "o riesgo."
                ),
                "utility": (
                    "Permite orientar muestreos de expedientes por territorio."
                ),
                "limitation": (
                    "El campo es la ubicación reportada de la entidad; no "
                    "necesariamente es el lugar de ejecución contractual."
                ),
            },
            {
                "dimension": "orden",
                "group_dimensions": ["orden", "adjudicado"],
                "metric": "awarded",
                "question": (
                    "¿Qué combinación de orden de entidad y adjudicación "
                    "acumula más valor?"
                ),
                "procedure": (
                    "Cruzar orden de entidad con estado de adjudicación y "
                    "sumar el valor; el denominador es la suma del corte "
                    "filtrado."
                ),
                "interpretation": (
                    "Describe la distribución del monto registrado; no "
                    "evalúa eficiencia ni desempeño de las entidades."
                ),
                "utility": (
                    "Sirve para asignar capacidad de revisión de acuerdo "
                    "con la concentración monetaria observada."
                ),
                "limitation": (
                    "Los valores cero se conservan; una suma no equivale a "
                    "pagos ni ejecución presupuestal."
                ),
            },
        ),
    },
    "temporal": {
        "title": "Comportamiento temporal",
        "question": (
            "¿Cómo varían el número de registros publicados y el valor "
            "adjudicado por año, trimestre y mes de publicación al segmentar "
            "por modalidad y departamento de la entidad?"
        ),
        "dimensions": ["Tiempo", "Contratación", "Territorio"],
        "hierarchies": [
            "Año → trimestre → mes → día, sobre pares mes-día comunes a todos "
            "los años observados."
        ],
        "measures": [
            "Registros",
            "Procesos únicos",
            "Valor adjudicado (COP)",
            "Precio base promedio (COP)",
        ],
        "continuity": (
            "La Etapa 4 reportó concentraciones del valor adjudicado en "
            "meses de 2025, incluido agosto. Esta vista no repite ese corte: "
            "compara años y niveles de la jerarquía año → trimestre → mes "
            "→ día usando pares mes-día observados en todos los años, y "
            "recalcula conteos, procesos distintos y valores para ese "
            "periodo comparable."
        ),
        "drill_path": ["anio", "trimestre", "mes", "dia"],
        "secondary": "modalidad",
        "matrix": ("mes", "modalidad"),
        "filters": (
            ("modalidad", "Modalidad de contratación"),
            ("departamento", "Departamento de la entidad"),
        ),
        "insights": (
            {
                "dimension": "anio",
                "group_dimensions": ["anio", "modalidad"],
                "metric": "rows",
                "question": (
                    "¿Qué combinación de año de publicación y modalidad "
                    "presenta más registros?"
                ),
                "procedure": (
                    "Cruzar año con modalidad y contar filas para los mismos "
                    "pares de mes y día observados en todos los años; el "
                    "denominador incluye todas las filas de ese corte comparable."
                ),
                "interpretation": (
                    "Compara conteos para ventanas de meses equivalentes. "
                    "No implica una tendencia de la población SECOP ni una "
                    "causa del cambio observado."
                ),
                "utility": (
                    "Ayuda a seleccionar periodos comparables para una "
                    "revisión temporal posterior."
                ),
                "limitation": (
                    "El archivo es una muestra con cuotas mensuales y no "
                    "representa el universo; los periodos están limitados a "
                    "las fechas mes-día comunes que sí aparecen en todos "
                    "los años."
                ),
                "common_months": True,
            },
            {
                "dimension": "modalidad",
                "group_dimensions": ["modalidad", "departamento"],
                "metric": "awarded",
                "question": (
                    "¿Qué combinación de modalidad y departamento concentra "
                    "valor adjudicado en el corte?"
                ),
                "procedure": (
                    "Cruzar modalidad con departamento de entidad y sumar "
                    "valor adjudicado en las fechas mes-día comunes; el "
                    "denominador es esa suma, no el conteo."
                ),
                "interpretation": (
                    "Muestra concentración monetaria descriptiva. No "
                    "demuestra que la modalidad haya causado el monto ni "
                    "que exista una irregularidad."
                ),
                "utility": (
                    "Permite identificar modalidades y expedientes que "
                    "merecen verificar su documentación."
                ),
                "limitation": (
                    "La fecha disponible es la de publicación, no la fecha "
                    "de adjudicación, firma o pago."
                ),
            },
        ),
    },
    "multidimensional": {
        "title": "Análisis multidimensional",
        "question": (
            "¿Cómo se cruzan orden de entidad, contratación y proveedor en "
            "el número de registros y el valor adjudicado?"
        ),
        "dimensions": ["Entidad", "Contratación", "Proveedor", "Territorio"],
        "measures": [
            "Registros",
            "Procesos únicos",
            "Valor adjudicado (COP)",
            "Precio base promedio (COP)",
        ],
        "continuity": (
            "El análisis multivariado de la Etapa 4 encontró que prestación "
            "de servicios sumaba 6.731 filas, de las cuales 4.234 eran de "
            "entidades territoriales. Esta vista vuelve a cruzar orden y "
            "modalidad, pero incorpora la disponibilidad del NIT y la "
            "dimensión de proveedor para comparar valores adjudicados; "
            "el drill-down válido orden de entidad → entidad muestra el "
            "detalle institucional mediante el código y nombre de entidad."
        ),
        "drill_path": ["orden", "entidad"],
        "hierarchies": [
            "Orden de la entidad → código y nombre de la entidad contratante."
        ],
        "secondary": "proveedor_identificado",
        "matrix": ("orden", "modalidad"),
        "filters": (
            ("departamento_proveedor", "Departamento del proveedor"),
            ("modalidad", "Modalidad de contratación"),
        ),
        "insights": (
            {
                "dimension": "orden",
                "group_dimensions": ["orden", "modalidad"],
                "metric": "rows",
                "question": (
                    "¿Qué combinación de orden de entidad y modalidad "
                    "registra más filas?"
                ),
                "procedure": (
                    "Cruzar orden de entidad con modalidad, contar filas y "
                    "calcular participación respecto al total filtrado."
                ),
                "interpretation": (
                    "Describe la distribución de registros del corte y no "
                    "establece la causa de la diferencia entre órdenes."
                ),
                "utility": (
                    "Ayuda a contextualizar la carga de revisión por orden "
                    "de entidad."
                ),
                "limitation": (
                    "El volumen no pondera valor, complejidad ni población "
                    "atendida."
                ),
            },
            {
                "dimension": "proveedor_identificado",
                "group_dimensions": ["proveedor_identificado", "modalidad"],
                "metric": "awarded",
                "question": (
                    "¿Qué combinación de disponibilidad del NIT y modalidad "
                    "reúne más valor adjudicado?"
                ),
                "procedure": (
                    "Cruzar disponibilidad literal del NIT con modalidad y "
                    "sumar valor adjudicado. El porcentaje usa como "
                    "denominador todo el valor del corte filtrado."
                ),
                "interpretation": (
                    "La clasificación describe disponibilidad del campo; "
                    "un NIT reportado no confirma identidad verificada, y "
                    "'No Definido' no prueba ausencia de proveedor."
                ),
                "utility": (
                    "Permite priorizar la mejora de completitud y la "
                    "verificación documental de identificadores."
                ),
                "limitation": (
                    "La dimensión de proveedor está incompleta en la fuente; "
                    "la categoría no constituye una evaluación de "
                    "transparencia o competencia."
                ),
            },
        ),
    },
}

ALIASES = {
    "rows": "COUNT(*)",
    "unique": "COUNT(DISTINCT f.id_del_proceso)",
    "awarded": "COALESCE(SUM(f.valor_total_adjudicacion_cop), 0)",
    "average": "AVG(f.precio_base_cop)",
}

FROM_SQL = """
    fact_proceso f
    JOIN dim_tiempo t ON t.tiempo_key = f.tiempo_key
    JOIN dim_entidad e ON e.entidad_key = f.entidad_key
    JOIN dim_territorio r ON r.territorio_key = f.territorio_key
    JOIN dim_contratacion c ON c.contratacion_key = f.contratacion_key
    JOIN dim_proveedor p ON p.proveedor_key = f.proveedor_key
"""

class InvalidSelection(ValueError):
    """Selección de dimensión, nivel u operación no permitida."""


def _connect(database: Path = DATABASE) -> sqlite3.Connection:
    if not database.is_file():
        raise FileNotFoundError(
            "No existe la base del modelo estrella. Ejecuta "
            "`python etl/load_star_schema.py` desde la raíz del proyecto."
        )
    connection = sqlite3.connect(database)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def _validate_filter(
    connection: sqlite3.Connection, dimension_id: str, value: str | None
) -> str | None:
    if value in (None, ""):
        return None
    expression = DIMENSIONS[dimension_id]["expression"]
    if value == NULL_FILTER:
        found = connection.execute(
            f"SELECT 1 FROM {FROM_SQL} WHERE {expression} IS NULL LIMIT 1"
        ).fetchone()
        if not found:
            raise InvalidSelection("El filtro de valor vacío no está disponible.")
        return value
    found = connection.execute(
        f"SELECT 1 FROM {FROM_SQL} WHERE {expression} = ? LIMIT 1",
        (value,),
    ).fetchone()
    if not found:
        raise InvalidSelection("El valor elegido no existe en el filtro.")
    return value


def _where_clause(
    filters: list[tuple[str, str | None]],
    period_days: list[tuple[int, int]] | None = None,
) -> tuple[str, list[Any]]:
    clauses = []
    parameters: list[Any] = []
    for dimension_id, value in filters:
        if value is None:
            continue
        expression = DIMENSIONS[dimension_id]["expression"]
        if value == NULL_FILTER:
            clauses.append(f"{expression} IS NULL")
        else:
            clauses.append(f"{expression} = ?")
            parameters.append(value)
    if period_days is not None:
        if not period_days:
            clauses.append("1 = 0")
        else:
            date_clauses = " OR ".join(
                "(t.mes = ? AND t.dia = ?)" for _ in period_days
            )
            clauses.append(f"({date_clauses})")
            parameters.extend(
                value for month_day in period_days for value in month_day
            )
    return (" WHERE " + " AND ".join(clauses) if clauses else "", parameters)


def _aggregate(
    connection: sqlite3.Connection,
    dimension_ids: list[str],
    filters: list[tuple[str, str | None]],
    metric: str = "awarded",
    limit: int = 100,
    period_days: list[tuple[int, int]] | None = None,
) -> list[dict[str, Any]]:
    if metric not in ALIASES:
        raise InvalidSelection("Medida no permitida.")
    select_parts = [
        f"{DIMENSIONS[dimension_id]['expression']} AS value_{index}"
        for index, dimension_id in enumerate(dimension_ids)
    ]
    group_parts = [
        DIMENSIONS[dimension_id]["expression"]
        for dimension_id in dimension_ids
    ]
    select_parts.extend(
        [
            f"{ALIASES['rows']} AS record_count",
            f"{ALIASES['unique']} AS unique_processes",
            f"{ALIASES['awarded']} AS awarded_cop",
            f"{ALIASES['average']} AS average_base_cop",
        ]
    )
    where_sql, parameters = _where_clause(filters, period_days)
    group_sql = " GROUP BY " + ", ".join(group_parts) if group_parts else ""
    order_expression = ALIASES[metric]
    query = (
        "SELECT "
        + ", ".join(select_parts)
        + f" FROM {FROM_SQL}{where_sql}{group_sql} "
        + f"ORDER BY {order_expression} DESC LIMIT ?"
    )
    rows = connection.execute(query, (*parameters, limit)).fetchall()
    result = []
    for row in rows:
        dimensions = [
            {"id": dimension_id, "value": row[f"value_{index}"]}
            for index, dimension_id in enumerate(dimension_ids)
        ]
        result.append(
            {
                "dimensions": dimensions,
                "label": " · ".join(
                    "(Vacío)" if item["value"] is None else str(item["value"])
                    for item in dimensions
                )
                or "Total",
                "record_count": row["record_count"],
                "unique_processes": row["unique_processes"],
                "awarded_cop": row["awarded_cop"],
                "average_base_cop": row["average_base_cop"],
            }
        )
    return result


def _total(
    connection: sqlite3.Connection,
    filters: list[tuple[str, str | None]],
    period_days: list[tuple[int, int]] | None = None,
) -> dict[str, Any]:
    where_sql, parameters = _where_clause(filters, period_days)
    row = connection.execute(
        f"""
        SELECT
            {ALIASES['rows']} AS record_count,
            {ALIASES['unique']} AS unique_processes,
            {ALIASES['awarded']} AS awarded_cop,
            {ALIASES['average']} AS average_base_cop
        FROM {FROM_SQL}{where_sql}
        """,
        parameters,
    ).fetchone()
    return dict(row)


def _choices(
    connection: sqlite3.Connection,
    dimension_id: str,
) -> list[dict[str, Any]]:
    expression = DIMENSIONS[dimension_id]["expression"]
    rows = connection.execute(
        f"SELECT DISTINCT {expression} AS value FROM {FROM_SQL} "
        f"ORDER BY value LIMIT 1000"
    ).fetchall()
    return [
        {
            "value": NULL_FILTER if row["value"] is None else str(row["value"]),
            "label": "(Vacío)" if row["value"] is None else str(row["value"]),
        }
        for row in rows
    ]


def _common_month_days(
    connection: sqlite3.Connection,
) -> list[tuple[int, int]]:
    rows = connection.execute(
        f"""
        SELECT DISTINCT t.anio
        FROM {FROM_SQL}
        WHERE t.anio IS NOT NULL AND t.mes IS NOT NULL AND t.dia IS NOT NULL
        """
    ).fetchall()
    if not rows:
        return []
    year_pairs = []
    for row in rows:
        pairs = connection.execute(
            f"""
            SELECT DISTINCT t.mes, t.dia
            FROM {FROM_SQL}
            WHERE t.anio = ? AND t.mes IS NOT NULL AND t.dia IS NOT NULL
            """,
            (row["anio"],),
        ).fetchall()
        year_pairs.append({(item["mes"], item["dia"]) for item in pairs})
    return sorted(set.intersection(*year_pairs)) if year_pairs else []


def _comparison_by_year(
    connection: sqlite3.Connection,
    filters: list[tuple[str, str | None]],
    month_days: list[tuple[int, int]],
) -> list[dict[str, Any]]:
    where_sql, parameters = _where_clause(filters, month_days)
    query = (
        "SELECT t.anio AS year, "
        f"{ALIASES['rows']} AS record_count, "
        f"{ALIASES['unique']} AS unique_processes, "
        f"{ALIASES['awarded']} AS awarded_cop "
        f"FROM {FROM_SQL}{where_sql} "
        "GROUP BY t.anio ORDER BY t.anio"
    )
    return [
        dict(row)
        for row in connection.execute(query, parameters).fetchall()
    ]


def _make_insight(
    connection: sqlite3.Connection,
    definition: dict[str, Any],
    filters: list[tuple[str, str | None]],
    common_month_days: list[tuple[int, int]],
    comparison_period: list[tuple[int, int]] | None,
    level_dimensions: list[str],
    level: int,
    level_count: int,
    active_filter_labels: list[str],
) -> dict[str, Any]:
    dimension_ids = list(
        dict.fromkeys(
            [
                *level_dimensions,
                *definition.get(
                    "group_dimensions", [definition["dimension"]]
                ),
            ]
        )
    )
    insight_filters = list(filters)
    periods = (
        common_month_days
        if definition.get("common_months")
        else comparison_period
    )
    if definition.get("common_months") and not common_month_days:
        groups: list[dict[str, Any]] = []
        denominator = 0
    else:
        groups = _aggregate(
            connection,
            dimension_ids,
            insight_filters,
            metric=definition["metric"],
            limit=1000,
            period_days=periods,
        )
        groups = [
            {
                "category": row["label"],
                "measure_value": (
                    row["record_count"]
                    if definition["metric"] == "rows"
                    else row["unique_processes"]
                    if definition["metric"] == "unique"
                    else row["awarded_cop"]
                ),
            }
            for row in groups
        ]
        denominator = _total(connection, insight_filters, periods)[
            "record_count"
            if definition["metric"] == "rows"
            else "unique_processes"
            if definition["metric"] == "unique"
            else "awarded_cop"
        ]

    top = groups[0] if groups else None
    value = top["measure_value"] if top else 0
    share = (value / denominator * 100) if denominator else 0
    category_value = top["category"] if top else None
    category_label = "(Vacío)" if category_value is None else str(category_value)
    unit = (
        "registros"
        if definition["metric"] == "rows"
        else "procesos únicos"
        if definition["metric"] == "unique"
        else "COP"
    )
    if definition["metric"] == "awarded":
        formatted_value = f"${int(value):,}".replace(",", ".")
        formatted_denominator = f"${int(denominator):,}".replace(",", ".")
        denominator_label = (
            f"valor adjudicado del corte filtrado: {formatted_denominator} COP"
        )
    else:
        formatted_value = f"{int(value):,}".replace(",", ".")
        formatted_denominator = f"{int(denominator):,}".replace(",", ".")
        denominator_label = (
            f"{unit} del corte filtrado: {formatted_denominator}"
        )
    measure_name = {
        "rows": "Registros (COUNT(*))",
        "unique": "Procesos únicos (COUNT(DISTINCT id_del_proceso))",
        "awarded": "Valor adjudicado (SUM en COP)",
    }[definition["metric"]]
    level_dimension = level_dimensions[-1]

    finding = (
        f"{category_label} presenta el mayor valor observado: "
        f"{formatted_value} {unit}; representa {share:.2f} % del "
        f"denominador ({denominator_label})."
        if top
        else "No hay filas para el corte seleccionado; no se calcula un hallazgo."
    )
    if definition.get("common_months"):
        finding += (
            " La comparación usa las mismas fechas mes-día observadas en "
            "todos los años: "
            + ", ".join(
                f"{month:02d}-{day:02d}" for month, day in common_month_days
            )
            + "."
            if common_month_days
            else " No hay fechas mes-día comunes para comparar años."
        )

    return {
        "title": definition["question"],
        "question": definition["question"],
        "dimensions": [
            {
                "dimension": DIMENSIONS[dimension_id]["dimension"],
                "attribute": DIMENSIONS[dimension_id]["label"],
            }
            for dimension_id in dimension_ids
        ],
        "measures": [measure_name, unit],
        "level": {
            "index": level + 1,
            "count": level_count,
            "dimension": DIMENSIONS[level_dimension]["label"],
        },
        "active_filters": active_filter_labels,
        "procedure": (
            f"{definition['procedure']} "
            f"El nivel OLAP {level + 1} ({DIMENSIONS[level_dimension]['label']}) "
            "también forma parte del agrupamiento."
        ),
        "evidence": (
            f"Consulta SQL parametrizada: agrupación por "
            f"{' y '.join(DIMENSIONS[item]['label'] for item in dimension_ids)} "
            f"y medida {unit}; "
            f"denominador explícito: {denominator_label}."
        ),
        "finding": finding,
        "interpretation": definition["interpretation"],
        "utility": definition["utility"],
        "limitation": definition["limitation"],
    }


def view_data(
    view_id: str,
    params: dict[str, str],
    database: Path = DATABASE,
) -> dict[str, Any]:
    if view_id not in VIEWS:
        raise InvalidSelection("Vista de análisis desconocida.")
    config = VIEWS[view_id]
    operation = params.get("operation", "dice")
    allowed_operations = {
        "drill-down",
        "roll-up",
        "slice",
        "dice",
        "pivot",
    }
    if operation not in allowed_operations:
        raise InvalidSelection("Operación OLAP desconocida.")
    try:
        previous_level = int(params.get("level", "0"))
    except ValueError as error:
        raise InvalidSelection("El nivel de exploración debe ser entero.") from error
    if not 0 <= previous_level < len(config["drill_path"]):
        raise InvalidSelection("Nivel de exploración fuera de rango.")
    level = previous_level
    if operation == "drill-down":
        level = min(level + 1, len(config["drill_path"]) - 1)
    elif operation == "roll-up":
        level = max(level - 1, 0)

    first_filter, second_filter = [
        item[0] for item in config["filters"]
    ]
    filter_one = params.get("filter_one") or None
    filter_two = params.get("filter_two") or None

    with _connect(database) as connection:
        filter_one = _validate_filter(connection, first_filter, filter_one)
        filter_two = _validate_filter(connection, second_filter, filter_two)
        filters = [(first_filter, filter_one), (second_filter, filter_two)]
        active_filters = (
            filters[:1]
            if operation == "slice"
            else filters
        )
        common_month_days = (
            _common_month_days(connection) if view_id == "temporal" else []
        )
        active_filter_labels = [
            f"{DIMENSIONS[dimension_id]['label']}: "
            f"{'(Vacío)' if value == NULL_FILTER else value}"
            for dimension_id, value in active_filters
            if value is not None
        ]
        if view_id == "temporal":
            active_filter_labels.append(
                "Fechas mes-día comunes: "
                + ", ".join(
                    f"{month:02d}-{day:02d}"
                    for month, day in common_month_days
                )
                if common_month_days
                else "Sin fechas mes-día comunes"
            )
        comparison_period = common_month_days if view_id == "temporal" else None
        totals = _total(connection, active_filters, comparison_period)
        all_period_totals = (
            _total(connection, active_filters)
            if view_id == "temporal"
            else totals
        )
        primary_dimension = config["drill_path"][level]
        hierarchy_dimensions = config["drill_path"][: level + 1]
        primary = _aggregate(
            connection,
            hierarchy_dimensions,
            active_filters,
            metric="rows",
            period_days=comparison_period,
        )
        secondary_dimension = config["secondary"]
        secondary = _aggregate(
            connection,
            [secondary_dimension],
            active_filters,
            metric="awarded",
            period_days=comparison_period,
        )
        matrix_row, matrix_column = config["matrix"]
        if operation == "pivot":
            matrix_row, matrix_column = matrix_column, matrix_row
        matrix_records = _aggregate(
            connection,
            [matrix_row, matrix_column],
            active_filters,
            metric="rows",
            limit=1000,
            period_days=comparison_period,
        )
        row_labels = list(dict.fromkeys(
            item["dimensions"][0]["value"] for item in matrix_records
        ))[:10]
        column_labels = list(dict.fromkeys(
            item["dimensions"][1]["value"] for item in matrix_records
        ))[:10]
        matrix_index = {
            (
                item["dimensions"][0]["value"],
                item["dimensions"][1]["value"],
            ): item
            for item in matrix_records
        }
        matrix = {
            "row_label": DIMENSIONS[matrix_row]["label"],
            "column_label": DIMENSIONS[matrix_column]["label"],
            "columns": [
                "(Vacío)" if value is None else str(value)
                for value in column_labels
            ],
            "rows": [
                {
                    "label": "(Vacío)" if row_value is None else str(row_value),
                    "cells": [
                        (
                            matrix_index.get((row_value, column_value), {})
                            .get("record_count", 0)
                        )
                        for column_value in column_labels
                    ],
                    "total": sum(
                        matrix_index.get((row_value, column_value), {})
                        .get("record_count", 0)
                        for column_value in column_labels
                    ),
                }
                for row_value in row_labels
            ],
        }
        insights = [
            _make_insight(
                connection, definition, active_filters,
                common_month_days, comparison_period,
                hierarchy_dimensions, level, len(config["drill_path"]),
                active_filter_labels,
            )
            for definition in config["insights"]
        ]
        options = {
            first_filter: _choices(connection, first_filter),
            second_filter: _choices(connection, second_filter),
        }
        load_info = connection.execute(
            """
            SELECT archivo_origen, registros_csv, registros_hecho,
                   duplicados_exactos_omitidos, cargado_en_utc
            FROM etl_carga WHERE carga_key = 1
            """
        ).fetchone()

    count_sum = sum(item["record_count"] for item in primary)
    award_sum = sum(item["awarded_cop"] for item in secondary)
    top_records = primary[0] if primary else None
    top_record_share = (
        top_records["record_count"] / totals["record_count"] * 100
        if top_records and totals["record_count"]
        else 0
    )
    primary_chart_rows = [
        {
            **item,
            "share_percent": (
                item["record_count"] / totals["record_count"] * 100
                if totals["record_count"]
                else 0
            ),
        }
        for item in primary[:12]
    ]
    secondary_chart_rows = [
        {
            **item,
            "share_percent": (
                item["awarded_cop"] / totals["awarded_cop"] * 100
                if totals["awarded_cop"]
                else 0
            ),
        }
        for item in secondary[:12]
    ]
    annual_comparison = []
    if view_id == "temporal":
        with _connect(database) as connection:
            annual_comparison = _comparison_by_year(
                connection, active_filters, common_month_days
            )
    second_chart_rows = secondary_chart_rows
    second_chart_title = (
        f"Valor adjudicado por "
        f"{DIMENSIONS[secondary_dimension]['label'].lower()}"
    )
    second_chart_unit = "COP"
    second_chart_denominator = (
        f"{award_sum} COP sumados en los grupos mostrados; "
        f"total filtrado = {totals['awarded_cop']} COP"
    )
    second_chart_metric = "awarded_cop"
    if view_id == "temporal":
        year_awarded_sum = sum(
            row["awarded_cop"] for row in annual_comparison
        )
        second_chart_rows = [
            {
                **row,
                "label": str(row["year"]),
                "share_percent": (
                    row["awarded_cop"] / year_awarded_sum * 100
                    if year_awarded_sum
                    else 0
                ),
            }
            for row in annual_comparison
        ]
        second_chart_title = (
            "Valor adjudicado anual en las mismas fechas mes-día observadas"
        )
        second_chart_unit = "COP"
        second_chart_denominator = (
            f"{year_awarded_sum} COP en los años comparables "
            f"({', '.join(f'{month:02d}-{day:02d}' for month, day in common_month_days)})."
        )

    if view_id == "temporal":
        second_chart_denominator += (
            " El corte común mes-día se aplica a los indicadores y ambos "
            "gráficos de esta vista."
        )

    return {
        "view": view_id,
        "title": config["title"],
        "question": config["question"],
        "operation": operation,
        "level": level,
        "level_count": len(config["drill_path"]),
        "hierarchy": [
            DIMENSIONS[dimension_id]["label"]
            for dimension_id in config["drill_path"]
        ],
        "active_dimension": DIMENSIONS[primary_dimension]["label"],
        "pivoted": operation == "pivot",
        "active_filters": active_filter_labels,
        "filters": [
            {
                "id": first_filter,
                "label": dict(config["filters"])[first_filter],
                "selected": filter_one,
                "options": options[first_filter],
            },
            {
                "id": second_filter,
                "label": dict(config["filters"])[second_filter],
                "selected": filter_two,
                "options": options[second_filter],
            },
        ],
        "indicators": [
            {
                "label": "Registros",
                "value": totals["record_count"],
                "unit": "filas del hecho",
                "denominator": "corte filtrado actual",
            },
            {
                "label": "Procesos únicos",
                "value": totals["unique_processes"],
                "unit": "id_del_proceso distintos",
                "denominator": "corte filtrado actual",
            },
            {
                "label": "Valor adjudicado",
                "value": totals["awarded_cop"],
                "unit": "COP",
                "denominator": "suma por filas del corte filtrado",
            },
            {
                "label": "Mayor grupo por registros",
                "value": top_record_share,
                "unit": "%",
                "denominator": (
                    f"{top_records['record_count'] if top_records else 0} / "
                    f"{totals['record_count']} filas del corte filtrado"
                ),
            },
        ],
        "charts": [
            {
                "title": f"Registros por {DIMENSIONS[primary_dimension]['label'].lower()}",
                "unit": "registros",
                "denominator": (
                    f"{count_sum} registros sumados en los grupos mostrados; "
                    f"total filtrado = {totals['record_count']}"
                ),
                "metric": "record_count",
                "rows": primary_chart_rows,
            },
            {
                "title": second_chart_title,
                "unit": second_chart_unit,
                "denominator": second_chart_denominator,
                "metric": second_chart_metric,
                "rows": second_chart_rows,
            },
        ],
        "matrix": matrix,
        "insights": insights,
        "interpretation": (
            "Los cruces describen asociaciones dentro del corte actual. "
            "No establecen causalidad ni prueban irregularidades."
        ),
        "limitation": (
            "La fuente es una muestra de 10.000 registros antes de excluir "
            "79 filas exactamente duplicadas; las categorías 'No Definido' "
            "y los registros distintos que comparten ID se conservan."
        ),
        "decision": (
            "Priorizar la revisión documental de las categorías y expedientes "
            "que presentan los mayores conteos o montos en la selección activa, "
            "sin inferir irregularidad a partir de una asociación."
        ),
        "annual_comparison": annual_comparison,
        "common_periods": [
            {"month": month, "day": day}
            for month, day in common_month_days
        ],
        "period_scope": (
            {
                "included_records": totals["record_count"],
                "all_filtered_records": all_period_totals["record_count"],
                "excluded_records": (
                    all_period_totals["record_count"] - totals["record_count"]
                ),
            }
            if view_id == "temporal"
            else None
        ),
        "source": (
            Path(load_info["archivo_origen"]).name if load_info else None
        ),
        "load": (
            {
                **dict(load_info),
                "archivo_origen": Path(load_info["archivo_origen"]).name,
            }
            if load_info
            else None
        ),
    }


def overview_data(database: Path = DATABASE) -> dict[str, Any]:
    with _connect(database) as connection:
        load_info = connection.execute(
            "SELECT * FROM etl_carga WHERE carga_key = 1"
        ).fetchone()
        date_range = connection.execute(
            """
            SELECT MIN(fecha_publicacion) AS first_date,
                   MAX(fecha_publicacion) AS last_date
            FROM dim_tiempo
            WHERE fecha_publicacion IS NOT NULL
              AND fecha_publicacion != 'Desconocido'
            """
        ).fetchone()
        record_summary = _total(connection, [])
        top_modalities = _aggregate(
            connection, ["modalidad"], [], metric="rows", limit=5
        )
        top_territories = _aggregate(
            connection, ["departamento"], [], metric="rows", limit=1
        )
        annual_rows = [
            dict(row)
            for row in connection.execute(
                f"""
                SELECT t.anio AS year,
                       {ALIASES['rows']} AS record_count,
                       {ALIASES['unique']} AS unique_processes,
                       {ALIASES['awarded']} AS awarded_cop
                FROM {FROM_SQL}
                WHERE t.anio IS NOT NULL
                GROUP BY t.anio
                ORDER BY t.anio
                """
            ).fetchall()
        ]
        monthly_rows = [
            dict(row)
            for row in connection.execute(
                f"""
                SELECT t.anio AS year, t.mes AS month,
                       {ALIASES['rows']} AS record_count
                FROM {FROM_SQL}
                WHERE t.anio IS NOT NULL AND t.mes BETWEEN 1 AND 12
                GROUP BY t.anio, t.mes
                ORDER BY t.anio, t.mes
                """
            ).fetchall()
        ]
        dimension_counts = {
            table: connection.execute(
                f"SELECT COUNT(*) FROM {table}"
            ).fetchone()[0]
            for table in (
                "dim_tiempo",
                "dim_entidad",
                "dim_territorio",
                "dim_contratacion",
                "dim_proveedor",
            )
        }
        repeated_ids = connection.execute(
            """
            SELECT COALESCE(SUM(repeticiones - 1), 0) FROM (
                SELECT id_del_proceso, COUNT(*) AS repeticiones
                FROM fact_proceso
                WHERE id_del_proceso IS NOT NULL
                GROUP BY id_del_proceso HAVING COUNT(*) > 1
            )
            """
        ).fetchone()[0]
        unknown_supplier = connection.execute(
            """
            SELECT COUNT(*) FROM fact_proceso f
            JOIN dim_proveedor p ON p.proveedor_key = f.proveedor_key
            WHERE p.nit_del_proveedor_adjudicado = 'No Definido'
            """
        ).fetchone()[0]
    if load_info is None:
        raise FileNotFoundError(
            "No hay carga de Etapa 5. Ejecuta python etl/load_star_schema.py."
        )
    record_count = record_summary["record_count"]
    source_count = load_info["registros_csv"]
    annual_record_total = sum(row["record_count"] for row in annual_rows)
    annual_awarded_total = sum(row["awarded_cop"] for row in annual_rows)
    monthly_counts = {
        (row["year"], row["month"]): row["record_count"]
        for row in monthly_rows
    }
    years = [row["year"] for row in annual_rows]
    monthly_coverage = [
        {
            "year": year,
            "months": [
                {
                    "month": month,
                    "records": monthly_counts.get((year, month), 0),
                }
                for month in range(1, 13)
            ],
        }
        for year in years
    ]

    chart_width = 760
    chart_height = 230
    chart_padding_x = 18
    chart_padding_y = 20
    maximum_monthly_records = max(
        (row["record_count"] for row in monthly_rows), default=0
    )
    chart_points = []
    for index, row in enumerate(monthly_rows):
        x = (
            chart_padding_x
            + index
            * (chart_width - 2 * chart_padding_x)
            / max(len(monthly_rows) - 1, 1)
        )
        y = (
            chart_height
            - chart_padding_y
            - (
                row["record_count"] / maximum_monthly_records
                * (chart_height - 2 * chart_padding_y)
                if maximum_monthly_records
                else 0
            )
        )
        chart_points.append(
            {
                "x": round(x, 2),
                "y": round(y, 2),
                "label": f"{row['month']:02d}/{row['year']}",
                "records": row["record_count"],
            }
        )
    line_path = " ".join(
        ("M" if index == 0 else "L") + f" {point['x']} {point['y']}"
        for index, point in enumerate(chart_points)
    )
    area_path = (
        f"{line_path} L {chart_points[-1]['x']} "
        f"{chart_height - chart_padding_y} L {chart_points[0]['x']} "
        f"{chart_height - chart_padding_y} Z"
        if chart_points
        else ""
    )

    return {
        "load": {
            **dict(load_info),
            "archivo_origen": Path(load_info["archivo_origen"]).name,
        },
        "dates": dict(date_range),
        "records": record_summary,
        "top_modality": top_modalities[0] if top_modalities else None,
        "top_modalities": [
            {
                **item,
                "share_percent": (
                    item["record_count"] / record_count * 100
                    if record_count
                    else 0
                ),
            }
            for item in top_modalities
        ],
        "top_department": top_territories[0] if top_territories else None,
        "dimensions": dimension_counts,
        "repeated_id_rows": repeated_ids,
        "supplier_nit_no_definido": unknown_supplier,
        "dashboard": {
            "supplier_unknown_percent": (
                unknown_supplier / record_count * 100 if record_count else 0
            ),
            "source_duplicate_percent": (
                load_info["duplicados_exactos_omitidos"] / source_count * 100
                if source_count
                else 0
            ),
            "distinct_process_percent": (
                record_summary["unique_processes"] / record_count * 100
                if record_count
                else 0
            ),
            "annual": [
                {
                    **row,
                    "share_percent": (
                        row["record_count"] / annual_record_total * 100
                        if annual_record_total
                        else 0
                    ),
                    "awarded_share_percent": (
                        row["awarded_cop"] / annual_awarded_total * 100
                        if annual_awarded_total
                        else 0
                    ),
                }
                for row in annual_rows
            ],
            "annual_record_total": annual_record_total,
            "annual_awarded_total": annual_awarded_total,
            "monthly_coverage": monthly_coverage,
            "monthly_chart": {
                "width": chart_width,
                "height": chart_height,
                "line_path": line_path,
                "area_path": area_path,
                "points": chart_points,
                "maximum": maximum_monthly_records,
            },
        },
    }
