import pandas as pd
from pathlib import Path

DATASET = Path("dataset/processed/secop_ii_nacional.csv")
OUT = Path("dataset/metadata/diagnostico_calidad.csv")


def diagnosticar():

    df = pd.read_csv(DATASET, low_memory=False)

    print("\n========== DIMENSIONES ==========")
    print(f"Registros: {df.shape[0]}")
    print(f"Variables: {df.shape[1]}")

    print("\n========== DUPLICADOS ==========")
    print(f"Duplicados exactos: {df.duplicated().sum()}")

    if "id_del_proceso" in df.columns:
        print(
            f"Duplicados por id_del_proceso: "
            f"{df.duplicated('id_del_proceso').sum()}"
        )

    print("\n========== VALORES FALTANTES ==========")

    faltantes = pd.DataFrame({
        "variable": df.columns,
        "faltantes": df.isna().sum().values,
        "porcentaje_faltantes": (
            df.isna().mean().values * 100
        ).round(2)
    })

    faltantes = faltantes.sort_values(
        "faltantes",
        ascending=False
    )

    print(faltantes.to_string(index=False))

    print("\n========== TIPOS DE DATOS ==========")
    print(df.dtypes)

    print("\n========== COBERTURA TEMPORAL ==========")

    if "fecha_de_publicacion_del" in df.columns:
        fechas = pd.to_datetime(
            df["fecha_de_publicacion_del"],
            errors="coerce"
        )

        print("Fecha mínima:", fechas.min())
        print("Fecha máxima:", fechas.max())

    print("\n========== COBERTURA GEOGRÁFICA ==========")

    for columna in [
        "departamento_entidad",
        "ciudad_entidad"
    ]:
        if columna in df.columns:
            print(
                f"\n{columna}: "
                f"{df[columna].nunique(dropna=True)} "
                f"valores únicos"
            )

    OUT.parent.mkdir(parents=True, exist_ok=True)

    faltantes.to_csv(
        OUT,
        index=False,
        encoding="utf-8-sig"
    )

    print(f"\nReporte guardado en: {OUT}")


if __name__ == "__main__":
    diagnosticar()