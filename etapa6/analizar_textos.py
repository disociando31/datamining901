"""Análisis textual con Orange3-Text y recursos congelados en el repositorio."""
import csv
import hashlib
import json
import shutil
from collections import Counter
from pathlib import Path

import numpy as np
from Orange.misc.environ import data_dir, data_dir_base
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import squareform
from Orange.distance import Cosine

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT/'etapa6/recursos'
OUT = ROOT/'etapa6/resultados/verificados'


def preparar_recursos():
    # Orange usa estos nombres para Multilingual Sentiment (es). Se evita
    # depender de versiones remotas cambiantes del diccionario en cada equipo.
    sentiment = Path(data_dir(versioned=False))/'sentiment'
    sentiment.mkdir(parents=True, exist_ok=True)
    for name in ['positive_words_es.txt', 'negative_words_es.txt']:
        shutil.copyfile(RES/name, sentiment/name)
    stop = Path(data_dir_base())/'Orange/nltk_data/corpora/stopwords'
    stop.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(RES/'stopwords_es.txt', stop/'spanish')


def main():
    preparar_recursos()
    import orangecontrib.text
    from orangecontrib.text import Corpus
    from orangecontrib.text.preprocess import (LowercaseTransformer, HtmlTransformer,
        UrlRemover, RegexpTokenizer, StopwordsFilter, NGrams)
    from orangecontrib.text.vectorization import BowVectorizer
    from orangecontrib.text.topics import LsiWrapper
    from orangecontrib.text.sentiment import MultiSentiment
    corpus = Corpus.from_file(str(ROOT/'etapa6/datos/youtube/privado/comentarios_limpios.tab'))
    corpus.attributes['language'] = 'es'
    for pp in [LowercaseTransformer(), HtmlTransformer(), UrlRemover(), RegexpTokenizer(),
               StopwordsFilter(language=None, path=str(RES/'stopwords_es.txt')), NGrams((1, 1))]:
        corpus = pp(corpus)
    frequencies = Counter(t for doc in corpus.ngrams for t in doc)
    bow = BowVectorizer(norm=BowVectorizer.L2, wglobal=BowVectorizer.IDF).transform(corpus)
    # LSI usa SVD aleatorizada; semilla de NumPy para esta ejecución de API.
    # La interfaz de Orange no expone esa semilla: signos/pesos pueden variar.
    np.random.seed(42)
    lsi = LsiWrapper(num_topics=3, random_seed=42)
    lsi.fit_transform(bow)
    topics = []
    for i in range(3):
        words, weights = lsi.get_top_words_by_id(i, 10)
        topics.append({'componente': i+1, 'terminos': [{'termino': w, 'peso': float(v)} for w, v in zip(words, weights)]})
    distances = Cosine(bow)
    tree = linkage(squareform(np.asarray(distances), checks=False), method='average')
    labels = fcluster(tree, 3, criterion='maxclust')
    scored = MultiSentiment(language='es').transform(corpus)
    values = scored.get_column('sentiment')
    records = list(csv.DictReader((ROOT/'etapa6/datos/youtube/privado/comentarios_limpios.csv').open(encoding='utf-8')))
    with (ROOT/'etapa6/datos/youtube/privado/youtube_resultados_por_comentario.csv').open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f); w.writerow(['id', 'cluster_jerarquico', 'sentimiento_orange', 'signo_orange', 'tema_asistido', 'sentimiento_asistido'])
        for r, label, score in zip(records, labels, values):
            w.writerow([r['id'], int(label), float(score), 'positivo' if score>0 else 'negativo' if score<0 else 'cero', r['tema'], r['sentimiento']])
    # Contraste exploratorio con etiquetas asistidas, no patrón oro humano.
    comparable = [(float(s), r['sentimiento']) for s, r in zip(values, records)
                  if r['sentimiento'] in {'positivo','negativo','neutro'}]
    agree = sum(('positivo' if s>0 else 'negativo' if s<0 else 'neutro') == label for s,label in comparable)
    summary = {'filas': len(corpus), 'orange_text': orangecontrib.text.__version__,
        'preprocesamiento': 'Minúsculas, HTML/URLs, regex \\w+, stopwords NLTK español congeladas, unigramas; sin stemming ni traducción.',
        'vectorizacion': 'Count con IDF y normalización L2 (TF-IDF).',
        'terminos': [{'termino': w, 'frecuencia': n} for w,n in frequencies.most_common(20)],
        'lsi': topics, 'semilla_lsi_api': 42,
        'nota_lsi': 'Los componentes no son temas verificados; sus signos pueden invertirse. La GUI no expone la semilla de SVD.',
        'jerarquico': {'distancia': 'Coseno sobre TF-IDF normalizado L2', 'enlace': 'average',
                      'corte_exploratorio': 3, 'tamanos': dict(Counter(str(x) for x in labels)),
                      'limitacion': 'Corte exploratorio sin optimizar; corpus pequeño y vocabulario escaso en comentarios cortos.'},
        'sentimiento': {'metodo': 'Multilingual Sentiment, español, diccionarios congelados',
                       'puntuacion': 'Balance de palabras positivas/negativas del lexicón; cero no significa neutralidad verificada.',
                       'positivos': int((values>0).sum()), 'negativos': int((values<0).sum()), 'cero': int((values==0).sum()),
                       'comparables_asistidos': len(comparable), 'coincidencias_signo': int(agree),
                       'limite_validacion': 'Contraste con etiquetas asistidas por IA; excluye mixtos e inciertos. No es accuracy humana ni validación independiente.'},
        'sha256_recursos': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(RES.glob('*.txt'))},
        'sha256_corpus': hashlib.sha256((ROOT/'etapa6/datos/youtube/privado/comentarios_limpios.tab').read_bytes()).hexdigest()}
    (OUT/'youtube_texto.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
