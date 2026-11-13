"""Verificación de evidencias y enlaces locales; no reentrena modelos."""
import csv
import json
import math
import sys
import tempfile
import xml.etree.ElementTree as E
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from app import app
from etapa6.youtube_preparar import prepare


def main():
    checks = 0
    def check(condition, message):
        nonlocal checks
        if not condition:
            raise AssertionError(message)
        checks += 1
    folder = ROOT/'etapa6/resultados/verificados'
    sup = json.loads((folder/'supervisado.json').read_text())
    pred = list(csv.DictReader((folder/'predicciones_fuera_de_muestra.csv').open()))
    ids = [r['id_del_proceso'] for r in pred]
    check(len(ids) == len(set(ids)) == sup['filas'], 'Procesos duplicados o conteo inconsistente')
    check({r['fold'] for r in pred} == {str(i) for i in range(1,11)}, 'Faltan folds')
    for m in sup['metricas']:
        c = Counter(('tp' if r['real']=='Si' else 'fp') if r[m['nombre']+'_pred']=='Si'
                    else ('fn' if r['real']=='Si' else 'tn') for r in pred)
        check(dict(c) == m['matriz'], 'Matriz no corresponde al modelo '+m['nombre'])
        f1 = 2*c['tp']/(2*c['tp']+c['fp']+c['fn'])
        check(math.isclose(f1,m['f1']), 'F1 inconsistente')
        check(math.isclose((c['tp']+c['tn'])/len(pred),m['accuracy']), 'Accuracy inconsistente')
    clu = json.loads((folder/'clustering.json').read_text())
    assign = list(csv.DictReader((folder/'asignaciones_clustering_4000.csv').open()))
    check(len(assign) == 4000 == sum(g['n'] for g in clu['clusters']), 'Tamaño clustering')
    check(len({r['id_del_proceso'] for r in assign}) == 4000, 'Repeticiones en clustering')
    check(set(r['id_del_proceso'] for r in assign) <= set(ids), 'Muestra fuera del conjunto preparado')
    check(Counter(r['cluster'] for r in assign) == {g['id']:g['n'] for g in clu['clusters']}, 'Perfiles inconsistentes')
    check('adjudicado' not in (ROOT/'etapa6/datos/clustering_4000.tab').read_text().splitlines()[0], 'Objetivo en clustering')
    sup_flow = E.parse(ROOT/'etapa6/workflows/orange_supervisado.ows').getroot()
    links = {(l.get('source_node_id'),l.get('source_channel'),l.get('sink_node_id'),l.get('sink_channel')) for l in sup_flow.findall('./links/link')}
    check(('1','Preprocessor','5','Preprocessor') in links and ('0','Data','5','Data') in links, 'Imputación fuera de CV')
    c = app.test_client()
    for slug in ['aprendizaje-supervisado','aprendizaje-no-supervisado','comentarios-youtube']:
        page = c.get('/etapa6/'+slug)
        check(page.status_code == 200, 'Flask falla '+slug)
        import re
        for link in re.findall(r'(?:href|src)="([^"]+)"',page.text):
            if link.startswith('/'):
                check(c.get(link).status_code in {200,302}, 'Enlace roto '+link)
    for path in ['/etapa6/archivo/no-permitido.ows','/etapa6/reproducible/.env','/etapa6/reproducible/extraccion.json']:
        check(c.get(path).status_code == 404, 'Descarga fuera de lista permitida')
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        source = tmp/'fuente.csv'
        with source.open('w',newline='',encoding='utf-8') as f:
            w=csv.writer(f);w.writerow(['texto']);w.writerows([[''],['Hola mundo'],['  HOLA mundo '],['Bye'],['Texto sin revisar']])
        first=prepare(source,None,tmp/'limpio')
        check(first['conteos']['vacios']==1 and first['conteos']['duplicados']==1,'Limpieza básica')
        check(first['fecha_extraccion'] is None,'Fecha de extracción inventada')
        rows=list(csv.DictReader((tmp/'limpio/revision.csv').open()))
        rows[0].update(idioma='es',pertinente='si',tema='saludo',sentimiento='neutro')
        rows[1].update(idioma='otro',pertinente='no',motivo='idioma de prueba')
        rev=tmp/'revision.csv'
        with rev.open('w',newline='') as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
        done=prepare(source,None,tmp/'limpio',rev)
        check(done['conteos']==dict(entrada_csv=5,vacios=1,duplicados=1,descartados=1,pendientes_revision=1,retenidos=1),'Conciliación de limpieza')
    print(f'{checks} comprobaciones correctas: conteos, matrices, folds, clustering, conexiones, limpieza y enlaces Flask.')


if __name__ == '__main__':
    main()
