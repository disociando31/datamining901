"""Genera entradas portables de Orange; no ajusta imputadores ni modelos.

Ejecutar desde cualquier directorio: python etapa6/preparar_datos.py
"""
import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
import random
import math

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'dataset/processed/secop_ii_nacional.csv'
OUT = ROOT / 'etapa6/datos'
SEED = 42
NUMERIC = ['precio_base', 'duracion', 'numero_de_lotes']
CATEGORICAL = ['departamento_entidad', 'ordenentidad',
               'modalidad_de_contratacion', 'tipo_de_contrato', 'unidad_de_duracion']
FEATURES = CATEGORICAL + NUMERIC
CLUSTER_FEATURES = ['precio_base', 'proveedores_unicos_con',
                    'modalidad_de_contratacion', 'tipo_de_contrato', 'ordenentidad']
CLUSTER_MODEL_FEATURES = ['log_precio_base', 'log_proveedores_unicos_con',
                          'modalidad_de_contratacion', 'tipo_de_contrato', 'ordenentidad']
MISSING = {'', 'no definido', 'no especificado', 'no aplica', 'nan', 'none'}


def write_tab(path, rows, features, target=None, extra_metas=()):
    """Formato nativo de tres cabeceras: tipos y roles sin inferencia del CSV."""
    cols = features + ([target] if target else []) + ['id_del_proceso'] + list(extra_metas)
    numeric = set(NUMERIC + ['proveedores_unicos_con', 'log_precio_base', 'log_proveedores_unicos_con'])
    with path.open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(cols)
        w.writerow(['continuous' if c in numeric else ('string' if c == 'id_del_proceso'
                    else ('No Si' if c == target else 'discrete')) for c in cols])
        w.writerow(['class' if c == target else ('meta' if c == 'id_del_proceso' or c in extra_metas else '') for c in cols])
        for row in rows:
            w.writerow([row[c] for c in cols])


def main():
    OUT.mkdir(exist_ok=True)
    rows = list(csv.DictReader(SOURCE.open(encoding='utf-8-sig', newline='')))
    groups = defaultdict(list)
    for row in rows:
        groups[row['id_del_proceso']].append(row)
    # Un único registro por proceso. Las filas repetidas con diferencias en
    # predictores/objetivo se excluyen completas: no existe fecha de actualización.
    keys = FEATURES + CLUSTER_FEATURES + ['adjudicado']
    kept, ambiguous = [], []
    for pid, group in groups.items():
        if not pid or len({tuple(r[k] for k in keys) for r in group}) > 1:
            ambiguous.extend(group)
        else:
            kept.append(dict(group[0]))
    unknown = [r for r in kept if r['adjudicado'] not in {'No', 'Si'}]
    kept = [r for r in kept if r['adjudicado'] in {'No', 'Si'}]
    missing = Counter()
    for row in kept:
        for key in set(FEATURES + CLUSTER_FEATURES):
            v = row[key].strip()
            if v.lower() in MISSING:
                row[key] = '?'
                missing[key] += 1
            else:
                if key in NUMERIC + ['proveedores_unicos_con']:
                    float(v)  # Rechaza tipos inesperados en vez de cambiarlos silenciosamente.
                row[key] = v
    write_tab(OUT / 'supervisado.tab', kept, FEATURES, 'adjudicado')
    # Muestreo ANTES de imputación, escalamiento, K-Means y Silhouette.
    indices = sorted(random.Random(SEED).sample(range(len(kept)), min(4000, len(kept))))
    sample = [kept[i] for i in indices]
    for row in sample:
        for key in ['precio_base', 'proveedores_unicos_con']:
            row['log_' + key] = '?' if row[key] == '?' else str(math.log1p(float(row[key])))
    write_tab(OUT / 'clustering_4000.tab', sample, CLUSTER_MODEL_FEATURES,
              extra_metas=['precio_base', 'proveedores_unicos_con'])
    with (OUT / 'muestra_clustering_ids.csv').open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f); w.writerow(['id_del_proceso'])
        w.writerows([[r['id_del_proceso']] for r in sample])
    metadata = {
        'fuente': str(SOURCE.relative_to(ROOT)),
        'sha256_fuente': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        'filas_fuente': len(rows), 'procesos_distintos': len(groups),
        'filas_excluidas_por_ambiguedad': len(ambiguous),
        'procesos_excluidos_por_ambiguedad': len({r['id_del_proceso'] for r in ambiguous}),
        'filas_repetidas_con_mismos_predictores_retiradas': len(rows) - len(ambiguous) - len(kept) - len(unknown),
        'procesos_sin_objetivo_valido': len(unknown),
        'filas_supervisado': len(kept), 'distribucion_objetivo': dict(Counter(r['adjudicado'] for r in kept)),
        'predictores_supervisado': FEATURES, 'faltantes_por_predictor': dict(missing),
        'filas_clustering': len(sample), 'semilla_muestra': SEED,
        'predictores_clustering': CLUSTER_MODEL_FEATURES,
        'transformacion_clustering': 'log1p de precio_base y proveedores_unicos_con; conserva originales como metas para interpretar.',
        'alcance': 'Nueva ejecución sobre el CSV versionado; no reproduce la captura histórica del millón ni los antiguos 4.000 casos.',
        'limitacion_temporal': 'Instantánea retrospectiva. Se excluyen campos posteriores al trámite; no hay versiones de los campos al publicar ni seguimiento final para comprobar adjudicación futura.',
        'sesgo_muestra_fuente': 'construir_dataset.py toma cuotas anuales/mensuales y ordena por fecha ascendente; no es una muestra aleatoria nacional.',
    }
    metadata['archivos'] = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                           for p in sorted(OUT.iterdir()) if p.suffix in {'.tab', '.csv'}}
    (OUT / 'procedencia.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(metadata, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
