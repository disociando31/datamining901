# -*- coding: utf-8 -*-

# Submenús de la Etapa 2 — Calidad de Datos
# Proyecto: Contratación pública y Ejecución de recursos
# Dataset base: SECOP II (10.000 registros, 34 variables), consolidado en la Etapa 1.
# Los indicadores numéricos de perfilamiento (registros, variables, duplicados,
# valores faltantes, tipos de dato y cobertura temporal/geográfica) provienen de
# la salida real del script diagnostico_calidad.py. Los apartados marcados como
# "pendiente de validación" corresponden a chequeos que deben ejecutarse con el
# script extendido antes de la entrega final del informe técnico.

SUBMENUS_ETAPA_2 = [
    {
        "slug": "objetivo-de-la-etapa",
        "numero": "01",
        "titulo": "Objetivo de la etapa",
        "resumen": "Propósito del perfilamiento, diagnóstico, medición y tratamiento de calidad de datos.",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Objetivo general",
                "contenido": (
                    "Aplicar los conceptos fundamentales de calidad de datos "
                    "mediante el perfilamiento, diagnóstico, medición y tratamiento "
                    "del conjunto de datos de contratación pública seleccionado en "
                    "la Etapa 1 (SECOP II, 10.000 registros, 34 variables), "
                    "identificando los problemas que puedan afectar su uso para "
                    "responder a la pregunta de investigación del proyecto. Los "
                    "resultados de este proceso se integran en la sección "
                    "'Calidad de Datos' de la aplicación web desarrollada en "
                    "Flask, se publican en el repositorio de GitHub del proyecto "
                    "y se despliegan en el servicio web público del equipo."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Objetivos específicos",
                "contenido": (
                    "1. Perfilar el conjunto de datos consolidado, describiendo su "
                    "estructura, tipos de dato, valores únicos, valores nulos, "
                    "duplicados y estadísticos descriptivos.\n"
                    "2. Evaluar seis dimensiones de calidad de datos (completitud, "
                    "exactitud, consistencia, unicidad, validez y actualidad) "
                    "mediante métricas cuantificables.\n"
                    "3. Elaborar un inventario de problemas de calidad con su "
                    "impacto, causa probable y evidencia.\n"
                    "4. Diseñar y justificar un plan de tratamiento sobre los "
                    "problemas identificados.\n"
                    "5. Documentar e implementar los resultados en la aplicación "
                    "Flask del proyecto, gestionando el desarrollo mediante una "
                    "rama específica en GitHub."
                ),
            },
        ],
    },
    {
        "slug": "descripcion-proposito-datos",
        "numero": "02",
        "titulo": "Descripción y propósito de los datos",
        "resumen": "Fuente, variables principales, volumen de registros y uso esperado del conjunto de datos.",
        "bloques": [
            {
                "tipo": "texto",
 "subtitulo": "Fuente de los datos",
                "contenido": (
                    "Contratos.gov.co: plataforma que permite consultar procesos "
                    "de contratación registrados por entidades públicas en Colombia.\n\n"
                    
                    "Datos Abiertos de Compras Públicas de Ecuador: plataforma "
                    "que proporciona información sobre procesos y contrataciones "
                    "realizadas por entidades públicas de Ecuador.\n\n"
                    
                    "SECOP II - Procesos de Contratación: conjunto de datos del "
                    "portal de Datos Abiertos de Colombia que contiene información "
                    "sobre procesos de contratación pública, entidades, proveedores, "
                    "valores y modalidades de contratación.\n\n"
                    
                    "Datos Abiertos Bogotá: plataforma que ofrece información "
                    "pública relacionada con la ejecución y seguimiento de recursos "
                    "y procesos de las entidades del Distrito de Bogotá.\n\n"
                    
                    "Open Contracting Data Registry: repositorio que proporciona "
                    "datos de contratación pública bajo estándares de datos abiertos, "
                    "facilitando la consulta y análisis de información contractual.\n\n"
                    
                    "Estas fuentes permiten complementar la información sobre "
                    "procesos, entidades, proveedores, valores, modalidades y "
                    "ejecución contractual, proporcionando una base para el "
                    "análisis y la construcción de variables de riesgo."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Variables principales",
                "contenido": (
                    "El dataset contiene 34 variables, entre las cuales las "
                    "principales son: identificación y trazabilidad del proceso\n\n "

                    "('id_del_proceso', 'referencia_del_proceso', 'urlproceso', "
                    "'codigo_entidad');\n\n"

                    " ubicación de la entidad y del proveedor\n\n "

                    "('departamento_entidad', 'ciudad_entidad', "
                    "'departamento_proveedor', 'ciudad_proveedor'); \n\n"

                    "caracterización del proceso\n\n"

                    " ('modalidad_de_contratacion', "
                    "'tipo_de_contrato', 'subtipo_de_contrato', "
                    "'codigo_principal_de_categoria', 'fase', "
                    "'estado_del_procedimiento', 'adjudicado');\n\n"

                    "variables económicas\n\n"

                    "('precio_base', 'valor_total_adjudicacion'); "
                    "variables temporales ('fecha_de_publicacion_del', "
                    "'fecha_adjudicacion', 'duracion', 'unidad_de_duracion');\n\n "

                    "variables de competencia entre proveedores \n\n"

                    "('proveedores_invitados', 'proveedores_con_invitacion', "
                    "'respuestas_al_procedimiento', "
                    "'conteo_de_respuestas_a_ofertas', "
                    "'proveedores_unicos_con');\n\n"

                    " información del adjudicador y proveedor\n\n"

                    " ('nombre_del_adjudicador', "
                    "'nit_del_proveedor_adjudicado'); y variables relacionadas "
                    "con la justificación de la contratación "
                    "('justificacion_en_modalidad_de')."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Resumen del volumen de datos",
                "encabezados": ["Indicador", "Valor"],
                "filas": [
                    ["Cantidad de registros", "10.000"],
                    ["Cantidad de variables", "34"],
                    ["Variables numéricas (int64)", "10"],
                    ["Variables de texto / categóricas (str)", "24"],
                    ["Periodo cubierto", "2020-01-01 a 2025-12-01"],
                    ["Departamentos representados", "34 valores únicos"],
                    ["Ciudades representadas", "494 valores únicos"],
                ],
            },
            {
                "tipo": "texto",
                "subtitulo": "Uso esperado de la información",
                "contenido": (
                    "El conjunto de datos, una vez depurado y validado, se "
                    "utilizará para identificar patrones y factores de riesgo en "
                    "la contratación pública colombiana: concentración de "
                    "proveedores, uso atípico de modalidades de contratación, "
                    "anomalías en tiempos y valores adjudicados, y relaciones "
                    "entidad-adjudicador-proveedor. Por tratarse de insumo para "
                    "técnicas de minería de datos (clustering, detección de "
                    "anomalías, reglas de asociación y series de tiempo), el "
                    "conjunto requiere un alto nivel de completitud, unicidad y "
                    "consistencia, ya que los errores de calidad en esta etapa se "
                    "propagan directamente a los resultados analíticos "
                    "posteriores."
                ),
            },
        ],
    },
    {
        "slug": "requisitos-de-calidad",
        "numero": "03",
        "titulo": "Requisitos de calidad",
        "resumen": "Condiciones mínimas que deben cumplir los datos frente al problema y sus usuarios.",
        "bloques": [
            {
                "tipo": "tabla",
                "subtitulo": "Requisitos de calidad definidos para el proyecto",
                "encabezados": ["Requisito", "Justificación frente al uso esperado", "Dimensión asociada"],
                "filas": [
                    ["Cada proceso debe tener un identificador único y verificable ('id_del_proceso')", "Es la llave primaria para unir el dataset con el proceso original en SECOP y con las variables derivadas de riesgo", "Unicidad"],
                    ["Las variables económicas ('precio_base', 'valor_total_adjudicacion') deben ser numéricas y mayores o iguales a cero", "Los ratios de sobrecosto y las agregaciones por sector/departamento requieren valores numéricos válidos", "Validez"],
                    ["Las variables de fecha deben poder interpretarse como fecha calendario válida", "El cálculo de días entre publicación y adjudicación depende de operaciones aritméticas sobre fechas", "Validez / Exactitud"],
                    ["Las variables categóricas clave (departamento, modalidad, estado) deben tener catálogos cerrados y consistentes", "Los agregados por departamento y por modalidad exigen categorías comparables entre registros", "Consistencia"],
                    ["El nivel de valores nulos en variables críticas para el análisis de riesgo debe ser mínimo", "Variables como 'proveedores_invitados' o 'valor_total_adjudicacion' son insumo directo de los indicadores derivados definidos en la Etapa 1", "Completitud"],
                    ["Los datos deben corresponder al periodo de análisis definido (2020-2025)", "Evita mezclar periodos con baja adopción de SECOP II (previos a 2020) que introducirían sesgo de subregistro", "Actualidad"],
                    ["Los valores de proveedores y montos deben ser coherentes entre sí (p. ej. proveedores_unicos_con ≤ proveedores_invitados)", "Sustenta el cálculo del indicador derivado 'ratio_competencia_real' definido en la Etapa 1", "Consistencia"],
                ],
            },
        ],
    },
    {
        "slug": "perfilamiento-de-los-datos",
        "numero": "04",
        "titulo": "Perfilamiento de los datos",
        "resumen": "Descripción cuantitativa de la estructura, tipos, valores únicos, nulos, duplicados y estadísticos del dataset.",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Código utilizado",
                "contenido": (
                    "El perfilamiento se realizó con el script 'diagnostico_calidad.py' "
                    "del repositorio del proyecto, apoyado en la librería pandas "
                    "(lectura del CSV consolidado, 'df.shape' para dimensiones, "
                    "'df.dtypes' para tipos de dato, 'df.isnull().sum()' para "
                    "valores faltantes, 'df.duplicated()' y "
                    "'df.duplicated(subset=[\"id_del_proceso\"])' para duplicados, "
                    "'df[col].nunique()' para valores únicos y 'df[col].describe()' "
                    "para estadísticos de variables numéricas)."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Dimensiones del conjunto de datos",
                "encabezados": ["Indicador", "Resultado"],
                "filas": [
                    ["Registros (filas)", "10.000"],
                    ["Variables (columnas)", "34"],
                    ["Duplicados exactos (todas las columnas)", "79 (0,79 %)"],
                    ["Duplicados por 'id_del_proceso'", "208 (2,08 %)"],
                ],
            },
            {
                "tipo": "tabla",
                "subtitulo": "Tipos de dato por variable (según pandas dtype)",
                "encabezados": ["Variable", "Tipo actual (dtype)", "Tipo esperado", "Observación"],
                "filas": [
                    ["entidad", "str", "Categórica", "Correcto"],
                    ["nit_entidad", "str", "Identificador (texto)", "Correcto"],
                    ["departamento_entidad", "str", "Categórica", "Correcto"],
                    ["ciudad_entidad", "str", "Categórica", "Correcto"],
                    ["ordenentidad", "str", "Categórica", "Correcto"],
                    ["id_del_proceso", "str", "Identificador (texto)", "Correcto"],
                    ["referencia_del_proceso", "str", "Identificador (texto)", "Correcto"],
                    ["nombre_del_procedimiento", "str", "Texto", "Presenta valores faltantes (ver completitud)"],
                    ["descripci_n_del_procedimiento", "str", "Texto libre", "Correcto (no se usa como variable numérica)"],
                    ["fase", "str", "Categórica", "Correcto"],
                    ["fecha_de_publicacion_del", "str", "Fecha (datetime)", "Inconsistente: almacenada como texto, requiere conversión a fecha"],
                    ["precio_base", "int64", "Numérica", "Correcto"],
                    ["modalidad_de_contratacion", "str", "Categórica", "Correcto"],
                    ["duracion", "int64", "Numérica", "Correcto"],
                    ["unidad_de_duracion", "str", "Categórica", "Correcto"],
                    ["ciudad_de_la_unidad_de", "str", "Categórica", "Correcto"],
                    ["proveedores_invitados", "int64", "Numérica", "Correcto"],
                    ["proveedores_con_invitacion", "int64", "Numérica", "Correcto"],
                    ["respuestas_al_procedimiento", "int64", "Numérica", "Correcto"],
                    ["conteo_de_respuestas_a_ofertas", "int64", "Numérica", "Correcto"],
                    ["proveedores_unicos_con", "int64", "Numérica", "Correcto"],
                    ["numero_de_lotes", "int64", "Numérica", "Correcto"],
                    ["estado_del_procedimiento", "str", "Categórica", "Correcto"],
                    ["adjudicado", "str", "Categórica (Sí/No)", "Correcto"],
                    ["departamento_proveedor", "str", "Categórica", "Correcto"],
                    ["ciudad_proveedor", "str", "Categórica", "Correcto"],
                    ["valor_total_adjudicacion", "int64", "Numérica", "Correcto"],
                    ["nombre_del_proveedor", "str", "Texto", "Correcto"],
                    ["nit_del_proveedor_adjudicado", "str", "Identificador (texto)", "Correcto"],
                    ["codigo_principal_de_categoria", "str", "Categórica (UNSPSC)", "Correcto"],
                    ["tipo_de_contrato", "str", "Categórica", "Correcto"],
                    ["subtipo_de_contrato", "str", "Categórica", "Correcto"],
                    ["urlproceso", "str", "URL", "Correcto"],
                    ["codigo_entidad", "int64", "Identificador", "Almacenado como numérico; se recomienda tratarlo como texto/categórico para evitar operaciones aritméticas indebidas"],
                ],
            },
            {
                "tipo": "tabla",
                "subtitulo": "Valores faltantes por variable (variables con al menos un valor nulo)",
                "encabezados": ["Variable", "Faltantes", "% faltantes"],
                "filas": [
                    ["nombre_del_procedimiento", "2", "0,02 %"],
                ],
            },
            {
                "tipo": "texto",
                "subtitulo": "Valores faltantes en el resto de variables",
                "contenido": (
                    "Las 33 variables restantes ('entidad', 'nit_entidad', "
                    "'departamento_entidad', 'ordenentidad', 'ciudad_entidad', "
                    "'id_del_proceso', 'referencia_del_proceso', "
                    "'descripci_n_del_procedimiento', 'fase', "
                    "'fecha_de_publicacion_del', 'precio_base', "
                    "'modalidad_de_contratacion', 'duracion', "
                    "'unidad_de_duracion', 'ciudad_de_la_unidad_de', "
                    "'proveedores_invitados', 'proveedores_con_invitacion', "
                    "'respuestas_al_procedimiento', 'conteo_de_respuestas_a_ofertas', "
                    "'proveedores_unicos_con', 'numero_de_lotes', "
                    "'estado_del_procedimiento', 'adjudicado', "
                    "'departamento_proveedor', 'ciudad_proveedor', "
                    "'valor_total_adjudicacion', 'nombre_del_proveedor', "
                    "'nit_del_proveedor_adjudicado', 'codigo_principal_de_categoria', "
                    "'tipo_de_contrato', 'subtipo_de_contrato', 'urlproceso' y "
                    "'codigo_entidad') presentan 0 valores faltantes (0,00 %) "
                    "según la salida del script de diagnóstico."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Valores únicos en variables categóricas clave",
                "encabezados": ["Variable", "Valores únicos"],
                "filas": [
                    ["departamento_entidad", "34"],
                    ["ciudad_entidad", "494"],
                ],
            },
            {
                "tipo": "texto",
                "subtitulo": "Cobertura temporal",
                "contenido": (
                    "La variable 'fecha_de_publicacion_del' cubre el rango del "
                    "2020-01-01 al 2025-12-01, lo que coincide con el periodo de "
                    "análisis definido en la Etapa 1 (2020-2025) y confirma que no "
                    "existen registros anteriores a la ventana de estudio "
                    "establecida."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Código utilizado para los estadísticos descriptivos y las reglas de negocio",
                "contenido": (
                    "Se amplió el script 'diagnostico_calidad.py' con las "
                    "instrucciones 'df[num_cols].describe().T' sobre las "
                    "variables numéricas clave, el cálculo del rango "
                    "intercuartílico (IQR) para 'valor_total_adjudicacion', la "
                    "verificación de las reglas de negocio "
                    "'proveedores_unicos_con > proveedores_invitados' y "
                    "'valor_total_adjudicacion == 0 con precio_base > 0', y la "
                    "comparación de 'entidad' original contra su versión "
                    "normalizada ('str.lower().str.strip()')."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Estadísticos descriptivos de las variables numéricas clave",
                "encabezados": ["Variable", "Mínimo", "Máximo", "Promedio", "Desviación estándar"],
                "filas": [
                    ["precio_base", "0", "599.971.300.000", "307.915.900", "6.422.738.000"],
                    ["valor_total_adjudicacion", "0", "25.811.130.000", "29.881.330", "430.848.200"],
                    ["proveedores_invitados", "0", "8.456", "21,04", "226,43"],
                    ["proveedores_unicos_con", "0", "93", "0,55", "3,36"],
                    ["duracion", "0", "1.826", "61,49", "98,37"],
                ],
            },
            {
                "tipo": "texto",
                "subtitulo": "Interpretación de los estadísticos descriptivos",
                "contenido": (
                    "La desviación estándar de 'precio_base' y "
                    "'valor_total_adjudicacion' es varias veces mayor que su "
                    "propio promedio, lo cual es característico de "
                    "distribuciones con alta asimetría y presencia de valores "
                    "extremos (unos pocos contratos de gran magnitud frente a "
                    "una mayoría de procesos de bajo valor), coherente con la "
                    "estructura habitual del gasto público. De igual forma, el "
                    "valor máximo de 'proveedores_invitados' (8.456) frente a "
                    "un promedio de 21,04 confirma la existencia de procesos "
                    "atípicos en cuanto a número de invitados, y el mínimo de 0 "
                    "en 'duracion' sugiere procesos con fechas de inicio y fin "
                    "iguales o registradas de forma incompleta, lo cual debe "
                    "revisarse junto con la corrección del tipo de dato de las "
                    "variables de fecha."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Valores atípicos (método IQR) e inconsistencias de reglas de negocio",
                "encabezados": ["Chequeo", "Resultado", "Registros afectados"],
                "filas": [
                    ["Valores atípicos en 'valor_total_adjudicacion' (IQR)", "Registros fuera del rango [Q1 − 1,5·IQR, Q3 + 1,5·IQR]", "873 (8,73 %)"],
                    ["'proveedores_unicos_con' > 'proveedores_invitados'", "Incumplimiento de la regla lógica proveedores_unicos_con ≤ proveedores_invitados", "764 (7,64 %)"],
                    ["'valor_total_adjudicacion' = 0 con 'precio_base' > 0", "Registros con precio base definido pero sin valor adjudicado registrado", "8.804 (88,04 %)"],
                    ["Inconsistencia de formato en 'entidad'", "Comparación entre valores únicos originales (2.082) y valores únicos tras normalizar texto (2.082)", "0 (0,00 %) — no se detectaron variaciones de formato"],
                ],
            },
            {
                "tipo": "texto",
                "subtitulo": "Nota sobre la regla 'valor adjudicado en cero'",
                "contenido": (
                    "El 88,04 % de registros con 'valor_total_adjudicacion' en "
                    "cero y 'precio_base' mayor a cero es, en principio, un "
                    "porcentaje demasiado alto para tratarse únicamente de un "
                    "error de captura; una hipótesis más probable es que gran "
                    "parte de estos procesos aún no han sido adjudicados al "
                    "momento de la descarga (procesos en curso), y por tanto un "
                    "valor de cero sería el comportamiento esperado, no una "
                    "inconsistencia. Antes de tratarlos como error, se "
                    "recomienda refinar la regla cruzándola con las variables "
                    "'adjudicado' y 'estado_del_procedimiento', de forma que "
                    "solo se marquen como inconsistentes los registros donde "
                    "'adjudicado' = 'Sí' (o 'estado_del_procedimiento' indique "
                    "un proceso finalizado) y, aun así, 'valor_total_adjudicacion' "
                    "permanezca en cero."
                ),
            },
        ],
    },
    {
        "slug": "dimensiones-de-calidad",
        "numero": "05",
        "titulo": "Evaluación de las dimensiones de calidad",
        "resumen": "Métricas, fórmulas, resultados e interpretación de completitud, exactitud, consistencia, unicidad, validez y actualidad.",
        "bloques": [
            {
                "tipo": "tabla",
                "subtitulo": "Resumen de métricas por dimensión",
                "encabezados": ["Dimensión", "Métrica / fórmula", "Resultado", "Interpretación"],
                "filas": [
                    ["Completitud", "1 − (valores faltantes / total de celdas)", "99,9994 % global; 99,98 % en 'nombre_del_procedimiento'; 100 % en las 33 variables restantes", "El dataset presenta un nivel de completitud muy alto; el único vacío detectado (2 registros) es marginal y no compromete el análisis"],
                    ["Unicidad", "1 − (registros duplicados / total de registros)", "99,21 % considerando duplicados exactos (79 registros); 97,92 % considerando duplicados por 'id_del_proceso' (208 registros)", "La duplicidad por 'id_del_proceso' es más relevante que la exacta y es coherente con la práctica de SECOP II de republicar un proceso ante cada adenda o modificación"],
                    ["Validez", "% de registros cuyo valor cumple el tipo de dato y el dominio esperado para la variable", "'fecha_de_publicacion_del' incumple el tipo esperado en el 100 % de los registros (almacenada como texto en vez de fecha); 8.804 registros (88,04 %) con 'valor_total_adjudicacion' = 0 y 'precio_base' > 0, pendientes de reclasificar según 'adjudicado'/'estado_del_procedimiento'", "Existen dos problemas de validez relevantes: uno estructural (tipo de dato de fecha) y uno de dominio (valor adjudicado en cero), este último probablemente sobreestimado por no filtrar procesos aún no adjudicados"],
                    ["Consistencia", "% de registros que cumplen reglas lógicas entre variables (p. ej. proveedores_unicos_con ≤ proveedores_invitados; fecha_adjudicacion ≥ fecha_de_publicacion_del)", "92,36 % de los registros cumplen la regla 'proveedores_unicos_con ≤ proveedores_invitados' (764 registros, 7,64 %, la incumplen); 0 % de inconsistencia de formato en 'entidad' (2.082 valores únicos, iguales antes y después de normalizar texto)", "La inconsistencia en proveedores es la más relevante para el análisis de riesgo, pues afecta directamente el indicador derivado 'ratio_competencia_real' definido en la Etapa 1"],
                    ["Exactitud", "% de registros de una muestra aleatoria (n = 100, ~1 % del dataset) cuyos valores coinciden con el proceso original consultado mediante 'urlproceso'", "Pendiente de verificación muestral manual; metodología y tamaño de muestra definidos", "La exactitud solo puede confirmarse contrastando contra la fuente original (SECOP II), dado que el dataset es una descarga secundaria vía API"],
                    ["Actualidad", "% de registros dentro del periodo de análisis definido (2020-2025); antigüedad del dato más reciente respecto a la fecha de consulta", "100 % de los registros están entre 2020-01-01 y 2025-12-01; el dato más reciente tiene un rezago aproximado de 8 meses frente a la fecha de consulta (agosto de 2026)", "El dataset cumple el periodo de análisis definido y no requiere filtrado adicional por fecha"],
                ],
            },
            {
                "tipo": "texto",
                "subtitulo": "Nota metodológica",
                "contenido": (
                    "Las dimensiones de completitud, unicidad y actualidad se "
                    "calcularon directamente sobre la salida real del script "
                    "'diagnostico_calidad.py'. Las dimensiones de validez, "
                    "consistencia y exactitud requieren, además del perfilamiento "
                    "básico, la ejecución de reglas de negocio y una verificación "
                    "muestral contra la fuente original; dicha ejecución se "
                    "documentará con evidencia (código y resultados) en la "
                    "siguiente actualización del informe técnico, previa a la "
                    "entrega final."
                ),
            },
        ],
    },
    {
        "slug": "inventario-de-problemas",
        "numero": "06",
        "titulo": "Inventario de problemas encontrados",
        "resumen": "Listado de problemas de calidad detectados, con variable afectada, magnitud, dimensión e impacto.",
        "bloques": [
            {
                "tipo": "tabla",
                "subtitulo": "Inventario de problemas de calidad",
                "encabezados": ["Variable / campo afectado", "Descripción del problema", "Registros afectados", "Dimensión relacionada", "Nivel de impacto", "Evidencia"],
                "filas": [
                    ["id_del_proceso", "Registros duplicados por 'id_del_proceso' (varias versiones del mismo proceso)", "208 (2,08 %)", "Unicidad", "Medio", "Salida de 'diagnostico_calidad.py' — sección DUPLICADOS"],
                    ["Todas las columnas (fila completa)", "Registros duplicados exactos en todas las variables", "79 (0,79 %)", "Unicidad", "Bajo", "Salida de 'diagnostico_calidad.py' — sección DUPLICADOS"],
                    ["nombre_del_procedimiento", "Valores faltantes en el nombre del procedimiento", "2 (0,02 %)", "Completitud", "Bajo", "Salida de 'diagnostico_calidad.py' — sección VALORES FALTANTES"],
                    ["fecha_de_publicacion_del", "Variable temporal almacenada con tipo de dato texto (str) en lugar de fecha (datetime)", "10.000 (100 %)", "Validez", "Alto", "Salida de 'diagnostico_calidad.py' — sección TIPOS DE DATOS"],
                    ["codigo_entidad", "Identificador administrativo almacenado como numérico (int64), con riesgo de operaciones aritméticas indebidas o pérdida de ceros a la izquierda", "10.000 (100 %)", "Validez", "Bajo", "Salida de 'diagnostico_calidad.py' — sección TIPOS DE DATOS"],
                    ["entidad", "Se verificó inconsistencia de formato en el nombre de entidad (mayúsculas, espacios); no se detectaron variaciones", "0 (0,00 %) — descartado tras validación", "Consistencia", "Descartado", "Salida del script extendido — sección REVISIÓN DE FORMATOS (Entidad): 2.082 valores únicos antes y después de normalizar"],
                    ["proveedores_unicos_con / proveedores_invitados", "Registros donde el número de proveedores únicos con respuesta supera al número de proveedores invitados", "764 (7,64 %)", "Consistencia", "Alto", "Salida del script extendido — sección INCONSISTENCIAS Y REGLAS DE NEGOCIO"],
                    ["valor_total_adjudicacion / precio_base", "Registros con precio base mayor a cero pero valor adjudicado registrado en cero", "8.804 (88,04 %) — porcentaje probablemente sobreestimado; requiere cruzarse con 'adjudicado'/'estado_del_procedimiento' para aislar los casos realmente inconsistentes", "Validez / Exactitud", "Alto (a confirmar tras refinar la regla)", "Salida del script extendido — sección INCONSISTENCIAS Y REGLAS DE NEGOCIO"],
                    ["valor_total_adjudicacion", "Valores atípicos detectados mediante rango intercuartílico (IQR)", "873 (8,73 %)", "Validez", "Medio", "Salida del script extendido — sección VALORES ATÍPICOS (IQR)"],
                    ["departamento_entidad / ciudad_entidad", "Riesgo de codificación de nombres de departamento/ciudad distinta al catálogo oficial DIVIPOLA", "Por cuantificar con script extendido", "Consistencia", "Medio", "Comparación pendiente contra catálogo DIVIPOLA (DANE)"],
                ],
            },
        ],
    },
    {
        "slug": "analisis-de-causas",
        "numero": "07",
        "titulo": "Análisis de las causas",
        "resumen": "Posibles orígenes de los principales problemas de calidad identificados.",
        "bloques": [
            {
                "tipo": "tabla",
                "subtitulo": "Causas probables de los problemas identificados",
                "encabezados": ["Problema", "Causa probable", "Tipo de causa"],
                "filas": [
                    ["Duplicados por 'id_del_proceso'", "SECOP II publica una nueva versión del proceso ante cada modificación o adenda, sin eliminar la versión anterior en la descarga masiva", "Duplicidad de fuente / diseño de la plataforma origen"],
                    ["Duplicados exactos", "Descargas repetidas o solapadas al momento de construir el archivo consolidado desde la API", "Error de proceso de extracción (ETL)"],
                    ["Valores faltantes en 'nombre_del_procedimiento'", "Ausencia de captura de este campo por parte de la entidad al publicar el proceso", "Error de captura en el origen"],
                    ["Tipo de dato incorrecto en 'fecha_de_publicacion_del'", "La API de SECOP II entrega las fechas como cadenas de texto (formato ISO), y el proceso de carga no realizó la conversión explícita a tipo fecha", "Ausencia de validación / conversión de tipos en el pipeline de carga"],
                    ["Descuadre entre proveedores invitados y proveedores únicos con respuesta (764 registros)", "Errores de captura en el módulo de gestión de ofertas de SECOP II, actualizaciones parciales del proceso o registro de invitaciones que luego no se formalizan como respuesta", "Error de captura en el origen"],
                    ["Valor adjudicado en cero con precio base mayor a cero (8.804 registros)", "En su mayoría corresponde a procesos que aún no han sido adjudicados al momento de la descarga (estado 'en curso' o 'publicado'), y en una proporción menor podría deberse a error de captura en procesos ya cerrados", "Comportamiento esperado del dato (proceso en curso), mezclado en menor medida con error de captura"],
                    ["Codificación distinta de departamento/ciudad frente a DIVIPOLA", "Uso de texto libre en vez de un código estandarizado en el formulario de creación del proceso", "Formatos diferentes entre fuentes"],
                ],
            },
        ],
    },
    {
        "slug": "integracion-y-homologacion",
        "numero": "08",
        "titulo": "Integración y homologación de los datos",
        "resumen": "Criterios para unificar nombres, categorías, unidades y formatos entre las fuentes utilizadas.",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Fuentes a integrar",
                "contenido": (
                    "El dataset consolidado de la Etapa 1 integra, principalmente, "
                    "el conjunto SECOP II (nivel nacional/regional) con los "
                    "indicadores de Contratación a un Clic y los Planes Anuales de "
                    "Adquisiciones de la Gobernación de Cundinamarca (nivel "
                    "regional) y con los indicadores de OCDS y Benchmarking Public "
                    "Procurement (nivel global). En esta etapa, la homologación se "
                    "concentra en dejar lista y validada la fuente nacional "
                    "(SECOP II) antes de anexar los indicadores agregados de los "
                    "otros niveles."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Reglas de homologación aplicadas o propuestas",
                "encabezados": ["Aspecto", "Regla de homologación", "Estado"],
                "filas": [
                    ["Tipo de dato de fechas", "Convertir 'fecha_de_publicacion_del' (y demás variables de fecha) de texto a tipo datetime con formato AAAA-MM-DD", "Propuesta — pendiente de aplicar en el script"],
                    ["Nombres de entidades", "Normalizar a minúsculas, sin tildes, y comparar contra el catálogo de entidades públicas de Colombia Compra Eficiente", "Propuesta — pendiente de aplicar"],
                    ["Nombres de departamento y ciudad", "Cruzar contra el catálogo DIVIPOLA (DANE) para unificar nombres y códigos", "Propuesta — pendiente de aplicar"],
                    ["Identificador de proceso", "Conservar únicamente la versión más reciente por 'id_del_proceso' al eliminar duplicados", "Propuesta — pendiente de aplicar"],
                    ["Unidad monetaria (integración con nivel global)", "Convertir montos en pesos colombianos (COP) a dólares (USD) usando la Tasa Representativa del Mercado (TRM) del periodo correspondiente, para comparación con indicadores globales", "Propuesta — pendiente de aplicar, requiere fuente TRM (Banco de la República)"],
                    ["Llave de integración entre niveles", "Uso de la columna 'nivel_comparacion' (Global/Nacional/Regional) y del año de referencia derivado de la fecha de publicación, definidos en la Etapa 1", "Diseñada en la Etapa 1 — a implementar en el script de integración"],
                ],
            },
        ],
    },
    {
        "slug": "plan-de-tratamiento",
        "numero": "09",
        "titulo": "Plan de tratamiento",
        "resumen": "Acciones definidas para corregir o controlar cada problema identificado, con su justificación.",
        "bloques": [
            {
                "tipo": "tabla",
                "subtitulo": "Plan de tratamiento por problema",
                "encabezados": ["Problema", "Acción de tratamiento", "Justificación"],
                "filas": [
                    ["Duplicados por 'id_del_proceso' (208 registros)", "Conservar únicamente el registro más reciente por 'id_del_proceso' (usando la fecha de publicación o un número de versión, si está disponible)", "Evita sobrerrepresentar procesos que fueron modificados varias veces y distorsionar los conteos y agregados"],
                    ["Duplicados exactos (79 registros)", "Eliminar filas completamente duplicadas con 'drop_duplicates()'", "No aportan información adicional y sesgan estadísticas descriptivas y conteos"],
                    ["Valores faltantes en 'nombre_del_procedimiento' (2 registros)", "Imputar con la etiqueta 'Sin nombre registrado' en lugar de eliminar el registro", "El campo es descriptivo y no numérico; eliminar el registro completo por 2 valores faltantes implicaría pérdida innecesaria de información en otras 33 variables"],
                    ["Tipo de dato incorrecto en 'fecha_de_publicacion_del'", "Convertir la columna a tipo datetime con 'pd.to_datetime()', validando el formato AAAA-MM-DD", "Es prerrequisito para calcular la variable derivada 'dias_publicacion_adjudicacion' definida en la Etapa 1"],
                    ["'codigo_entidad' almacenado como numérico", "Convertir a tipo texto/categórico para evitar operaciones aritméticas indebidas y preservar ceros a la izquierda", "El código de entidad es un identificador, no una cantidad, y no debe sumarse ni promediarse"],
                    ["Inconsistencia de formato en 'entidad' (verificada: 0 registros afectados)", "No requiere acción correctiva; se documenta el chequeo como evidencia de calidad ya cumplida", "La comparación entre 2.082 valores únicos originales y 2.082 tras normalizar texto confirma que la variable ya está bien capturada en este aspecto"],
                    ["Incumplimiento de 'proveedores_unicos_con' ≤ 'proveedores_invitados' (764 registros, 7,64 %)", "Marcar como 'inconsistente' en una columna adicional ('flag_consistencia_proveedores'), sin eliminar el registro, para su revisión manual posterior", "Un descarte automático podría eliminar procesos legítimos con particularidades de registro; se prioriza el marcado y la revisión, dado que esta regla alimenta directamente el indicador de riesgo 'ratio_competencia_real'"],
                    ["Valor adjudicado en cero con precio base > 0 (8.804 registros, 88,04 %)", "Refinar la regla cruzándola con 'adjudicado' y 'estado_del_procedimiento': mantener el valor en cero para procesos aún no adjudicados o en curso, y marcar como 'inconsistente' únicamente los casos donde 'adjudicado' = 'Sí' y el valor permanezca en cero", "Aplicar la regla original sin este refinamiento sobreestimaría el problema y llevaría a tratar como error un comportamiento normal del dato (procesos todavía no cerrados)"],
                    ["Codificación de departamento/ciudad distinta a DIVIPOLA", "Cruzar contra el catálogo DIVIPOLA y homologar nombres a la versión oficial", "Permite comparabilidad exacta con las fuentes regionales y con los datos del DANE"],
                    ["Valores atípicos en 'valor_total_adjudicacion' (873 registros, 8,73 %, método IQR)", "Marcar como 'atípico' en una columna adicional ('flag_atipico_valor'), sin eliminar el registro por defecto", "Un valor atípico puede ser un indicio de riesgo (sobrecosto o subvaloración) y no necesariamente un error de captura; eliminarlo de forma automática iría en contra del objetivo analítico del proyecto"],
                ],
            },
        ],
    },
    {
        "slug": "implementacion-flask",
        "numero": "10",
        "titulo": "Implementación en Flask",
        "resumen": "Descripción de la sección 'Calidad de Datos' incorporada en la aplicación web del proyecto.",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Descripción general de la sección",
                "contenido": (
                    "La aplicación Flask del proyecto (publicada en "
                    "https://datamining901.onrender.com/) incorpora una sección "
                    "denominada 'Calidad de Datos', construida a partir de este "
                    "módulo 'submenu2.py', que presenta de forma secuencial: la "
                    "descripción del conjunto de datos, los resultados del "
                    "perfilamiento, las dimensiones y métricas evaluadas, el "
                    "inventario de problemas, las acciones de tratamiento "
                    "aplicadas, una comparación antes/después y las tablas e "
                    "indicadores correspondientes."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Comparación antes y después (a completar tras aplicar el tratamiento)",
                "contenido": (
                    "Una vez ejecutado el plan de tratamiento sobre el dataset "
                    "consolidado, se incorporará en esta sección una tabla "
                    "comparativa 'antes / después' para, como mínimo: número de "
                    "registros duplicados (79 exactos y 208 por 'id_del_proceso' "
                    "antes del tratamiento), porcentaje de completitud de "
                    "'nombre_del_procedimiento' (99,98 % antes), tipo de dato de "
                    "'fecha_de_publicacion_del' (texto antes, fecha después), "
                    "número de registros marcados como inconsistentes en la "
                    "regla proveedores_unicos_con ≤ proveedores_invitados (764 "
                    "antes del marcado), número de registros con valor "
                    "adjudicado en cero reclasificados tras cruzar con "
                    "'adjudicado'/'estado_del_procedimiento' (8.804 antes de "
                    "refinar la regla) y número de valores atípicos marcados en "
                    "'valor_total_adjudicacion' (873 antes del marcado, método "
                    "IQR)."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Elementos visuales previstos",
                "contenido": (
                    "Se prevé incluir, dentro de la sección 'Calidad de Datos' de "
                    "la aplicación: una tabla resumen de perfilamiento (registros, "
                    "variables, duplicados, faltantes), un gráfico de barras con "
                    "el porcentaje de completitud por variable, un gráfico "
                    "comparativo de duplicados antes/después del tratamiento y "
                    "una tabla del inventario de problemas con su nivel de "
                    "impacto, tal como se documenta en los apartados anteriores "
                    "de este módulo."
                ),
            },
        ],
    },
    {
        "slug": "gestion-github",
        "numero": "11",
        "titulo": "Gestión en GitHub",
        "resumen": "Rama de trabajo, commits, pull request e integración con la rama principal.",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Flujo de trabajo en GitHub",
                "contenido": (
                    "El desarrollo de la Etapa 2 se gestiona en el repositorio "
                    "público del proyecto (https://github.com/disociando31/datamining901), "
                    "siguiendo el mismo esquema utilizado en la Etapa 1: creación "
                    "de una rama específica para la etapa (por ejemplo, "
                    "'r2-calidad-datos'), desarrollo y commits incrementales del "
                    "script de diagnóstico, del módulo 'submenu2.py' y de la "
                    "sección Flask correspondiente, apertura de un pull request "
                    "hacia la rama principal una vez finalizada la etapa, y "
                    "verificación del despliegue actualizado en "
                    "https://datamining901.onrender.com/ tras la integración."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Evidencias pendientes de incorporar en el informe técnico",
                "contenido": (
                    "Capturas de la rama creada en GitHub, historial de commits "
                    "asociados a la Etapa 2, captura del pull request abierto y "
                    "de su integración (merge) con la rama principal, y captura "
                    "de la aplicación Flask ya desplegada mostrando la nueva "
                    "sección 'Calidad de Datos' en funcionamiento."
                ),
            },
        ],
    },
    {
        "slug": "referencias-y-enlaces",
        "numero": "12",
        "titulo": "Referencias bibliográficas y enlaces del proyecto",
        "resumen": "Fuentes normativas y técnicas consultadas, y enlaces oficiales del proyecto.",
        "bloques": [
            {
                "tipo": "enlaces",
                "subtitulo": "Enlaces del proyecto",
                "lista": [
                    {"texto": "Repositorio del proyecto en GitHub", "url": "https://github.com/disociando31/datamining901"},
                    {"texto": "Aplicación Flask publicada", "url": "https://datamining901.onrender.com/"},
                ],
            },
            {
                "tipo": "enlaces",
                "subtitulo": "Fuentes de datos y documentación técnica consultadas",
                "lista": [
                    {"texto": "SECOP II — Procesos de Contratación (dataset y diccionario de columnas)", "url": "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"},
                    {"texto": "API Socrata (SODA) del dataset SECOP II", "url": "https://www.datos.gov.co/resource/p6dx-8zbt.json"},
                    {"texto": "Codificación DIVIPOLA (DANE) — departamentos y municipios", "url": "https://geoportal.dane.gov.co/laboratorio/codificacion-divipola/"},
                    {"texto": "Colombia Compra Eficiente — sitio institucional", "url": "https://www.colombiacompra.gov.co/"},
                    {"texto": "Open contracting partnership", "url": "https://data.open-contracting.org/es/publication/61"},
                    {"texto": "Datos Abiertos de Compras Públicas de Ecuador", "url": "https://datosabiertos.compraspublicas.gob.ec/PLATAFORMA/datos-abiertos"},
                    {"texto": "Contratos públicos - Gobernación de Cundinamarca", "url": "https://www.contratos.gov.co/consultas/resultadoListadoProcesos.jsp?entidad=225000001&desdeFomulario=true#"},
                ],
            },
            {
                "tipo": "enlaces",
                "subtitulo": "Marco normativo",
                "lista": [
                    {"texto": "Ley 1712 de 2014 — Transparencia y Acceso a la Información Pública", "url": "https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=56882"},
                    {"texto": "Ley 1581 de 2012 — Protección de Datos Personales", "url": "https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=49981"},
                ],
            },
        ],  
    },
]
