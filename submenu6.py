"""Etapa 6: Conocimiento oculto. Bloques compatibles con templates/submenu.html.

Los resultados sin evidencias aún se mantienen explícitamente pendientes.
"""

SUBMENUS_ETAPA_6 = [
    {
        "slug": "conocimiento-oculto",
        "numero": "01",
        "titulo": "Conocimiento oculto: objetivos y metodología",
        "resumen": "Integración de predicción, agrupamiento y opiniones públicas sobre contratación en SECOP II.",
        "bloques": [
            {"tipo": "texto", "subtitulo": "Pregunta integradora", "contenido":
             "¿Qué patrones de contratación, perfiles atípicos y preocupaciones expresadas en comentarios de YouTube permiten priorizar revisiones de procesos registrados en SECOP II?"},
            {"tipo": "texto", "subtitulo": "Qué entendemos por conocimiento oculto", "contenido":
             "Son relaciones y comportamientos obtenidos mediante modelos y análisis de texto, más allá de los conteos y cruces descriptivos de las etapas anteriores. Las anomalías y predicciones no demuestran fraude ni corrupción."},
            {"tipo": "tabla", "subtitulo": "Tres fuentes complementarias", "encabezados": ["Componente", "Pregunta", "Producto"],
             "filas": [
                 ["Supervisado", "¿Se puede predecir adjudicado?", "Comparación de tres clasificadores"],
                 ["No supervisado", "¿Qué perfiles y anomalías se observan?", "K-Means e Isolation Forest"],
                 ["YouTube", "¿Qué temas y percepciones expresan quienes comentan?", "Procesamiento de texto"],
             ]},
        ],
    },
    {
        "slug": "aprendizaje-supervisado",
        "numero": "02",
        "titulo": "Aprendizaje supervisado",
        "resumen": "Predicción de la variable adjudicado y comparación de tres algoritmos.",
        "bloques": [
            {"tipo": "texto", "subtitulo": "Problema de clasificación", "contenido":
             "La variable objetivo es adjudicado. Se comparan tres modelos bajo una misma partición o validación cruzada, documentando características disponibles al momento de predecir para evitar fuga de información. Predecir adjudicación no equivale a predecir fraude."},
            {"tipo": "texto", "subtitulo": "Evaluación pendiente de incorporar", "contenido":
             "Agregar nombres y parámetros reales de los tres modelos, métricas Accuracy, Precision, Recall y F1, matriz de confusión, distribución de clases y justificación del modelo seleccionado, usando las salidas exportadas de Orange."},
            {"tipo": "captura", "subtitulo": "Flujo supervisado de Orange", "url": None,
             "alt": "Flujo de evaluación supervisada en Orange"},
            {"tipo": "captura", "subtitulo": "Matriz de confusión y métricas", "url": None,
             "alt": "Matriz de confusión y métricas de los modelos"},
        ],
    },
    {
        "slug": "aprendizaje-no-supervisado",
        "numero": "03",
        "titulo": "Aprendizaje no supervisado",
        "resumen": "Agrupamiento de procesos y detección exploratoria de anomalías.",
        "bloques": [
            {"tipo": "texto", "subtitulo": "Pregunta de agrupamiento", "contenido":
             "¿Qué perfiles de contratación pública se identifican por características económicas y administrativas, y cuáles presentan comportamientos estadísticamente atípicos?"},
            {"tipo": "texto", "subtitulo": "Variables y preparación", "contenido":
             "Se utilizaron precio_base, modalidad_de_contratacion, tipo_de_contrato, ordenentidad y proveedores_unicos_con. Se trataron faltantes y se codificaron categorías mediante one-hot y variables numéricas mediante estandarización. La variable adjudicado se excluyó del agrupamiento y se conservó únicamente para análisis posterior."},
            {"tipo": "tabla", "subtitulo": "Comparación inicial de K-Means (4.000 filas)",
             "encabezados": ["Número de grupos (K)", "Silhouette Score"],
             "filas": [["2", "0,327"], ["3", "0,353"], ["4", "0,420"], ["5", "0,488"], ["6", "0,550"]]},
            {"tipo": "texto", "subtitulo": "Selección del modelo", "contenido":
             "Se eligió provisionalmente K=6 por presentar el mayor Silhouette entre K=2 y K=6 en la muestra reproducible evaluada. Esta cifra no evalúa directamente una ejecución posterior sobre el conjunto completo. Los clusters son perfiles, no niveles de fraude."},
            {"tipo": "tabla", "subtitulo": "Perfiles observados en la muestra de 4.000 filas",
             "encabezados": ["Cluster", "Filas", "Caracterización preliminar"],
             "filas": [
                 ["C1", "1.141", "Contratación directa territorial de servicios"],
                 ["C2", "1.006", "Contratación territorial mixta"],
                 ["C3", "656", "Contratación directa nacional de servicios"],
                 ["C4", "511", "Procesos del tipo Decreto 092 de 2017"],
                 ["C5", "48", "Participación registrada elevada y valores extremos"],
                 ["C6", "638", "Contratación nacional heterogénea"],
             ]},
            {"tipo": "texto", "subtitulo": "Detección de anomalías (Isolation Forest)", "contenido":
             "En el experimento de 4.000 filas, el modelo señaló 173 filas como atípicas (4,33 %). La condición Outlier=Yes indica anomalía estadística y no fraude verificado. En un ajuste con el dataset completo se deben publicar sus nuevos conteos por separado."},
            {"tipo": "captura", "subtitulo": "Diagrama no supervisado de Orange", "url": '/static/etapa6/imagenes/flujo_kmeans_muestra.png',
             "alt": "Flujo K-Means e Isolation Forest"},
            {"tipo": "texto", "subtitulo": "Cómo interpretar Silhouette", "contenido":
             "El coeficiente mide cohesión y separación de los grupos: valores positivos altos sugieren mejor asignación, valores cercanos a cero indican solapamiento y valores negativos requieren revisión. La evaluación exhaustiva sobre cerca de un millón de filas agotó la memoria, por lo que se utilizó una muestra de 4.000 filas con muestreo reproducible."},
            {"tipo": "captura", "subtitulo": "Agrupamiento y calidad Silhouette", "url": '/static/etapa6/imagenes/silhouette_4000.png',
             "alt": "Visualización de evaluación Silhouette"},
            {"tipo": "captura", "subtitulo": "Distribución de clusters en la muestra (4.000 filas)", "url": "/static/etapa6/imagenes/distribucion_clusters_4000.png",
             "alt": "Frecuencia aproximada por cluster en la muestra de 4.000 filas"},
            {"tipo": "texto", "subtitulo": "Lectura de los resultados", "contenido":
             "Las tablas y las capturas de evaluación de K-Means corresponden al experimento de 4.000 filas. El Scatter Plot de Isolation Forest fue capturado en una ejecución posterior de mayor tamaño y no debe confundirse con los 173 registros atípicos de la muestra. La posición en el gráfico no demuestra fraude: indica características inusuales en variables transformadas."},
            {"tipo": "captura", "subtitulo": "Anomalías detectadas por Isolation Forest", "url": '/static/etapa6/imagenes/isolation_forest_scatter_completo.png',
             "alt": "Scatter Plot de las observaciones atípicas"},
        ],
    },
    {
        "slug": "comentarios-youtube",
        "numero": "04",
        "titulo": "Conocimiento oculto en comentarios de YouTube",
        "resumen": "Extracción mediante YouTube Data API, depuración y análisis de texto en Orange.",
        "bloques": [
            {"tipo": "texto", "subtitulo": "Pregunta de análisis", "contenido":
             "¿Qué temas, preocupaciones o percepciones expresan quienes comentan videos relacionados con la contratación pública en Colombia, y cómo se relacionan con el análisis estructurado de SECOP II?"},
            {"tipo": "texto", "subtitulo": "Extracción y transparencia", "contenido":
             "Documentar términos de búsqueda, criterios para elegir videos, enlaces, fechas de extracción, total de comentarios obtenidos y restricciones de la API. Nunca publicar la clave de acceso ni datos personales innecesarios."},
            {"tipo": "texto", "subtitulo": "Procesamiento de texto y resultados pendientes", "contenido":
             "Incluir limpieza de comentarios, tratamiento del idioma, widget de procesamiento de texto, temas o agrupaciones identificadas y ejemplos anonimizados que sustenten los hallazgos. Los comentarios no representan necesariamente a toda la población colombiana."},
            {"tipo": "captura", "subtitulo": "Flujo de análisis de texto en Orange", "url": None,
             "alt": "Flujo del análisis de comentarios"},
        ],
    },
    {
        "slug": "conclusiones-integradas",
        "numero": "05",
        "titulo": "Conclusiones integradas",
        "resumen": "Convergencias, diferencias, decisiones posibles y limitaciones de las tres fuentes de análisis.",
        "bloques": [
            {"tipo": "texto", "subtitulo": "Integración de evidencias", "contenido":
             "Esta sección relacionará las métricas reales del modelo supervisado, los seis perfiles y anomalías del no supervisado, y los temas observados en comentarios de YouTube. La interpretación final queda pendiente hasta contar con evidencia de los tres análisis."},
            {"tipo": "tabla", "subtitulo": "Cómo se complementan las técnicas", "encabezados": ["Técnica", "Qué aporta", "Qué no permite afirmar"],
             "filas": [
                 ["Clasificación", "Predicción de adjudicado", "Existencia de fraude"],
                 ["K-Means", "Perfiles de procesos similares", "Que un cluster sea sospechoso"],
                 ["Isolation Forest", "Observaciones estadísticas inusuales", "Que una anomalía sea delito"],
                 ["Comentarios de YouTube", "Temas y percepciones de comentaristas", "Opinión de toda la población"],
             ]},
        ],
    },
    {
        "slug": "evidencias-y-entrega",
        "numero": "06",
        "titulo": "Evidencias, informe y sustentación",
        "resumen": "Acceso a flujos de Orange, fuentes reproducibles, informe técnico y video.",
        "bloques": [
            {"tipo": "texto", "subtitulo": "Entrega técnica", "contenido":
             "El informe PDF debe describir el procedimiento reproducible paso a paso e incluir el enlace al repositorio, la URL de Flask publicada y el enlace al video de máximo 10 minutos. El PDF es obligatorio aunque la aplicación explique todos los análisis."},
            {"tipo": "enlaces", "subtitulo": "Productos", "lista": [
                {"texto": "Repositorio público del proyecto", "url": "https://github.com/disociando31/datamining901"},
                {"texto": "URL pública de Flask (pendiente)", "url": None},
                {"texto": "Informe parcial de aprendizaje no supervisado (PDF)", "url": "/static/etapa6/documentos/informe_parcial_no_supervisado.pdf"},
                {"texto": "Informe técnico final integrado (pendiente)", "url": None},
                {"texto": "Video de sustentación (pendiente)", "url": None},
            ]},
        ],
    },
]
