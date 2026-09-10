import pandas as pd
import numpy as np

# 1. Cargar el dataset
df = pd.read_csv('dataset/raw/secop_ii_raw.csv') # Reemplaza con el nombre de tu archivo consolidado

print("--- ESTADÍSTICOS DESCRIPTIVOS ---")
# Variables numéricas clave
num_cols = ['precio_base', 'valor_total_adjudicacion', 'proveedores_invitados', 'proveedores_unicos_con', 'duracion']
desc = df[num_cols].describe().T
print(desc[['min', 'max', 'mean', 'std']])
print("\n")

print("--- VALORES ATÍPICOS (IQR) ---")
# Cálculo de atípicos para valor de adjudicación
Q1 = df['valor_total_adjudicacion'].quantile(0.25)
Q3 = df['valor_total_adjudicacion'].quantile(0.75)
IQR = Q3 - Q1
limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

atipicos = df[(df['valor_total_adjudicacion'] < limite_inferior) | (df['valor_total_adjudicacion'] > limite_superior)]
print(f"Registros atípicos en 'valor_total_adjudicacion': {len(atipicos)} ({(len(atipicos)/len(df))*100:.2f}%)")
print("\n")

print("--- INCONSISTENCIAS Y REGLAS DE NEGOCIO ---")
# Proveedores únicos mayores a invitados
inconsistentes_prov = df[df['proveedores_unicos_con'] > df['proveedores_invitados']]
print(f"Inconsistencia (Proveedores únicos > invitados): {len(inconsistentes_prov)} registros afectados")

# Valor adjudicado en cero (si el precio base era mayor a cero)
adjudicado_cero = df[(df['valor_total_adjudicacion'] == 0) & (df['precio_base'] > 0)]
print(f"Inconsistencia (Adjudicado en $0 pero con precio base > $0): {len(adjudicado_cero)} registros afectados")
print("\n")

print("--- REVISIÓN DE FORMATOS (Entidad) ---")
# Cuántas entidades únicas hay originalmente vs si las pasamos a minúsculas y quitamos espacios
entidades_originales = df['entidad'].nunique()
entidades_limpias = df['entidad'].str.lower().str.strip().nunique()
diferencia = entidades_originales - entidades_limpias
print(f"Entidades únicas originales: {entidades_originales}")
print(f"Entidades únicas tras normalizar texto: {entidades_limpias}")
print(f"Registros que presentan inconsistencias de formato (mayúsculas/espacios): {diferencia} variaciones detectadas")