import requests
import pandas as pd
from pathlib import Path
import time


# ============================================================
# CONFIGURACIÓN
# ============================================================

API_URL = "https://www.datos.gov.co/resource/p6dx-8zbt.json"

RAW_OUT = Path("dataset/raw/secop_ii_raw.csv")
PROCESSED_OUT = Path("dataset/processed/secop_ii_nacional.csv")


# Variables seleccionadas para el dataset inicial
COLUMNS = [
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
]


# Cuota de registros por año.
# Total: 10.000 registros.
CUOTAS_ANUALES = {
    2020: 1667,
    2021: 1667,
    2022: 1667,
    2023: 1667,
    2024: 1666,
    2025: 1666,
}


# ============================================================
# FUNCIONES AUXILIARES
# ============================================================

def cuota_mensual(total_anual):
    """
    Distribuye la cantidad anual de registros
    entre los 12 meses del año.
    """

    base = total_anual // 12
    residuo = total_anual % 12

    cuotas = []

    for mes in range(1, 13):
        cantidad = base

        if mes <= residuo:
            cantidad += 1

        cuotas.append(cantidad)

    return cuotas


def obtener_siguiente_mes(anio, mes):
    """
    Retorna el año y mes siguiente.
    """

    if mes == 12:
        return anio + 1, 1

    return anio, mes + 1


# ============================================================
# DESCARGA DE DATOS
# ============================================================

def descargar_mes(anio, mes, cantidad):
    """
    Descarga una cantidad determinada de registros
    para un mes específico.
    """

    siguiente_anio, siguiente_mes_num = obtener_siguiente_mes(
        anio,
        mes
    )

    fecha_inicio = (
        f"{anio}-{mes:02d}-01T00:00:00.000"
    )

    fecha_fin = (
        f"{siguiente_anio}-{siguiente_mes_num:02d}"
        "-01T00:00:00.000"
    )

    params = {
        "$limit": cantidad,
        "$where": (
            f"fecha_de_publicacion_del >= '{fecha_inicio}' "
            f"AND fecha_de_publicacion_del < '{fecha_fin}'"
        ),
        "$order": "fecha_de_publicacion_del ASC"
    }

    try:

        response = requests.get(
            API_URL,
            params=params,
            timeout=120
        )

        response.raise_for_status()

        data = response.json()

        print(
            f"{anio}-{mes:02d}: "
            f"{len(data)} registros"
        )

        return data

    except requests.RequestException as error:

        print(
            f"ERROR en {anio}-{mes:02d}: {error}"
        )

        return []


# ============================================================
# CONSTRUCCIÓN DEL DATASET
# ============================================================

def descargar():

    filas = []

    print("\n========== DESCARGA SECOP II ==========\n")

    # Recorrer cada año
    for anio, total_anual in CUOTAS_ANUALES.items():

        print(
            f"\n----- AÑO {anio} "
            f"(meta: {total_anual}) -----"
        )

        cuotas = cuota_mensual(total_anual)

        # Recorrer cada mes
        for mes, cantidad in enumerate(
            cuotas,
            start=1
        ):

            datos = descargar_mes(
                anio,
                mes,
                cantidad
            )

            filas.extend(datos)

            # Pequeña pausa para no saturar la API
            time.sleep(0.3)

    # ========================================================
    # CREAR DATAFRAME CRUDO
    # ========================================================

    df_raw = pd.DataFrame(filas)

    print(
        f"\nTotal descargado: {len(df_raw)}"
    )

    # IMPORTANTE:
    # En esta Etapa 1 NO eliminamos duplicados.
    # La rúbrica solicita diagnosticar la calidad inicial,
    # por lo que se conservan para su posterior análisis.

    # Garantizar máximo 10.000 registros
    df_raw = df_raw.head(10000)

    # ========================================================
    # GUARDAR DATASET RAW
    # ========================================================

    RAW_OUT.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df_raw.to_csv(
        RAW_OUT,
        index=False,
        encoding="utf-8-sig"
    )

    # ========================================================
    # SELECCIONAR VARIABLES RELEVANTES
    # ========================================================

    columnas_disponibles = [
        columna
        for columna in COLUMNS
        if columna in df_raw.columns
    ]

    df = df_raw[
        columnas_disponibles
    ].copy()

    # ========================================================
    # GUARDAR DATASET PROCESADO
    # ========================================================

    PROCESSED_OUT.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    df.to_csv(
        PROCESSED_OUT,
        index=False,
        encoding="utf-8-sig"
    )

    # ========================================================
    # RESULTADOS
    # ========================================================

    print("\n========== RESULTADO ==========")

    print(
        f"Registros finales: {len(df)}"
    )

    print(
        f"Variables: {len(df.columns)}"
    )

    # ========================================================
    # ANÁLISIS TEMPORAL
    # ========================================================

    if "fecha_de_publicacion_del" in df.columns:

        fechas = pd.to_datetime(
            df["fecha_de_publicacion_del"],
            errors="coerce"
        )

        print(
            "\n========== REGISTROS POR AÑO =========="
        )

        print(
            fechas.dt.year
            .value_counts()
            .sort_index()
        )

        print(
            "\n========== REGISTROS POR MES =========="
        )

        print(
            fechas.dt.to_period("M")
            .value_counts()
            .sort_index()
        )

        print(
            "\n========== COBERTURA TEMPORAL =========="
        )

        print(
            "Fecha mínima:",
            fechas.min()
        )

        print(
            "Fecha máxima:",
            fechas.max()
        )

    # ========================================================
    # ARCHIVOS GENERADOS
    # ========================================================

    print("\n========== ARCHIVOS GENERADOS ==========")

    print(
        f"Dataset crudo: {RAW_OUT}"
    )

    print(
        f"Dataset procesado: {PROCESSED_OUT}"
    )


# ============================================================
# EJECUCIÓN PRINCIPAL
# ============================================================

if __name__ == "__main__":
    descargar()