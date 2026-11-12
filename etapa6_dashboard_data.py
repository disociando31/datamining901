"""Contenido académico verificable de Etapa 6. No carga datasets grandes."""
METRICAS = [
    {'nombre':'Naive Bayes','auc':0.996,'accuracy':0.987,'f1':0.946,'precision':0.910,'recall':0.985,'mcc':0.939},
    {'nombre':'Tree','auc':0.987,'accuracy':0.987,'f1':0.946,'precision':0.922,'recall':0.972,'mcc':0.939},
    {'nombre':'Random Forest','auc':0.996,'accuracy':0.987,'f1':0.947,'precision':0.922,'recall':0.972,'mcc':0.940},
]
CLUSTERS = [
    {'id':'C1','n':1141,'perfil':'Contratación directa territorial, principalmente de servicios','anomalos':2},
    {'id':'C2','n':1006,'perfil':'Contratación territorial mixta y regímenes de cuantía menor','anomalos':28},
    {'id':'C3','n':656,'perfil':'Contratación directa nacional de servicios','anomalos':0},
    {'id':'C4','n':511,'perfil':'Procesos relacionados con Decreto 092 de 2017','anomalos':6},
    {'id':'C5','n':48,'perfil':'Participación registrada elevada; perfil minoritario','anomalos':44},
    {'id':'C6','n':638,'perfil':'Contratación nacional heterogénea','anomalos':93},
]
SILHOUETTE=[{'k':2,'score':0.327},{'k':3,'score':0.353},{'k':4,'score':0.420},{'k':5,'score':0.488},{'k':6,'score':0.550}]
YOUTUBE_TERMS=[{'palabra':'video','n':10},{'palabra':'gobierno','n':9},{'palabra':'solo','n':6},{'palabra':'gracia','n':5},{'palabra':'si','n':5},{'palabra':'corrupción','n':5},{'palabra':'petro','n':4},{'palabra':'duqu','n':4},{'palabra':'bueno','n':4},{'palabra':'ejemplo','n':4},{'palabra':'control','n':3}]
FLOW_HELP = {
 'supervisado': {
 'CSV File Import':'Importación del CSV. La captura de Test & Score registra 1.000.000 de filas.',
 'Select Columns':'Separación de adjudicado como objetivo y predictores; revisar que no haya variables posteriores al resultado.',
 'Impute':'Tratamiento de valores faltantes antes de evaluar los algoritmos.',
 'Naive Bayes':'Clasificador probabilístico basado en la independencia condicional de predictores.',
 'Tree':'Árbol interpretable. En el archivo .ows: profundidad máxima 10, mínimo por hoja 10.',
 'Random Forest':'Bosque de 10 árboles en el archivo .ows; mínimo 5 para dividir nodo.',
 'Test and Score':'Validación cruzada estratificada de 10 particiones; métricas para la clase Sí.',
 'Confusion Matrix':'Errores por clase y aciertos del clasificador seleccionado; la imagen no identifica inequívocamente cuál es.',
 'ROC Analysis':'Capacidad de separar positivos y negativos para diferentes umbrales.',
 'Rank':'Ranking auxiliar de predictores. No demuestra causalidad.',
 'Tree Viewer':'Visualización de reglas del árbol entrenado.',
 'Distributions':'Distribución de clases y variables.',
 'Data Table':'Inspección de registros.',
 },
 'no_supervisado': {
 'CSV File Import':'Registros de SECOP II.',
 'Select Columns':'Cinco características del proceso; adjudicado fuera de Features.',
 'Impute':'Tratamiento de faltantes.',
 'Continuize':'One-hot en categorías y estandarización de variables numéricas.',
 'k-Means':'En el .ows adjunto: K fijo 6, KMeans++, 10 reinicios, 300 iteraciones, normalización interna desactivada.',
 'Outliers':'Isolation Forest dentro del widget Outliers; produce la etiqueta de anomalía estadística.',
 'Data Sampler':'En el .ows recibido está conectado DESPUÉS de K-Means para alimentar Silhouette Plot. No confundir con muestreo previo al entrenamiento.',
 'Silhouette Plot':'Evaluación de separación sobre datos muestreados; evitar aplicarla al millón de filas por memoria.',
 'Distributions':'Tamaño de clusters o distribución de anomalías.',
 'Box Plot':'Diferencias entre características de los perfiles.',
 'Scatter Plot':'Representación de anomalías en una proyección de dos variables.',
 'Data Table':'Consulta de procesos con sus indicadores y asignaciones.',
 },
 'youtube':{
 'CSV File Import':'Comentarios del video https://youtu.be/M6aisVwwkEg obtenidos con commentThreads.list de YouTube Data API v3; CSV con texto, fecha y likes.',
 'Corpus':'Define la columna textual para el análisis.',
 'Corpus Viewer':'Inspección de los comentarios y su calidad.',
 'Preprocess Text':'Tokenización y limpieza; requiere documentar idioma y filtros efectivos.',
 'Word Cloud':'Términos más visibles, evidencia exploratoria insuficiente por sí sola.',
 'Sentiment Analysis':'Evaluación de sentimiento. El .ows fija español; validar el método con ejemplos.',
 'Data Table':'36 comentarios analizados en la captura recibida.',
 'Distributions':'Distribución del subconjunto seleccionado.',
 'Bag of Words':'Vectorización por conteos de tokens.',
 'Topic Modelling':'Se muestran 10 temas mediante LSI en la captura. Se observa bastante ruido.',
 'Distances':'Distancias entre comentarios vectorizados.',
 'Hierarchical Clustering':'Agrupamiento jerárquico de los comentarios; captura con enlace promedio.',
 }
}
PAGINAS = {
 'conocimiento-oculto':{'titulo':'Conocimiento oculto','eyebrow':'ETAPA 06 · VISIÓN GENERAL', 'resumen':'Predicción de adjudicación, perfiles de contratación y voces de comentaristas. Tres análisis, tres tipos distintos de evidencia.', 'tipo':'inicio'},
 'aprendizaje-supervisado':{'titulo':'Aprendizaje supervisado','eyebrow':'01 · CLASIFICACIÓN', 'resumen':'¿Se puede anticipar la etiqueta adjudicado en los registros de SECOP II?', 'tipo':'supervisado','flujo':'supervisado'},
 'aprendizaje-no-supervisado':{'titulo':'Aprendizaje no supervisado','eyebrow':'02 · CLUSTERING Y ANOMALÍAS','resumen':'¿Qué perfiles de contratación se repiten y qué registros presentan comportamientos inusuales?', 'tipo':'no_supervisado','flujo':'no_supervisado'},
 'comentarios-youtube':{'titulo':'Comentarios de YouTube','eyebrow':'03 · MINERÍA DE TEXTO','resumen':'¿Qué preocupaciones, temas y reacciones expresan los comentaristas de videos relacionados con el proyecto?', 'tipo':'youtube','flujo':'youtube'},
 'conclusiones-integradas':{'titulo':'Conclusiones integradas','eyebrow':'04 · SÍNTESIS DE EVIDENCIA','resumen':'Relación entre predicción, patrones estadísticos y percepciones expresadas en comentarios.', 'tipo':'conclusiones'},
 'evidencias-y-entrega':{'titulo':'Evidencias y entrega','eyebrow':'05 · REPRODUCIBILIDAD','resumen':'Descarga de los flujos originales, resultados agregados y documentación de la entrega.', 'tipo':'evidencias'},
}
NAVEGACION = [
 ('conocimiento-oculto','Resumen'),('aprendizaje-supervisado','Supervisado'),('aprendizaje-no-supervisado','No supervisado'),('comentarios-youtube','YouTube'),('conclusiones-integradas','Conclusiones'),('evidencias-y-entrega','Archivos')
]
