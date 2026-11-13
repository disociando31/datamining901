"""Construye flujos Orange portables y su diagrama web desde la misma definición."""
import ast
import base64
import json
import pickle
from pathlib import Path
import xml.etree.ElementTree as E

from orangewidget.utils.filedialogs import RecentPath

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / 'etapa6/workflows'


def make_flow(filename, title, nodes, links):
    root = E.Element('scheme', version='2.0', title=title, description='Entradas relativas al directorio del flujo. Consultar etapa6/REPRODUCIR.md.')
    ns, ls, ps = E.SubElement(root, 'nodes'), E.SubElement(root, 'links'), E.SubElement(root, 'node_properties')
    diagram = {'nodes': [], 'edges': []}
    for i, (name, qualified, x, y, settings) in enumerate(nodes):
        E.SubElement(ns, 'node', id=str(i), name=name, qualified_name=qualified,
                     project_name='Orange3', version='', title=name, position=str((x, y)))
        prop = E.SubElement(ps, 'properties', node_id=str(i))
        if 'active_path' in settings:
            prop.set('format', 'pickle')
            prop.text = base64.b64encode(pickle.dumps(settings, protocol=4)).decode('ascii')
        else:
            prop.set('format', 'literal'); prop.text = repr(settings)
        diagram['nodes'].append({'id': str(i), 'name': name, 'x': x, 'y': y})
    for i, (a, output, b, input_) in enumerate(links):
        E.SubElement(ls, 'link', id=str(i), source_node_id=str(a), sink_node_id=str(b),
                     source_channel=output, sink_channel=input_, enabled='true')
        diagram['edges'].append({'source': str(a), 'target': str(b), 'sourcePort': output, 'targetPort': input_})
    E.SubElement(root, 'annotations'); E.SubElement(root, 'thumbnail')
    E.indent(root)
    E.ElementTree(root).write(WORK / filename, encoding='utf-8', xml_declaration=True)
    return diagram


def file_node(relative, x=0, y=160):
    # abspath deliberately nonexistent: resolution MUST use the workflow basedir.
    recent = RecentPath('__ruta_portable__', 'basedir', relative)
    return ('File', 'Orange.widgets.data.owfile.OWFile', x, y,
            {'active_path': recent, 'source': 0, '__version__': 2})


def node(name, qualified, x, y, **settings):
    return name, qualified, x, y, settings


def main():
    k = json.loads((ROOT/'etapa6/resultados/verificados/clustering.json').read_text())['k']
    flow = {}
    nodes = [file_node('../datos/supervisado.tab'),
        node('Preprocess', 'Orange.widgets.data.owpreprocess.OWPreprocess', 190, 0,
             storedsettings={'name': '', 'preprocessors': [('orange.preprocess.impute', {'method': 2})]}),
        node('Naive Bayes', 'Orange.widgets.model.ownaivebayes.OWNaiveBayes', 210, 100),
        node('Tree', 'Orange.widgets.model.owtree.OWTreeLearner', 210, 230,
             limit_depth=True, max_depth=10, limit_min_leaf=True, min_leaf=10,
             limit_min_internal=True, min_internal=20, limit_majority=True, sufficient_majority=95),
        node('Random Forest', 'Orange.widgets.model.owrandomforest.OWRandomForest', 210, 360,
             n_estimators=10, use_min_samples_split=True, min_samples_split=5,
             use_random_state=True, use_max_depth=False, use_max_features=False),
        node('Test and Score', 'Orange.widgets.evaluate.owtestandscore.OWTestAndScore', 460, 160,
             n_folds=3, cv_stratified=True, resampling=0),
        node('Confusion Matrix', 'Orange.widgets.evaluate.owconfusionmatrix.OWConfusionMatrix', 700, 80,
             selected_learner=[1]),
        node('ROC Analysis', 'Orange.widgets.evaluate.owrocanalysis.OWROCAnalysis', 700, 230),
        node('Data Table', 'Orange.widgets.data.owtable.OWTable', 0, 360)]
    links = [(0, 'Data', 5, 'Data'), (1, 'Preprocessor', 5, 'Preprocessor'),
             (2, 'Learner', 5, 'Learner'), (3, 'Learner', 5, 'Learner'),
             (4, 'Learner', 5, 'Learner'), (5, 'Evaluation Results', 6, 'Evaluation Results'),
             (5, 'Evaluation Results', 7, 'Evaluation Results'), (0, 'Data', 8, 'Data')]
    flow['supervisado'] = make_flow('orange_supervisado.ows', 'SECOP · clasificación verificada', nodes, links)
    nodes = [file_node('../datos/clustering_4000.tab'),
        node('Impute', 'Orange.widgets.data.owimpute.OWImpute', 190, 160, _default_method_index=2),
        node('Continuize', 'Orange.widgets.data.owcontinuize.OWContinuize', 380, 160,
             cont_var_hints={'': 1}, disc_var_hints={'': 1}, __version__=3),
        node('k-Means', 'Orange.widgets.unsupervised.owkmeans.OWKMeans', 580, 160,
             k=k, k_from=2, k_to=8, optimize_k=False, normalize=False, n_init=10,
             max_iterations=300, smart_init=0, __version__=2),
        node('Silhouette Plot', 'Orange.widgets.visualize.owsilhouetteplot.OWSilhouettePlot', 800, 0),
        node('Data Table', 'Orange.widgets.data.owtable.OWTable', 800, 160),
        node('Distributions', 'Orange.widgets.visualize.owdistributions.OWDistributions', 800, 300),
        node('Box Plot', 'Orange.widgets.visualize.owboxplot.OWBoxPlot', 580, 360)]
    links = [(0, 'Data', 1, 'Data'), (1, 'Data', 2, 'Data'), (2, 'Data', 3, 'Data'),
             (3, 'Data', 4, 'Data'), (3, 'Data', 5, 'Data'), (3, 'Data', 6, 'Data'), (3, 'Data', 7, 'Data')]
    flow['no_supervisado'] = make_flow('orange_no_supervisado.ows', 'SECOP · muestra nueva de 4.000', nodes, links)
    # La entrada apunta al corpus real depurado; ningún comentario se genera como ejemplo.
    old = E.parse(WORK/'orange_youtube.ows').getroot()
    props = {p.get('node_id'): ast.literal_eval(p.text) for p in old.findall('./node_properties/properties')
             if p.get('format') == 'literal'}
    nodes = []
    for n in old.findall('./nodes/node'):
        i = int(n.get('id'))
        x, y = ast.literal_eval(n.get('position'))
        if i == 1:
            nodes.append(file_node('../datos/youtube/privado/comentarios_limpios.tab', x, y))
        else:
            settings = props.get(str(i), {})
            settings.pop('savedWidgetGeometry', None)
            settings.pop('__session_state_data', None)
            if i == 0:
                settings = {'recent_files': [], 'language': 'es'}
            if i == 3:
                settings = {'storedsettings': {'name': '', 'preprocessors': [
                    ('preprocess.transform', {'methods': [0, 2, 3]}),
                    ('preprocess.tokenize', {}),
                    ('preprocess.filter', {'methods': [0], 'language': 'es'}),
                    ('preprocess.ngrams', {'start': 1, 'end': 1})]}, '__version__': 4}
            if i == 8:
                settings = {'wlocal': 'Count', 'wglobal': 'IDF', 'normalization': 'L2 (Euclidean)'}
            if i == 10:
                settings = {'axis': 0, 'metric_id': 4, '__version__': 4}
            if i == 9:
                settings.update(lsi={'num_topics': 3}, method_index=0)
            nodes.append((n.get('name'), n.get('qualified_name'), x, y, settings))
    links = [(int(l.get('source_node_id')), l.get('source_channel'),
              int(l.get('sink_node_id')), l.get('sink_channel')) for l in old.findall('./links/link')]
    links = [(5, 'Corpus', 7, 'Data') if a == 6 and b == 7 else (a, o, b, i) for a, o, b, i in links]
    flow['youtube'] = make_flow('orange_youtube.ows', 'YouTube · corpus revisado de 35 comentarios', nodes, links)
    (ROOT/'static/etapa6/flows.json').write_text(json.dumps(flow, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')


if __name__ == '__main__':
    main()
