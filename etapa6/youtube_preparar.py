"""Limpieza con conteos y revisión humana; nunca inventa fecha ni sentimiento.

python etapa6/youtube_preparar.py --csv ruta.csv --metadata extraccion.json
Completar revision.csv; repetir añadiendo --revision ruta/revision.csv.
idioma: es/otro/incierto; pertinente: si/no; tema: texto libre;
sentimiento: positivo/neutro/negativo/mixto/incierto; motivo: texto libre.
"""
import argparse
import csv
import hashlib
import html
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def normalized(text):
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', html.unescape(text))).strip()


def anonymous(text):
    text = re.sub(r'díganle a [A-ZÁÉÍÓÚÑ][a-záéíóúñ]+ [A-ZÁÉÍÓÚÑ][a-záéíóúñ]+', 'díganle al editor', text)
    text = re.sub(r'https?://\S+', '[enlace]', text)
    text = re.sub(r'[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}', '[correo]', text)
    text = re.sub(r'(?<!\w)@[\w.-]+', '[mención]', text)
    return re.sub(r'(?<!\w)(?:\+?\d[\s().-]*){7,}(?!\w)', '[número]', text)


def prepare(source, metadata_path, output, review_path=None):
    metadata = json.loads(metadata_path.read_text(encoding='utf-8')) if metadata_path else {}
    original_hash = hashlib.sha256(source.read_bytes()).hexdigest()
    if metadata.get('sha256_csv_original') and metadata['sha256_csv_original'] != original_hash:
        raise ValueError('El CSV no corresponde al hash de la extracción.')
    rows = list(csv.DictReader(source.open(encoding='utf-8-sig', newline='')))
    if metadata.get('comentarios_extraidos') is not None and metadata['comentarios_extraidos'] != len(rows):
        raise ValueError('La cantidad declarada difiere del CSV.')
    reviews = {}
    if review_path:
        for r in csv.DictReader(review_path.open(encoding='utf-8-sig', newline='')):
            if r['id'] in reviews:
                raise ValueError('ID repetido en la revisión.')
            reviews[r['id']] = r
    counts = Counter(entrada_csv=len(rows), vacios=0, duplicados=0, descartados=0,
                     pendientes_revision=0, retenidos=0)
    seen, review_rows, clean, valid_ids = set(), [], [], set()
    for row in rows:
        text = normalized(row.get('texto', ''))
        ident = hashlib.sha256(text.casefold().encode()).hexdigest()[:24]
        if not text:
            counts['vacios'] += 1; continue
        if text.casefold() in seen:
            counts['duplicados'] += 1; continue
        seen.add(text.casefold()); valid_ids.add(ident)
        r = reviews.get(ident, {})
        item = {'id': ident, 'texto': anonymous(text), 'video_id': row.get('video_id', metadata.get('video_id', '')),
                'idioma': r.get('idioma', ''), 'pertinente': r.get('pertinente', ''),
                'tema': r.get('tema', ''), 'sentimiento': r.get('sentimiento', ''), 'motivo': r.get('motivo', '')}
        review_rows.append(item)
        if item['idioma'] in {'otro', 'incierto'} or item['pertinente'] == 'no':
            if not item['motivo'].strip():
                raise ValueError('Todo descarte manual necesita motivo.')
            counts['descartados'] += 1
        elif (item['idioma'] == 'es' and item['pertinente'] == 'si' and item['tema'].strip()
              and item['sentimiento'] in {'positivo', 'neutro', 'negativo', 'mixto', 'incierto'}):
            counts['retenidos'] += 1; clean.append(item)
        else:
            counts['pendientes_revision'] += 1
    if set(reviews)-valid_ids:
        raise ValueError('La revisión contiene IDs ajenos a este CSV.')
    output.mkdir(parents=True, exist_ok=True)
    fields = ['id', 'texto', 'video_id', 'idioma', 'pertinente', 'tema', 'sentimiento', 'motivo']
    for name, records in [('revision.csv', review_rows), ('comentarios_limpios.csv', clean)]:
        with (output/name).open('w', encoding='utf-8', newline='') as f:
            w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(records)
    with (output/'comentarios_limpios.tab').open('w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(['texto']); w.writerow(['string']); w.writerow(['meta'])
        w.writerows([[r['texto']] for r in clean])
    assert sum(counts[k] for k in ['vacios', 'duplicados', 'descartados', 'pendientes_revision', 'retenidos']) == len(rows)
    summary = {'estado': 'revision_cualitativa_asistida' if not counts['pendientes_revision'] else 'pendiente_revision',
               'conteos': dict(counts), 'extraccion': metadata, 'sha256_csv_original': original_hash,
               'fecha_extraccion': metadata.get('fecha_extraccion_utc'),
               'autor_revision': 'Asistente de IA; codificación cualitativa explícita, requiere contraste por el equipo',
               'validacion_humana_independiente': False,
               'reglas': 'NFKC/HTML/espacios; duplicados por texto casefold; codificación cualitativa explícita de idioma, pertinencia, tema y sentimiento.',
               'temas_revisados': dict(Counter(r['tema'] for r in clean)),
               'sentimientos_revisados': dict(Counter(r['sentimiento'] for r in clean)),
               'advertencia': 'La etiqueta manual no valida el widget automático. Contrastar sus puntuaciones con las etiquetas antes de interpretarlo. Revisar nombres propios antes de publicar.'}
    (output/'limpieza.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--csv', required=True, type=Path)
    parser.add_argument('--metadata', type=Path)
    parser.add_argument('--revision', type=Path)
    parser.add_argument('--salida', type=Path, default=ROOT/'etapa6/datos/youtube/privado')
    args = parser.parse_args()
    summary = prepare(args.csv, args.metadata, args.salida, args.revision)
    # Solo conteos agregados en el área pública, nunca textos o etiquetas por persona.
    (ROOT/'etapa6/datos/youtube/limpieza.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
