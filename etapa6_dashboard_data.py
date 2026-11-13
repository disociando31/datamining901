"""Presentación de resultados exportados; Flask no importa Orange ni entrena modelos."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGINAS = {
    'aprendizaje-supervisado': {'titulo': 'Aprendizaje supervisado', 'eyebrow': '01 · CLASIFICACIÓN', 'resumen': 'Comparación reproducible de tres modelos sobre procesos únicos del CSV versionado.', 'tipo': 'supervisado', 'flujo': 'supervisado'},
    'aprendizaje-no-supervisado': {'titulo': 'Aprendizaje no supervisado', 'eyebrow': '02 · CLUSTERING', 'resumen': 'Agrupamiento sobre una nueva muestra identificable de 4.000 procesos.', 'tipo': 'no_supervisado', 'flujo': 'no_supervisado'},
    'comentarios-youtube': {'titulo': 'Conocimiento oculto en YouTube', 'eyebrow': '03 · MINERÍA DE TEXTO', 'resumen': 'Extracción, limpieza y contraste de opiniones con los datos de SECOP II.', 'tipo': 'youtube', 'flujo': 'youtube'},
}
NAVEGACION = [('aprendizaje-supervisado', 'Supervisado'), ('aprendizaje-no-supervisado', 'No supervisado'), ('comentarios-youtube', 'Comentarios YouTube')]


def datos_dashboard():
    def read(path):
        return json.loads((ROOT/path).read_text(encoding='utf-8'))
    supervised = read('etapa6/resultados/verificados/supervisado.json')
    cluster = read('etapa6/resultados/verificados/clustering.json')
    selected = next(m for m in supervised['metricas'] if m['nombre'] == supervised['modelo_seleccionado'])
    path = ROOT/'etapa6/datos/youtube/limpieza.json'
    youtube = json.loads(path.read_text(encoding='utf-8')) if path.exists() else None
    return dict(supervisado=supervised, agrupamiento=cluster, seleccionado=selected,
                procedencia=read('etapa6/datos/procedencia.json'), youtube=youtube,
                texto_youtube=read('etapa6/resultados/verificados/youtube_texto.json'),
                ejecucion=read('etapa6/resultados/verificados/ejecucion.json'))
