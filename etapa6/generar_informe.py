"""Genera el borrador técnico desde las evidencias exportadas (requiere reportlab)."""
import json
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'etapa6/informe_tecnico_borrador.pdf'
BLUE = colors.HexColor('#12334b')
TEAL = colors.HexColor('#087e8b')
GREY = colors.HexColor('#e9eff3')
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='TitleCustom', fontName='Helvetica-Bold', fontSize=26, leading=30, textColor=BLUE, spaceAfter=15))
styles.add(ParagraphStyle(name='HeadingCustom', fontName='Helvetica-Bold', fontSize=15, leading=19, textColor=BLUE, spaceAfter=10, spaceBefore=12))
styles.add(ParagraphStyle(name='BodyCustom', fontName='Helvetica', fontSize=10, leading=14, spaceAfter=8))
styles.add(ParagraphStyle(name='SmallCustom', fontName='Helvetica', fontSize=8.2, leading=11, spaceAfter=5))
styles.add(ParagraphStyle(name='CellCustom', fontName='Helvetica', fontSize=8.1, leading=10.5))
styles.add(ParagraphStyle(name='CellHeader', fontName='Helvetica-Bold', fontSize=8.1, leading=10.5, textColor=colors.white))
story = []


def p(text, small=False):
    story.append(Paragraph(text,styles['SmallCustom' if small else 'BodyCustom']))


def h(text):
    story.append(Paragraph(text,styles['HeadingCustom']))


def table(headers, rows, widths):
    data=[[Paragraph(escape(str(x)),styles['CellHeader']) for x in headers]]
    data += [[Paragraph(escape(str(x)),styles['CellCustom']) for x in row] for row in rows]
    t=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),BLUE),('VALIGN',(0,0),(-1,-1),'TOP'),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,GREY]),('BOTTOMPADDING',(0,0),(-1,-1),8),
        ('TOPPADDING',(0,0),(-1,-1),7),('LINEBELOW',(0,-1),(-1,-1),.5,GREY)]))
    story.extend([t,Spacer(1,10)])


def page(title):
    if story:story.append(PageBreak())
    h(title)


def read(path):return json.loads((ROOT/path).read_text(encoding='utf-8'))


def footer(canvas,doc):
    canvas.saveState();canvas.setStrokeColor(TEAL);canvas.line(44,42,A4[0]-44,42)
    canvas.setFont('Helvetica',8);canvas.setFillColor(BLUE)
    canvas.drawString(44,29,'SECOP II | Conocimiento Oculto | Borrador verificable')
    canvas.drawRightString(A4[0]-44,29,str(doc.page));canvas.restoreState()


def main():
    sup=read('etapa6/resultados/verificados/supervisado.json')
    clu=read('etapa6/resultados/verificados/clustering.json')
    clean=read('etapa6/datos/youtube/limpieza.json')
    txt=read('etapa6/resultados/verificados/youtube_texto.json')
    origin=read('etapa6/datos/procedencia.json')
    run=read('etapa6/resultados/verificados/ejecucion.json')
    story.append(Spacer(1,22))
    story.append(Paragraph('Conocimiento<br/>Oculto',styles['TitleCustom']))
    p('<b>Minería de Datos | Contratación pública y gestión de recursos</b>')
    p('David Santiago Arias Ramírez · Ian Andrés Galindo Bejarano · Juan Pablo Villarraga Espitia · Edwin Estiben Leal Vargas')
    p('<b>Estado: borrador técnico con resultados reproducidos.</b> Faltan la URL publicada de Flask, el enlace de sustentación, la fecha histórica de extracción y el contraste humano de la codificación textual. No es todavía el PDF final de entrega.')
    h('Contexto y objetivo')
    p('Se estudian procesos de SECOP II para identificar asociaciones de adjudicación registrada, perfiles administrativos y económicos, y percepciones expresadas en comentarios de un video. Los hallazgos orientan revisión de calidad y preguntas de investigación; no identifican fraude verificado.')
    table(['Pregunta','Método y evidencia'],[
        ['¿Puede clasificarse adjudicado usando características del diseño?','Tres clasificadores de Orange; predicciones fuera de muestra sobre 9.792 procesos únicos.'],
        ['¿Qué perfiles de precio y participación aparecen?','K-Means sobre nueva muestra de 4.000 procesos; sensibilidad y Silhouette.'],
        ['¿Qué preocupaciones expresan los comentaristas?','35 textos depurados; Orange3-Text y codificación cualitativa asistida.']], [190,317])
    h('Procedencia y alcance')
    p('Los CSV raw y processed versionados contienen 10.000 filas. Existen 9.792 procesos distintos: se retiran 208 repeticiones con iguales predictores seleccionados y objetivo. Se conserva el CSV original. La etiqueta positiva queda en 709 procesos (7,24 %).')
    p('Las capturas de un millón de registros no pueden reproducirse con estos archivos. Los seis grupos y 173 alertas de los resúmenes históricos corresponden a otra muestra de 4.000; no se trasladan a los nuevos resultados. La fuente original usa cuotas por mes/año y primeras fechas: no es una muestra nacional aleatoria.')
    p('Fuente: dataset/processed/secop_ii_nacional.csv. SHA-256: '+origin['sha256_fuente'],True)

    page('1. Supervisado: procedimiento y evaluación')
    p('<b>Problema:</b> clasificación binaria del campo administrativo adjudicado (No/Si) en esta instantánea. No equivale al desenlace final futuro ni a fraude. Los predictores describen diseño del proceso, pero no se dispone de sus versiones exactas al publicar.')
    p('<b>Features:</b> departamento_entidad, ordenentidad, modalidad_de_contratacion, tipo_de_contrato, unidad_de_duracion, precio_base, duracion y numero_de_lotes. El ID es meta. Se excluyen fase, estado, respuestas, proveedores participantes, adjudicatario, montos adjudicados, identificadores y nombres como predictores.')
    table(['Conexión del flujo','Finalidad'],[
        ['File → Data de Test and Score','Entrada supervisado.tab con tipos y objetivo explícitos.'],
        ['Preprocess → Preprocessor de Test and Score','Media/moda ajustada solo con entrenamiento de cada fold.'],
        ['Naive Bayes, Tree, Random Forest → Learner','Comparación con las mismas particiones y datos.'],
        ['Test and Score → Confusion Matrix / ROC','Resultados fuera de muestra, errores por modelo y separación por probabilidades.']], [230,277])
    p('<b>Validación:</b> 10 folds estratificados, semilla 42. Se usa la API de Orange 3.41.0 con las mismas clases y parámetros del flujo. Seleccionar Si en Test and Score; Tree en Confusion Matrix. No se seleccionan Features mediante un Rank que observe todos los objetivos.')
    table(['Modelo','AUC','Acc.','Prec. Si','Recall Si','F1 Si','MCC'],[
        [m['nombre'],*[f'{m[k]:.3f}' for k in ['auc','accuracy','precision','recall','f1','mcc']]] for m in sup['metricas']], [105,60,60,70,72,70,70])
    table(['Modelo','Parámetros'],[
        ['Naive Bayes','Predeterminados; discretización aprendida en entrenamiento.'],
        ['Tree','Profundidad 10, mínimo 10 por hoja y 20 para dividir, mayoría suficiente 95%.'],
        ['Random Forest','10 árboles; mínimo 5 para dividir; max_features=sqrt; semilla 0.']], [105,402])
    p('Accuracy: aciertos totales. Precisión: fracción de predichos Si correctos. Recall: fracción de Si recuperados. F1: balance entre precisión y recall. AUC: discriminación por probabilidades. MCC: asociación que considera las cuatro celdas de la matriz.',True)

    page('2. Supervisado: selección, errores y límites')
    p('<b>Selección:</b> mayor F1 positivo, con desempate MCC y nombre. Tree obtiene F1 0,7904; Random Forest 0,7842. Tree facilita reglas y su máximo de profundidad limita complejidad. La pequeña diferencia no demuestra superioridad estadística. Random Forest tiene mayor AUC, pero menor F1 con la decisión predeterminada.')
    table(['Modelo','TN','FP','FN','TP'],[[m['nombre'],m['matriz']['tn'],m['matriz']['fp'],m['matriz']['fn'],m['matriz']['tp']] for m in sup['metricas']], [147,90,90,90,90])
    p('<b>Tree:</b> 174 falsos positivos y 132 falsos negativos. Los falsos positivos predicen adjudicación donde el CSV indica No; los falsos negativos omiten un Si registrado. Las matrices están identificadas por modelo y se recalculan desde predicciones_fuera_de_muestra.csv; ya no dependen de la atribución ambigua de la captura antigua.')
    p('<b>Desbalance:</b> 9.083 No y 709 Si. Predecir siempre No consigue 92,76 % de accuracy y F1 positivo cero. Por eso la exactitud total no basta. Naive Bayes recupera 631 positivos y pierde 78, a costa de 333 falsas alarmas; sería una alternativa si el costo de omitir positivos fuese mayor.')
    h('Conocimiento y decisión apoyada')
    p('Las características de diseño contienen asociaciones con el estado registrado. El modelo puede orientar una exploración académica y comparar procesos para revisar registros. No se demuestra causalidad, irregularidad ni utilidad operativa en nuevas convocatorias.')
    h('Limitaciones que siguen vigentes')
    p('La instantánea no prueba cuáles eran los valores exactos antes de la adjudicación y los No pueden incluir procesos sin desenlace final observado. Hay dependencia posible entre procesos de una misma entidad y sesgo de cuotas. La validación aleatoria no sustituye un corte temporal; la elección sobre los mismos folds de comparación necesita prueba externa.')
    p('Siguiente validación: capturar variables al publicar, seguir el desenlace, separar entrenamiento pasado y prueba futura, y revisar estabilidad por entidad y año. La mejora metodológica no puede atribuirse por separado a la eliminación de variables o repetidos: varios aspectos cambiaron a la vez.')

    page('3. Clustering: preparación y comparación')
    p('<b>Pregunta:</b> ¿qué perfiles de precio, participación registrada y diseño administrativo aparecen en la muestra? Se toman 4.000 procesos de los 9.792, con semilla 42, antes de ajustar transformaciones. Se guarda cada ID. adjudicado no figura en el archivo de clustering.')
    p('Se usan log(1+precio_base), log(1+proveedores_unicos_con), modalidad, tipo y orden de entidad. El logaritmo conserva ceros y reduce extremos. Impute aplica media/moda; Continuize estandariza las dos numéricas y codifica categorías one-hot. Los originales son metas, usadas solo para interpretar.')
    p('<b>Flujo:</b> File → Impute → Continuize → k-Means → Silhouette Plot, Data Table, Distributions y Box Plot. K-Means++: 10 reinicios, 300 iteraciones, semilla 0; normalización interna desactivada. Distancia euclidiana y Silhouette exacto en 4.000 casos.')
    table(['K','Silhouette con log1p'],[[r['k'],f"{r['score']:.4f}"] for r in clu['comparacion']], [120,387])
    p('<b>Elección:</b> K=3, Silhouette 0,6088, el mayor entre K=2..8. No se afirma que sea el óptimo universal. Sin logaritmos K=2 alcanza 0,9711, pero produce grupos de 1 y 3.999 procesos: aísla un extremo y no proporciona la segmentación buscada. Se conserva esa sensibilidad en clustering.json.')
    table(['Grupo','n','Precio mediano COP','Proveedores mediana','Silhouette'],[[g['id'],g['n'],f"{g['precio_mediano_cop']:,.0f}",g['proveedores_mediana'],f"{g['silhouette']:.3f}"] for g in clu['clusters']], [65,65,160,137,80])
    p('C1: precio mediano cero y solicitudes de información frecuentes; revisar ceros y la categoría literal No de tipo de contrato. C2: grupo mayoritario, principalmente servicios y baja participación registrada; no todos son contratación directa (modalidad más frecuente: 48,45 %). C3: mayor participación (mediana cuatro) y precio mediano 47,5 millones; mezcla modalidades y tipos.')
    p('Los perfiles sirven para comparar contextos similares y revisar calidad. Ceros no demuestran ausencia de competencia. El promedio Silhouette está influido por el grupo mayoritario. Falta evaluar estabilidad entre semillas y muestras. No se ajustó un nuevo detector de anomalías; no se reutilizan las 173 alertas antiguas.',True)

    page('4. YouTube: corpus, limpieza e interpretación')
    p('<b>Fuente recibida:</b> CSV con texto, fecha y likes, 36 comentarios. La documentación previa lo vincula a https://youtu.be/M6aisVwwkEg; el CSV no contiene video_id. La asociación debe confirmarse por el equipo. Las publicaciones abarcan 10/11/2025 a 11/10/2026; ninguna de estas fechas identifica la extracción.')
    p('<b>Metadatos no recuperados:</b> fecha histórica de consulta, total anterior al CSV, búsqueda y paginación originales. No se inventan. El extractor mejorado permite una nueva consulta documentada a commentThreads.list, part=snippet, texto plano, orden temporal, máximo 500 y nextPageToken. No incluye respuestas ni autores. La clave se obtiene del entorno o Secrets de Colab.')
    table(['Entrada CSV','Vacíos','Duplicados','Descartes','Retenidos'],[[36,0,0,1,35]], [107,90,100,100,110])
    p('Limpieza: NFKC/HTML/espacios y duplicados por texto sin mayúsculas. Se descarta manzana* por corrección aislada sin contexto. Se mantienen elogios, críticas y quejas sobre audio; se distingue recepción del video y contenido institucional. Español verificado por lectura asistida, sin traducción. Se anonimiza una mención nominal al editor; no se publican autores.')
    p('<b>Codificación:</b> un tema principal por comentario, con etiquetas y decisiones locales privadas en codificacion_asistida.csv. La realizó el asistente de IA: no es una validación humana independiente. Los temas pueden coexistir y requieren contraste del equipo.')
    table(['Tema principal','Comentarios'],list(clean['temas_revisados'].items()), [407,100])
    p('La lectura identifica preocupación por competencia simulada y lentitud del control. Son percepciones, no hechos verificados. Otros textos combinan valoración educativa y crítica a la selección política de ejemplos; las quejas sobre volumen describen la recepción del video. El corpus completo y las etiquetas individuales se conservan localmente, sin publicarse en GitHub.')
    p('Las opiniones corresponden a comentaristas de un video seleccionado; no son una encuesta de Colombia ni pueden enlazarse a contratos concretos. La selección del video y la autoselección de quienes comentan limitan la generalización.')

    page('5. Texto en Orange y conclusiones integradas')
    p('Flujo: File → Corpus → Preprocess Text; luego Word Cloud, Sentiment Analysis y Bag of Words. Se aplican minúsculas, HTML/URLs, regex de palabras, stopwords de español congeladas y unigramas. Bag of Words usa TF-IDF con L2. Topic Modelling aplica tres componentes LSI; Distances usa coseno y Hierarchical Clustering enlace promedio.')
    p('LSI: el primer componente reúne gracias, video y excelente; el segundo gobiernos, Petro, ejemplos y gracias; el tercero referencias al medio. Coinciden parcialmente con recepción y sesgo, pero no producen cinco temas equivalentes a la codificación. Los signos de LSI no indican polaridad emocional. La API fija semilla 42; la GUI no la expone y los signos/pesos pueden variar.')
    p('El corte jerárquico exploratorio de máximo tres grupos devuelve uno por empates. No se presenta como segmentación temática útil. La interpretación se sustenta en comentarios, codificación explícita y términos, no únicamente en una nube.')
    table(['Sentimiento automático','Resultado'],[['Puntuación positiva',12],['Puntuación negativa',10],['Puntuación cero',13],['Coincidencia con etiquetas asistidas comparables','11 de 23']], [325,182])
    p('Multilingual Sentiment (es) usa lexicones congelados. Cero no prueba neutralidad. El contraste excluye mixtos e inciertos y no usa patrón oro humano. La coincidencia limitada impide usar las puntuaciones como conclusión principal; ironía, vocabulario y distintos blancos de opinión requieren revisión.')
    h('Evidencia, hipótesis y decisiones')
    table(['Tipo','Conclusión'],[
        ['Respaldado','El diseño se asocia con adjudicación registrada; Tree alcanza F1 0,7904 en validación interna. La muestra admite tres perfiles bajo el tratamiento elegido. Los textos incluyen control, competencia, sesgo y recepción del video.'],
        ['Hipótesis','La mención a empresas que simulan competencia sugiere estudiar beneficiarios comunes: contar proveedores no mide independencia. Esta base y el corpus no permiten confirmarlo.'],
        ['Decisiones posibles','Revisar ceros y categorías ambiguas, comparar procesos en perfiles similares, contrastar fuentes y validar el clasificador con datos posteriores capturados al publicar.'],
        ['No sustentado','Ningún resultado prueba corrupción en procesos específicos ni representa por sí solo toda la población.']], [105,402])

    page('6. Reproducción, productos y referencias')
    p('Ejecución: Orange '+run['orange']+', scikit-learn '+run['sklearn']+', NumPy '+run['numpy']+', Orange3-Text '+txt['orange_text']+'. Python '+run['python']+'. Los hashes, particiones supervisadas, probabilidades supervisadas y asignaciones de SECOP están versionados. Para texto se publican solo resultados agregados; el corpus y sus etiquetas requieren una copia autorizada local. La API reproduce las clases y parámetros de los flujos, sin afirmar que las capturas antiguas correspondan a esta ejecución.')
    table(['Paso','Acción desde la raíz del repositorio'],[
        ['1','Crear entorno Python 3.12 e instalar requirements-orange.txt.'],
        ['2','python etapa6/preparar_datos.py; python etapa6/reproducir.py'],
        ['3','Con una copia autorizada local, repetir youtube_preparar.py con el CSV y la codificación del equipo; no se publican textos ni etiquetas individuales. Comando completo en REPRODUCIR.md.'],
        ['4','python etapa6/analizar_textos.py; python etapa6/generar_flujos.py'],
        ['5','python etapa6/verificar.py. Para Flask: instalar requirements.txt y ejecutar python app.py.']], [45,462])
    p('Para abrir Orange conservar juntos workflows y datos: File resuelve rutas relativas al .ows. Descargar solo el flujo no descarga sus entradas. analizar_textos.py instala los recursos lingüísticos congelados en las cachés locales. Flask lee resultados y no requiere Orange en el hosting.')
    h('Accesos de la entrega')
    p('<b>Repositorio:</b> <link href="https://github.com/disociando31/datamining901/tree/Entrega-orange">https://github.com/disociando31/datamining901/tree/Entrega-orange</link>')
    p('<b>Aplicación Flask publicada:</b> URL pendiente de aportar y verificar.<br/><b>Video de sustentación:</b> enlace pendiente de aportar y verificar. No se sustituyen por enlaces locales.')
    p('El documento deberá actualizarse cuando se integren los cambios en la rama de entrega. Para el video de máximo 10 minutos: contexto 1 min; comparación y errores supervisados 3 min; clustering y escala 2 min; comentarios y límites 2 min; conclusiones y productos 2 min.')
    h('Referencias')
    for label,url in [
        ('Orange: Test and Score','https://orangedatamining.com/widget-catalog/evaluate/testandscore/'),
        ('Orange: Preprocess','https://orangedatamining.com/widget-catalog/data/preprocess/'),
        ('Orange: k-Means','https://orangedatamining.com/widget-catalog/unsupervised/kmeans/'),
        ('Orange Text Mining','https://orange3-text.readthedocs.io/'),
        ('YouTube Data API: commentThreads.list','https://developers.google.com/youtube/v3/docs/commentThreads/list'),
        ('SECOP II, API de datos abiertos','https://www.datos.gov.co/resource/p6dx-8zbt.json')]:
        p(escape(label)+': <link href="'+url+'">'+url+'</link>',True)
    SimpleDocTemplate(str(OUT),pagesize=A4,rightMargin=44,leftMargin=44,topMargin=40,bottomMargin=56,
         title='Conocimiento Oculto - Informe técnico verificable (borrador)',author='Equipo Minería de Datos').build(story,onFirstPage=footer,onLaterPages=footer)
    print(OUT)


if __name__ == '__main__':main()
