"""Evaluación real con la API de Orange (sin simular widgets ni métricas).

python etapa6/preparar_datos.py
python etapa6/reproducir.py
"""
import csv
import hashlib
import json
import platform
from pathlib import Path
from datetime import datetime, timezone

import numpy as np
import Orange
import sklearn
from Orange.classification import NaiveBayesLearner, TreeLearner, RandomForestLearner
from Orange.clustering import KMeans
from Orange.data import Table, Domain
from Orange.evaluation import CrossValidation
from Orange.preprocess import Impute, Continuize, Normalize
from sklearn.metrics import (accuracy_score, precision_score, recall_score, f1_score,
                             roc_auc_score, matthews_corrcoef, confusion_matrix,
                             silhouette_score, silhouette_samples)

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'etapa6/resultados/verificados'


def dump(name, value):
    (OUT / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def supervised():
    data = Table(str(ROOT / 'etapa6/datos/supervisado.tab'))
    learners = [NaiveBayesLearner(),
                TreeLearner(max_depth=10, min_samples_leaf=10, min_samples_split=20, sufficient_majority=.95),
                RandomForestLearner(n_estimators=10, min_samples_split=5,
                                    max_features='sqrt', random_state=0)]
    names = ['Naive Bayes', 'Tree', 'Random Forest']
    # Orange llama al preprocesador SOLO con data[train_i] en cada fold.
    result = CrossValidation(k=10, stratified=True, random_state=42, store_data=True)(
        data, learners, preprocessor=Impute())
    if any(result.failed):
        raise RuntimeError(str(result.failed))
    positive = data.domain.class_var.values.index('Si')
    y = (result.actual == positive).astype(int)
    metrics = []
    predictions = []
    for i, name in enumerate(names):
        pred = (result.predicted[i] == positive).astype(int)
        prob = result.probabilities[i, :, positive]
        tn, fp, fn, tp = confusion_matrix(y, pred, labels=[0, 1]).ravel()
        metrics.append(dict(nombre=name, n=len(y), auc=float(roc_auc_score(y, prob)),
            accuracy=float(accuracy_score(y, pred)), precision=float(precision_score(y, pred, zero_division=0)),
            recall=float(recall_score(y, pred)), f1=float(f1_score(y, pred)),
            mcc=float(matthews_corrcoef(y, pred)),
            matriz={'tn': int(tn), 'fp': int(fp), 'fn': int(fn), 'tp': int(tp)}))
    # Selección explícita: F1 clase Si; desempate MCC, luego nombre.
    best = sorted(metrics, key=lambda m: (-m['f1'], -m['mcc'], m['nombre']))[0]
    folds = np.empty(len(y), dtype=int)
    for fold, sl in enumerate(result.folds):
        folds[sl] = fold + 1
    with (OUT / 'predicciones_fuera_de_muestra.csv').open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f)
        w.writerow(['id_del_proceso', 'fold', 'real', *[n + '_pred' for n in names], *[n + '_prob_Si' for n in names]])
        for j, row_index in enumerate(result.row_indices):
            w.writerow([str(data[row_index]['id_del_proceso']), folds[j], 'Si' if y[j] else 'No',
                        *['Si' if result.predicted[i, j] == positive else 'No' for i in range(3)],
                        *[float(result.probabilities[i, j, positive]) for i in range(3)]])
    dump('supervisado.json', {'filas': len(y), 'positivos': int(y.sum()), 'clase_positiva': 'Si',
         'folds': 10, 'semilla_folds': 42, 'imputacion': 'Media/moda aprendida dentro de cada partición de entrenamiento',
         'modelo_seleccionado': best['nombre'], 'criterio': 'Mayor F1 de Si; desempate MCC y nombre',
         'baseline_accuracy_siempre_No': float((y == 0).mean()), 'metricas': metrics,
         'limitacion': 'Validación interna retrospectiva; selección sobre los mismos folds no equivale a prueba externa ni demuestra predicción futura.'})
    return best


def clustering():
    original = Table(str(ROOT / 'etapa6/datos/clustering_4000.tab'))
    raw = original.transform(Domain([original.domain[c] for c in [
        'precio_base', 'proveedores_unicos_con', 'modalidad_de_contratacion', 'tipo_de_contrato', 'ordenentidad']]))
    raw = Continuize(multinomial_treatment=Continuize.Indicators)(Normalize()(Impute()(raw)))
    raw_comparison = []
    for k in range(2, 9):
        labels = KMeans(n_clusters=k, n_init=10, max_iter=300, random_state=0, preprocessors=[])(raw)
        raw_comparison.append({'k': k, 'score': float(silhouette_score(raw.X, labels)),
                               'tamanos': sorted(np.bincount(labels).tolist())})
    # Estandarizar las dos numéricas; dejar indicadores categóricos en 0/1.
    imputed = Impute()(original)
    normalized = Normalize(norm_type=Normalize.NormalizeBySD)(imputed)
    data = Continuize(multinomial_treatment=Continuize.Indicators)(normalized)
    comparison, fitted = [], {}
    for k in range(2, 9):
        model = KMeans(n_clusters=k, init='k-means++', n_init=10, max_iter=300,
                       random_state=0, preprocessors=[]).get_model(data)
        labels = model.labels
        score = float(silhouette_score(data.X, labels))
        comparison.append({'k': k, 'score': score})
        fitted[k] = labels
        print('K', k, 'Silhouette', round(score, 6), flush=True)
    best = max(comparison, key=lambda r: (r['score'], -r['k']))
    labels = fitted[best['k']]
    silhouettes = silhouette_samples(data.X, labels)
    profiles = []
    for group in range(best['k']):
        mask = labels == group
        sub = imputed[mask]
        modes = {}
        for name in ['modalidad_de_contratacion', 'tipo_de_contrato', 'ordenentidad']:
            var = sub.domain[name]
            counts = np.bincount(sub.get_column(name).astype(int), minlength=len(var.values))
            modes[name] = {'valor': var.values[int(counts.argmax())], 'porcentaje': float(counts.max()/mask.sum()*100)}
        profiles.append({'id': f'C{group+1}', 'n': int(mask.sum()), 'silhouette': float(silhouettes[mask].mean()),
             'perfil': ' · '.join(modes[c]['valor'] for c in ['modalidad_de_contratacion', 'tipo_de_contrato', 'ordenentidad']),
             'modas': modes, 'precio_mediano_cop': float(np.median(sub.get_column('precio_base'))),
             'proveedores_mediana': float(np.median(sub.get_column('proveedores_unicos_con'))),
             'proveedores_media': float(np.mean(sub.get_column('proveedores_unicos_con')))})
    with (OUT / 'asignaciones_clustering_4000.csv').open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f); w.writerow(['id_del_proceso', 'cluster', 'silhouette'])
        w.writerows([str(original[i]['id_del_proceso']), f'C{int(labels[i])+1}', float(silhouettes[i])]
                    for i in range(len(original)))
    dump('clustering.json', {'filas': len(original), 'k': best['k'], 'silhouette': best['score'],
         'comparacion': comparison, 'sensibilidad_sin_log': raw_comparison,
         'clusters': profiles, 'semilla_kmeans': 0,
         'parametros': {'init': 'k-means++', 'n_init': 10, 'max_iter': 300},
         'preparacion': 'log1p de precio y proveedores; media/moda; z-score solo numéricas; one-hot completo de categorías; distancia euclidiana',
         'evaluacion': 'Silhouette euclidiano exacto sobre los 4.000 casos. adjudicado no está en el archivo.',
         'limitacion': 'K óptimo solo entre 2 y 8; sensible a extremos, escala y peso de categorías. No demuestra riesgo o fraude.'})


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    best = supervised()
    print('Modelo seleccionado:', best['nombre'], 'F1:', best['f1'], flush=True)
    clustering()
    dump('ejecucion.json', {'fecha_ejecucion_utc': datetime.now(timezone.utc).isoformat(),
         'python': platform.python_version(), 'orange': Orange.__version__, 'sklearn': sklearn.__version__,
         'numpy': np.__version__, 'metodo': 'API de Orange; mismas clases y parámetros que los flujos corregidos',
         'sha256_entradas': {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                            for p in sorted((ROOT/'etapa6/datos').glob('*.tab'))},
         'sha256_codigo': {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                            for p in [Path(__file__), ROOT/'etapa6/preparar_datos.py']}})


if __name__ == '__main__':
    main()
