# -*- coding: utf-8 -*-


# -----------------------------------------------------------------------
# 1. INFORMACIÓN GENERAL DEL PROYECTO
# -----------------------------------------------------------------------
INFO_PROYECTO = {
    "materia": "Minería de Datos",
    "titulo": "Contratación Pública y Gestión de Recursos: Identificación de Patrones y Riesgos",
    "participantes": [
        "David Santiago Arias Ramirez",
        "Ian Andres Galindo Bejarano",
        "Juan Pablo Villarraga Espitia",
        "Edwin Estiben Leal Vargas"
    ],
}

# -----------------------------------------------------------------------
# 2. MENÚ PRINCIPAL
# -----------------------------------------------------------------------
ETAPAS = [
    {
        "slug": "etapa-1",
        "nombre": "Etapa 1",
        "activa": True,
    },
    {
            "slug": "etapa-2",
            "nombre": "Etapa 2",
            "activa": True,
        },
]

# -----------------------------------------------------------------------
# 3. SUBMENÚS DE LA ETAPA 1
# -----------------------------------------------------------------------
SUBMENUS_ETAPA_1 = [
    {
        "slug": "problema-y-contexto",
        "numero": "01",
        "titulo": "Problema y contexto",
        "resumen": "Descripción del problema que se aborda y el entorno en el que ocurre.",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Contexto general",
                "contenido": (
                    "La contratación pública es el mecanismo mediante el cual los "
                    "gobiernos adquieren bienes, servicios y obras usando recursos "
                    "públicos. Representa entre el 12% y el 20% del PIB en la mayoría "
                    "de países (OCDE), lo que la convierte en un área crítica para la "
                    "eficiencia del gasto, la transparencia y la lucha contra la "
                    "corrupción. A nivel global, iniciativas como el Open Contracting "
                    "Data Standard (OCDS) buscan estandarizar y abrir estos datos. En "
                    "Colombia, la plataforma SECOP (Sistema Electrónico de "
                    "Contratación Pública) centraliza los procesos de contratación "
                    "estatal, generando grandes volúmenes de datos susceptibles de "
                    "análisis."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Descripción del problema",
                "contenido": (
                    "Existe una asimetría entre el volumen de datos abiertos de "
                    "contratación pública disponibles y su uso efectivo para "
                    "identificar patrones de riesgo, ineficiencia o irregularidad en "
                    "la asignación de recursos públicos. Muchas entidades "
                    "territoriales no cuentan con herramientas analíticas que les "
                    "permitan comparar su desempeño contractual frente a estándares "
                    "nacionales o internacionales, ni detectar anomalías (sobrecostos, "
                    "concentración de proveedores, retrasos, modalidades de "
                    "contratación atípicas)."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Análisis por niveles",
                "contenido": (
                    "Global: estándares de datos abiertos de contratación (OCDS), "
                    "índices de transparencia (Open Contracting Partnership, Banco "
                    "Mundial - Procurement) y comparación entre países en eficiencia "
                    "y riesgo de corrupción en compras públicas.\n\n"
                    "Nacional (Colombia): datos de SECOP I y II, Colombia Compra "
                    "Eficiente, análisis de modalidades de contratación, entidades "
                    "contratantes, montos y proveedores frecuentes.\n\n"
                    "Regional: comportamiento contractual por departamento/municipio "
                    "(concentración de contratos, entidades con mayor gasto, "
                    "disparidades regionales en ejecución de recursos), tomando "
                    "Cundinamarca como departamento de referencia."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Justificación",
                "contenido": (
                    "Identificar patrones y factores de riesgo en la contratación "
                    "pública permite fortalecer la transparencia, optimizar el uso de "
                    "recursos públicos y generar alertas tempranas frente a posibles "
                    "irregularidades. El impacto potencial abarca desde el diseño de "
                    "políticas públicas hasta el desarrollo de herramientas de "
                    "control y vigilancia ciudadana."
                ),
            },
        ],
    },
    {
        "slug": "preguntas",
        "numero": "02",
        "titulo": "Pregunta principal y preguntas secundarias",
        "resumen": "Pregunta central del proyecto y las preguntas de apoyo que la complementan.",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Pregunta principal",
                "contenido": (
                    "¿Qué patrones y factores de riesgo se pueden identificar en los "
                    "procesos de contratación pública mediante técnicas de minería "
                    "de datos?"
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Preguntas secundarias",
                "contenido": (
                    "1. ¿Cuáles son las modalidades de contratación más utilizadas en "
                    "Colombia y cómo varían entre departamentos/regiones?\n"
                    "2. ¿Existe concentración de contratos en un número reducido de "
                    "proveedores (posible indicador de riesgo de corrupción o falta "
                    "de competencia)?\n"
                    "3. ¿Qué relación existe entre el monto de los contratos, el tipo "
                    "de entidad contratante y el tiempo de ejecución o retrasos?\n"
                    "4. ¿Cómo se compara el nivel de apertura y estandarización de "
                    "los datos de contratación colombianos frente a los estándares "
                    "globales (OCDS)?\n"
                    "5. ¿Qué sectores (salud, infraestructura, educación, etc.) "
                    "concentran mayor volumen de recursos y cómo ha evolucionado "
                    "esto en el tiempo?"
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Conocimiento esperado",
                "contenido": (
                    "Se espera identificar patrones de concentración de proveedores y "
                    "entidades (clustering), anomalías o outliers en montos y plazos "
                    "que sugieran riesgo (detección de anomalías), relaciones entre "
                    "variables como tipo de entidad, sector, modalidad y monto "
                    "(asociación/correlación), tendencias temporales en el gasto "
                    "público por sector y región, y comparativos entre el desempeño "
                    "de Colombia y estándares/benchmarks globales, así como entre "
                    "regiones dentro del país."
                ),
            },
        ],
    },
    {
        "slug": "necesidades-de-informacion",
        "numero": "03",
        "titulo": "Necesidades de información",
        "resumen": "Qué información se necesita recolectar para responder las preguntas planteadas.",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Entidades involucradas",
                "contenido": (
                    "Colombia Compra Eficiente (ANCP-CCE), entidad rectora del "
                    "sistema de compra pública y administradora de SECOP I y SECOP "
                    "II. Entidades estatales contratantes de los tres niveles "
                    "(nacional, departamental y municipal), en particular la "
                    "Gobernación de Cundinamarca y sus dependencias. Proveedores y "
                    "contratistas registrados en el Registro Único de Proponentes "
                    "(RUP). A nivel global, Open Contracting Partnership (OCP), "
                    "responsable del estándar OCDS, y el Banco Mundial, a través de "
                    "su iniciativa Benchmarking Public Procurement, que compara la "
                    "regulación y desempeño de la contratación pública entre países."
                ),
            },
            {
                "tipo": "enlaces",
                "subtitulo": "Enlaces de las entidades involucradas",
                "lista": [
                    {"texto": "Colombia Compra Eficiente (ANCP-CCE)", "url": "https://www.colombiacompra.gov.co/"},
                    {"texto": "SECOP I - Consulta de procesos", "url": "https://www.contratos.gov.co/consultas/inicioConsulta.do"},
                    {"texto": "SECOP II - Portal transaccional", "url": "https://community.secop.gov.co/"},
                    {"texto": "Registro Único de Proponentes (RUP) - Cámara de Comercio", "url": "https://www.rues.org.co/RUP"},
                    {"texto": "Gobernación de Cundinamarca", "url": "https://www.cundinamarca.gov.co/"},
                    {"texto": "Open Contracting Partnership (OCP)", "url": "https://www.open-contracting.org/"},
                    {"texto": "Open Contracting Data Standard (OCDS)", "url": "https://standard.open-contracting.org/latest/en/"},
                    {"texto": "Banco Mundial - Benchmarking Public Procurement", "url": "https://bpp.worldbank.org/"},
                ],
            },
            {
                "tipo": "texto",
                "subtitulo": "Variables relevantes y su justificación (nombres reales de la API SECOP II)",
                "contenido": (
                    "Las variables se agrupan según el tipo de patrón de riesgo/fraude "
                    "que permiten detectar, usando los nombres de campo reales de la "
                    "API de SECOP II (ver diccionario de datos oficial, disponible en "
                    "el portal de datos.gov.co, sección 'Información Adicional' del "
                    "conjunto de datos SECOP II — Procesos de Contratación):\n\n"
                    "Grupo 1 — Competencia simulada o insuficiente (indicador central "
                    "de riesgo de colusión): 'proveedores_invitados', "
                    "'proveedores_con_invitacion' (directa), "
                    "'proveedores_que_manifestaron' (interés), "
                    "'respuestas_al_procedimiento', 'respuestas_externas', "
                    "'conteo_de_respuestas_a_ofert' (as), 'proveedores_unicos_con' "
                    "(respuestas). Con estas se calcula un ratio de competencia real "
                    "(respuestas únicas / invitados); un proceso formalmente "
                    "competitivo con un solo oferente efectivo es la señal de riesgo "
                    "más documentada en la literatura de contratación pública.\n\n"
                    "Grupo 2 — Uso atípico de la modalidad de contratación: "
                    "'modalidad_de_contratacion', 'justificaci_n_modalidad_de', "
                    "'tipo_de_contrato', 'subtipo_de_contrato', "
                    "'codigo_principal_de_categoria' (UNSPSC). Permiten detectar si "
                    "una entidad usa contratación directa muy por encima de lo "
                    "esperado para su categoría de compra, o sin justificación "
                    "registrada.\n\n"
                    "Grupo 3 — Anomalías de tiempo y de valor: 'precio_base' y "
                    "'valor_total_adjudicacion' (ratio adjudicado/base, para detectar "
                    "sobreprecio o precios sospechosamente bajos); "
                    "'fecha_de_publicacion_del', 'fecha_de_recepcion_de' "
                    "(respuestas), 'fecha_de_apertura_de_respuesta', "
                    "'fecha_de_apertura_efectiva', 'fecha_adjudicacion', 'duracion' y "
                    "'unidad_de_duracion'. Con las fechas se calcula el número de "
                    "días entre publicación y adjudicación: plazos anormalmente "
                    "cortos reducen la posibilidad real de que otros proveedores "
                    "compitan.\n\n"
                    "Grupo 4 — Concentración y relaciones entidad-proveedor-"
                    "adjudicador (posible colusión o direccionamiento): 'entidad', "
                    "'nit_entidad', 'nombre_del_adjudicador', 'nombre_del_proveedor', "
                    "'nit_del_proveedor_adjudicado', 'departamento_proveedor' y "
                    "'ciudad_proveedor' comparados contra 'departamento_entidad' y "
                    "'ciudad_entidad'. Permiten construir una red entidad→"
                    "adjudicador→proveedor y medir reincidencia (mismo adjudicador "
                    "favoreciendo repetidamente al mismo proveedor) o contratos "
                    "adjudicados a proveedores fuera de su región de forma atípica.\n\n"
                    "Variables de trazabilidad y filtrado (no son indicador de "
                    "riesgo por sí mismas, pero son obligatorias para poder unir, "
                    "depurar y comparar): 'id_del_proceso', 'referencia_del_proceso', "
                    "'urlproceso', 'codigo_entidad', 'departamento_entidad', "
                    "'ciudad_entidad', 'ordenentidad' (Nacional/Regional), "
                    "'estado_del_procedimiento', 'estado_resumen' y 'adjudicado'.\n\n"
                    "Variables descartadas por bajo valor analítico para este "
                    "objetivo (no se incluyen en el dataset consolidado, o se dejan "
                    "como opcionales): 'descripcion_del_procedimiento' (texto libre, "
                    "solo útil si se hace minería de texto en una etapa posterior), "
                    "'ppi', 'id_del_portafolio', 'categorias_adicionales', "
                    "'numero_de_lotes' y 'visualizaciones_del_procedimiento' (mide "
                    "interés público, no riesgo de contratación)."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Periodo de análisis",
                "contenido": (
                    "Se tomará como periodo de análisis 2020-2025 para SECOP II, por "
                    "ser el rango en el que la plataforma transaccional ya cuenta con "
                    "una adopción amplia y estable por parte de las entidades "
                    "estatales, lo cual reduce el sesgo de subregistro propio de los "
                    "primeros años de la plataforma (lanzada en 2016). Para los "
                    "indicadores globales de referencia se usará la última "
                    "publicación disponible de cada fuente."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Cobertura geográfica",
                "contenido": (
                    "Global: muestra de países incluidos en OCDS/Benchmarking Public "
                    "Procurement, usados como referencia comparativa.\n"
                    "Nacional: todo el territorio colombiano (32 departamentos y "
                    "Bogotá D.C.), según registro de SECOP I y II.\n"
                    "Regional: departamento de Cundinamarca y sus municipios, tomado "
                    "como caso de estudio regional."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Población / unidad de análisis y granularidad",
                "contenido": (
                    "La unidad de análisis principal es el proceso de contratación "
                    "(y, cuando aplica, el contrato derivado de dicho proceso), "
                    "publicado por una entidad estatal colombiana. Se trabajará con "
                    "granularidad a nivel de proceso individual (no agregados "
                    "mensuales o anuales), lo que permite luego construir agregados "
                    "propios por entidad, sector, modalidad, departamento o periodo "
                    "según se requiera en el análisis, evitando partir de datos ya "
                    "agregados que limiten el detalle del estudio."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Variables para comparar escalas global-nacional-regional",
                "contenido": (
                    "Para permitir la comparación entre niveles se estandarizarán al "
                    "menos las siguientes variables comunes: (1) monto contratado, "
                    "normalizado a USD o como porcentaje del gasto total del periodo, "
                    "para comparar magnitudes entre país/departamento; (2) sector u "
                    "objeto del contrato, mapeado a una clasificación común de tipo "
                    "CPV/CPC; (3) año/periodo de referencia, para alinear series de "
                    "tiempo entre fuentes con distinta frecuencia de publicación; y "
                    "(4) un indicador de nivel de apertura/competencia (por ejemplo, "
                    "número de oferentes o modalidad con/sin pluralidad de "
                    "oferentes), que tiene equivalentes tanto en los indicadores "
                    "globales de Benchmarking Public Procurement como en los datos "
                    "de SECOP II."
                ),
            },
        ],
    },
    {
        "slug": "fuentes-de-datos",
        "numero": "04",
        "titulo": "Fuentes de datos",
        "resumen": "Origen de los datos utilizados: de dónde provienen y cómo se obtuvieron.",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Criterio de clasificación",
                "contenido": (
                    "Se documentan al menos dos fuentes por nivel (global, nacional y "
                    "regional), procurando que en conjunto queden representados los "
                    "tres tipos de fuente exigidos: primarias (registro directo del "
                    "proceso de contratación hecho por la propia entidad), "
                    "secundarias (datos ya recolectados y publicados por una entidad "
                    "responsable, como Colombia Compra Eficiente) y terciarias "
                    "(portales que integran y redistribuyen datos recopilados por "
                    "terceros, como los portales de datos abiertos). Cada fuente "
                    "incluye su enlace de consulta directo para garantizar "
                    "trazabilidad completa hasta el dato original."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Nivel Nacional — Colombia",
                "encabezados": ["Campo", "Fuente 1", "Fuente 2", "Fuente 3"],
                "filas": [
                    ["Nombre", "Consulta de procesos SECOP I (detalleProceso)", "SECOP II - Procesos de Contratación", "Portal de Datos Abiertos del Estado Colombiano"],
                    ["Institución responsable", "Colombia Compra Eficiente (ANCP-CCE)", "Colombia Compra Eficiente (ANCP-CCE)", "MinTIC / ANCP-CCE"],
                    ["URL", "https://www.contratos.gov.co/consultas/inicioConsulta.do", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt", "https://www.datos.gov.co/"],
                    ["Tipo de fuente", "Primaria", "Secundaria", "Terciaria"],
                    ["Cobertura geográfica", "Nacional (todas las entidades registradas)", "Nacional", "Nacional"],
                    ["Periodo disponible", "Histórico por proceso, variable según entidad", "2016 (lanzamiento SECOP II) a la fecha", "Depende de cada conjunto de datos publicado"],
                    ["Formato", "Consulta web individual (HTML por proceso)", "CSV / JSON vía API Socrata (SODA)", "CSV / JSON / API Socrata"],
                    ["Método de adquisición", "Consulta manual proceso por proceso mediante número de constancia", "Descarga masiva o consulta a la API pública (endpoint /resource)", "Descarga desde el catálogo del portal"],
                    ["Nº aprox. de registros", "1 (por consulta); se usa como verificación puntual, no como fuente masiva", "Del orden de varios millones de procesos acumulados desde 2016 (cifra exacta a validar al momento de la descarga)", "Cientos de conjuntos de datos de contratación disponibles"],
                    ["Variables disponibles", "Entidad, objeto, modalidad, valor, proveedor, fechas, estado, documentos del proceso", "entidad, nit_entidad, departamento, ciudad, orden, sector, modalidad_de_contratacion, tipo_de_contrato, precio_base, valor_del_contrato, fecha_de_firma, fecha_de_inicio, fecha_de_fin, estado_del_procedimiento, proveedor_adjudicado, nit_proveedor, urlproceso", "Metadatos de cada conjunto: nombre, entidad publicadora, columnas, frecuencia de actualización"],
                    ["Fecha de consulta", "Agosto de 2026", "Agosto de 2026", "Agosto de 2026"],
                    ["Restricciones de uso", "Uso público, sujeto a Ley 1712 de 2014 (transparencia); no permite descarga masiva automatizada", "Datos abiertos, licencia de datos abiertos de Colombia (uso libre citando la fuente)", "Licencia de datos abiertos de Colombia"],
                    ["Enlace directo de consulta / API", "https://www.contratos.gov.co/consultas/inicioConsulta.do", "https://www.datos.gov.co/resource/p6dx-8zbt.json (endpoint API Socrata)", "https://www.datos.gov.co/browse?category=Gastos+Gubernamentales"],
                ],
            },
            {
                "tipo": "enlaces",
                "subtitulo": "Referencias — Nivel Nacional",
                "lista": [
                    {"texto": "SECOP I — Consulta de procesos (contratos.gov.co)", "url": "https://www.contratos.gov.co/consultas/inicioConsulta.do"},
                    {"texto": "SECOP II — Procesos de Contratación (datos.gov.co, dataset p6dx-8zbt)", "url": "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"},
                    {"texto": "API Socrata (SODA) del dataset SECOP II", "url": "https://www.datos.gov.co/resource/p6dx-8zbt.json"},
                    {"texto": "Portal de Datos Abiertos del Estado Colombiano", "url": "https://www.datos.gov.co/"},
                    {"texto": "Colombia Compra Eficiente — sitio institucional", "url": "https://www.colombiacompra.gov.co/"},
                    {"texto": "Ley 1712 de 2014 (Transparencia y Acceso a la Información Pública)", "url": "https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=56882"},
                ],
            },
            {
                "tipo": "texto",
                "subtitulo": "Justificación — Nivel Nacional",
                "contenido": (
                    "Pertinencia: SECOP II es la fuente oficial y más granular de "
                    "procesos de contratación en Colombia, y es la única que permite "
                    "responder directamente las preguntas sobre modalidades, montos, "
                    "proveedores y retrasos planteadas en el punto 2. Confiabilidad: "
                    "es administrada por Colombia Compra Eficiente, entidad rectora "
                    "del sistema de compra pública, con obligación legal de "
                    "publicación (Ley 1712 de 2014), lo que reduce el riesgo de datos "
                    "manipulados, aunque no elimina errores de digitación de cada "
                    "entidad. Actualidad: los datos se publican en tiempo real a "
                    "medida que las entidades gestionan sus procesos. Cobertura: "
                    "incluye, en principio, a todas las entidades estatales "
                    "obligadas a contratar por SECOP II, cubriendo el territorio "
                    "nacional; el uso de la consulta puntual en contratos.gov.co y "
                    "del catálogo de datos.gov.co permite además verificar y "
                    "contrastar registros individuales frente al conjunto masivo."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Nivel Regional — Cundinamarca",
                "encabezados": ["Campo", "Fuente 1", "Fuente 2"],
                "filas": [
                    ["Nombre", "Contratación a un Clic", "Planes Anuales de Adquisiciones (PAA) de la Gobernación"],
                    ["Institución responsable", "Gobernación de Cundinamarca", "Gobernación de Cundinamarca (dependencias del sector central)"],
                    ["URL", "https://www.cundinamarca.gov.co/web/contratacion", "https://www.cundinamarca.gov.co/web/transparencia/planeacion/planes-anuales-de-adquisiciones"],
                    ["Tipo de fuente", "Terciaria", "Primaria"],
                    ["Cobertura geográfica", "Departamento de Cundinamarca", "Departamento de Cundinamarca"],
                    ["Periodo disponible", "Vigencias publicadas por la Gobernación (últimos años)", "Vigencia fiscal en curso y anteriores publicadas"],
                    ["Formato", "Tablero web / enlaces a SECOP", "PDF / Excel"],
                    ["Método de adquisición", "Consulta en línea del tablero de contratación departamental", "Descarga directa de los documentos publicados"],
                    ["Nº aprox. de registros", "Variable según vigencia y dependencia consultada", "Decenas a cientos de ítems de adquisición planeada por vigencia"],
                    ["Variables disponibles", "Dependencia, proceso, estado, enlace a SECOP, valor estimado", "Objeto a contratar, valor estimado, modalidad prevista, fecha estimada de inicio, dependencia"],
                    ["Fecha de consulta", "Agosto de 2026", "Agosto de 2026"],
                    ["Restricciones de uso", "Uso público, información de carácter informativo/consulta", "Uso público bajo Ley 1712 de 2014"],
                    ["Enlace directo de consulta", "https://www.cundinamarca.gov.co/web/contratacion", "https://www.cundinamarca.gov.co/web/transparencia/planeacion/planes-anuales-de-adquisiciones"],
                ],
            },
            {
                "tipo": "enlaces",
                "subtitulo": "Referencias — Nivel Regional",
                "lista": [
                    {"texto": "Gobernación de Cundinamarca — Portal institucional", "url": "https://www.cundinamarca.gov.co/"},
                    {"texto": "Contratación a un Clic — Cundinamarca", "url": "https://www.cundinamarca.gov.co/web/contratacion"},
                    {"texto": "Planes Anuales de Adquisiciones — Transparencia Cundinamarca", "url": "https://www.cundinamarca.gov.co/web/transparencia/planeacion/planes-anuales-de-adquisiciones"},
                ],
            },
            {
                "tipo": "texto",
                "subtitulo": "Justificación — Nivel Regional",
                "contenido": (
                    "Pertinencia: Cundinamarca se toma como caso de estudio regional "
                    "porque rodea a Bogotá y agrupa municipios con capacidades "
                    "institucionales muy distintas, lo que la hace representativa "
                    "para observar disparidades regionales en la ejecución de "
                    "recursos. Confiabilidad: ambas fuentes son publicadas "
                    "directamente por la Gobernación, aunque Contratación a un Clic "
                    "depende de que cada dependencia mantenga actualizado el "
                    "tablero, por lo que se usará principalmente como punto de "
                    "verificación y enlace hacia SECOP, no como fuente masiva. "
                    "Actualidad: los Planes Anuales de Adquisiciones se publican por "
                    "vigencia fiscal y se actualizan ante modificaciones. Cobertura: "
                    "cubre el sector central del departamento; no incluye "
                    "necesariamente a todos los municipios ni a entidades "
                    "descentralizadas, lo cual se documenta como limitación en el "
                    "punto 8."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Nivel Global",
                "encabezados": ["Campo", "Fuente 1", "Fuente 2"],
                "filas": [
                    ["Nombre", "Open Contracting Data Standard (OCDS) / Open Contracting Partnership", "Benchmarking Public Procurement (Banco Mundial)"],
                    ["Institución responsable", "Open Contracting Partnership (OCP)", "Banco Mundial (World Bank Group)"],
                    ["URL", "https://standard.open-contracting.org/latest/en/", "https://bpp.worldbank.org/"],
                    ["Tipo de fuente", "Secundaria", "Secundaria"],
                    ["Cobertura geográfica", "Múltiples países que publican en formato OCDS", "Más de 180 economías"],
                    ["Periodo disponible", "Depende de cada país publicador", "Reportes periódicos (ediciones anuales/bienales)"],
                    ["Formato", "JSON estandarizado (esquema OCDS)", "Reportes e indicadores tabulares (PDF/Excel)"],
                    ["Método de adquisición", "Descarga de paquetes OCDS publicados por cada país", "Descarga de indicadores del reporte público"],
                    ["Nº aprox. de registros", "Variable por país (miles a millones de procesos publicados en formato abierto)", "1 indicador por país/edición, agregable por año"],
                    ["Variables disponibles", "Comprador, proveedor, valor, fechas, ítems, modalidad (esquema común OCDS)", "Índice de regulación, tiempo de trámite, transparencia, uso de e-procurement, por país"],
                    ["Fecha de consulta", "Agosto de 2026", "Agosto de 2026"],
                    ["Restricciones de uso", "Datos abiertos, licencia Open Data Commons", "Uso público con atribución al Banco Mundial"],
                    ["Enlace directo de consulta", "https://www.open-contracting.org/data/", "https://bpp.worldbank.org/en/data/exploreeconomies"],
                ],
            },
            {
                "tipo": "enlaces",
                "subtitulo": "Referencias — Nivel Global",
                "lista": [
                    {"texto": "Open Contracting Partnership — sitio institucional", "url": "https://www.open-contracting.org/"},
                    {"texto": "Open Contracting Data Standard (OCDS) — documentación del esquema", "url": "https://standard.open-contracting.org/latest/en/"},
                    {"texto": "OCP — Explorador de datos publicados por país", "url": "https://www.open-contracting.org/data/"},
                    {"texto": "Banco Mundial — Benchmarking Public Procurement (portal principal)", "url": "https://bpp.worldbank.org/"},
                    {"texto": "Banco Mundial — Explorar economías (indicadores por país)", "url": "https://bpp.worldbank.org/en/data/exploreeconomies"},
                ],
            },
            {
                "tipo": "texto",
                "subtitulo": "Justificación — Nivel Global",
                "contenido": (
                    "Pertinencia: OCDS y Benchmarking Public Procurement son las "
                    "referencias estándar de facto para comparar contratación "
                    "pública entre países, lo que permite responder la pregunta "
                    "secundaria sobre el nivel de apertura de Colombia frente a "
                    "estándares globales. Confiabilidad: son mantenidas por "
                    "organizaciones internacionales (Open Contracting Partnership y "
                    "Banco Mundial) con metodologías públicas y auditables. "
                    "Actualidad: OCDS depende de la frecuencia de publicación de "
                    "cada país; Benchmarking Public Procurement se actualiza por "
                    "ediciones periódicas del Banco Mundial. Cobertura: amplia a "
                    "nivel de países, pero con una granularidad mucho menor "
                    "(indicadores agregados por país/año) que las fuentes "
                    "nacionales y regionales, lo cual se documenta como limitación "
                    "de comparabilidad en el punto 8."
                ),
            },
        ],
    },
    {
        "slug": "dataset",
        "numero": "05",
        "titulo": "Dataset",
        "resumen": "Descripción general del conjunto de datos final utilizado en el proyecto.",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Estado actual",
                "contenido": (
                    "En esta etapa se define el diseño del dataset consolidado, "
                    "construido principalmente a partir de SECOP II (nivel "
                    "nacional/regional), complementado con el tablero de "
                    "Contratación a un Clic y los Planes Anuales de Adquisiciones de "
                    "Cundinamarca (nivel regional) y con los indicadores de OCDS y "
                    "Benchmarking Public Procurement (nivel global). La construcción "
                    "definitiva del archivo consolidado (mínimo 10.000 registros) se "
                    "realiza mediante descarga vía API de SECOP II "
                    "(https://www.datos.gov.co/resource/p6dx-8zbt.json), filtrando "
                    "por departamento y fecha, integrando después las variables "
                    "comparativas de nivel global y regional descritas en la sección "
                    "de necesidades de información."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Estrategia de integración",
                "contenido": (
                    "La integración entre niveles se realiza mediante dos llaves "
                    "comunes: geográfica (país / departamento / municipio, "
                    "normalizados a un mismo catálogo de nombres) y temporal (año de "
                    "publicación o firma del proceso). A cada registro nacional o "
                    "regional se le añade una columna de 'nivel_comparacion' que "
                    "permite unir, en el análisis, un proceso puntual de SECOP con el "
                    "indicador global o departamental del mismo periodo."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Estructura prevista del dataset consolidado (muestra ilustrativa, nombres reales de campo SECOP II)",
                "encabezados": ["id_del_proceso", "departamento_entidad", "modalidad_de_contratacion", "precio_base", "valor_total_adjudicacion", "proveedores_invitados", "proveedores_unicos_con", "fecha_de_publicacion_del", "fecha_adjudicacion", "nit_del_proveedor_adjudicado", "nivel_comparacion", "urlproceso"],
                "filas": [
                    ["CO1.PCCNTR.001", "Cundinamarca", "Contratación directa", "185000000", "185000000", "1", "1", "2024-03-01", "2024-03-15", "900123456-1", "Regional", "https://community.secop.gov.co/Public/Tendering/OpportunityDetail/Index?noticeUID=CO1.PCCNTR.001"],
                    ["CO1.PCCNTR.002", "Bogotá D.C.", "Licitación pública", "3000000000", "3200000000", "8", "5", "2023-05-10", "2023-07-02", "800987654-2", "Nacional", "https://community.secop.gov.co/Public/Tendering/OpportunityDetail/Index?noticeUID=CO1.PCCNTR.002"],
                    ["CO1.PCCNTR.003", "Antioquia", "Mínima cuantía", "12000000", "12500000", "3", "2", "2024-11-05", "2024-11-20", "901234567-3", "Nacional", "https://community.secop.gov.co/Public/Tendering/OpportunityDetail/Index?noticeUID=CO1.PCCNTR.003"],
                ],
            },
            {
                "tipo": "texto",
                "subtitulo": "Nota sobre trazabilidad del dataset",
                "contenido": (
                    "La columna 'urlproceso' (ejemplos ilustrativos arriba) es la que "
                    "permite, para cualquier registro del dataset consolidado, "
                    "regresar al proceso original publicado en la plataforma "
                    "transaccional SECOP II (https://community.secop.gov.co/) y "
                    "verificar su contenido completo, incluyendo documentos "
                    "soporte, observaciones y respuestas de proveedores."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Cumplimiento de requisitos mínimos",
                "contenido": (
                    "El diseño garantiza al menos 10 variables, con variables "
                    "numéricas ('precio_base', 'valor_total_adjudicacion', "
                    "'proveedores_invitados', 'proveedores_unicos_con'), variables "
                    "categóricas ('departamento_entidad', 'modalidad_de_contratacion', "
                    "'estado_del_procedimiento'), variable temporal "
                    "('fecha_de_publicacion_del' / 'fecha_adjudicacion') y variable "
                    "geográfica ('departamento_entidad' / 'departamento_proveedor'), "
                    "además del indicador derivado 'nivel_comparacion' "
                    "(global/nacional/regional) que permite filtrar y comparar las "
                    "tres escalas exigidas por el proyecto. El volumen meta de "
                    "10.000 registros se cubre principalmente con procesos de "
                    "SECOP II, dado que es la fuente con mayor granularidad y "
                    "volumen disponible."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Potencial para minería de datos",
                "contenido": (
                    "La estructura del dataset se diseñó pensando en las técnicas que "
                    "se aplicarán en etapas posteriores: 'ratio_valor_adjudicado_base' "
                    "y 'ratio_competencia_real' permiten detección de anomalías "
                    "(outliers que sugieran sobrecostos o baja competencia); "
                    "'nombre_del_adjudicador', 'nit_del_proveedor_adjudicado' y "
                    "'valor_total_adjudicacion' permiten clustering y análisis de "
                    "redes para identificar concentración y reincidencia; "
                    "'modalidad_de_contratacion', 'codigo_principal_de_categoria' y "
                    "'estado_del_procedimiento' permiten reglas de asociación entre "
                    "tipo de proceso y resultado; y 'fecha_de_publicacion_del'/"
                    "'fecha_adjudicacion' junto con 'duracion' permiten análisis de "
                    "series de tiempo y modelos predictivos de retrasos. La columna "
                    "derivada 'nivel_comparacion' es la que habilita, de forma "
                    "transversal, la comparación global-nacional-regional exigida en "
                    "el problema de investigación."
                ),
            },
        ],
    },
    {
        "slug": "diccionario-de-datos",
        "numero": "06",
        "titulo": "Diccionario de datos",
        "resumen": "Definición de cada variable del dataset: nombre, tipo de dato y significado.",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Unidad de análisis y registro",
                "contenido": (
                    "Unidad de análisis: el proceso de contratación pública "
                    "adelantado por una entidad estatal colombiana (y el contrato "
                    "derivado de ese proceso, cuando aplica). Registro: cada fila "
                    "del dataset corresponde a un único proceso/contrato, "
                    "identificado por 'id_del_proceso', con sus atributos asociados "
                    "(entidad, ubicación, modalidad, valor, fechas, proveedor y "
                    "estado). Cuando se incorporan indicadores de nivel global o "
                    "regional agregados (por ejemplo, el indicador de apertura de "
                    "Benchmarking Public Procurement), estos se anexan como columnas "
                    "adicionales al registro mediante las llaves geográfica y "
                    "temporal descritas en el punto 'Dataset', y no como filas "
                    "independientes, para conservar 'un registro = un proceso' como "
                    "unidad de análisis principal."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Variables base tomadas directamente de la API de SECOP II",
                "encabezados": ["Variable (campo API)", "Tipo de dato", "Descripción", "Unidad / dominio", "Grupo de riesgo al que aporta", "Fuente / documentación"],
                "filas": [
                    ["entidad", "Texto", "Nombre de la entidad que publica el proceso", "Catálogo de entidades públicas", "Trazabilidad / Grupo 4", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["nit_entidad", "Texto (identificador)", "NIT de la entidad que publicó el proceso", "NIT colombiano", "Trazabilidad / Grupo 4", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["departamento_entidad", "Categórica / geográfica", "Departamento en el cual está registrada la entidad", "32 departamentos + Bogotá D.C.", "Trazabilidad / Grupo 4 (comparar con departamento_proveedor)", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["ciudad_entidad", "Categórica / geográfica", "Ciudad en la cual está registrada la entidad", "Catálogo DIVIPOLA", "Grupo 4", "https://geoportal.dane.gov.co/laboratorio/codificacion-divipola/"],
                    ["ordenentidad", "Categórica", "Orden de la entidad (Nacional, Regional)", "Nacional / Regional", "Necesidades de información — comparación nacional-regional", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["id_del_proceso", "Texto (identificador)", "Identificador único del proceso, generado por la plataforma", "Código alfanumérico SECOP", "Trazabilidad / llave primaria del registro", "https://community.secop.gov.co/"],
                    ["modalidad_de_contratacion", "Categórica", "Modalidad de selección bajo la cual se desarrolla el proceso", "Licitación pública, contratación directa, mínima cuantía, selección abreviada, concurso de méritos, otras", "Grupo 2", "https://www.colombiacompra.gov.co/"],
                    ["justificaci_n_modalidad_de", "Texto", "Justificación de la modalidad de selección elegida", "Texto libre / puede estar vacío", "Grupo 2 (ausencia de justificación = señal de riesgo)", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["tipo_de_contrato", "Categórica", "Tipo de contrato definido para el proceso", "Catálogo SECOP (obra, consultoría, suministro, etc.)", "Grupo 2", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["codigo_principal_de_categoria", "Categórica", "Código UNSPSC de la categoría principal del bien/servicio", "Catálogo UNSPSC", "Grupo 2 (referencia de precio esperado por categoría)", "https://www.ungm.org/Public/UNSPSC"],
                    ["precio_base", "Numérica (decimal)", "Precio base proyectado del proceso de compra", "Pesos colombianos (COP)", "Grupo 3", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["valor_total_adjudicacion", "Numérica (decimal)", "Valor total adjudicado", "Pesos colombianos (COP)", "Grupo 3 (ratio adjudicado/base)", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["fecha_de_publicacion_del", "Temporal (fecha)", "Fecha de publicación inicial del proceso", "AAAA-MM-DD", "Grupo 3", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["fecha_de_recepcion_de", "Temporal (fecha)", "Fecha asignada para la recepción de respuestas de proveedores", "AAAA-MM-DD", "Grupo 3", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["fecha_de_apertura_efectiva", "Temporal (fecha)", "Fecha real de apertura de las respuestas", "AAAA-MM-DD", "Grupo 3 (comparar con fecha estimada)", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["fecha_adjudicacion", "Temporal (fecha)", "Fecha en la que se adjudicó el proceso al proveedor seleccionado", "AAAA-MM-DD", "Grupo 3 (días entre publicación y adjudicación)", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["duracion", "Numérica (entero)", "Duración estimada del proceso de compra", "Según 'unidad_de_duracion'", "Grupo 3", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["unidad_de_duracion", "Categórica", "Unidad que aplica a la duración estimada", "Días, meses, años", "Grupo 3", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["proveedores_invitados", "Numérica (entero)", "Número total de proveedores invitados a participar", "Entero ≥ 0", "Grupo 1", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["proveedores_con_invitacion", "Numérica (entero)", "Proveedores con invitación directa a participar", "Entero ≥ 0", "Grupo 1", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["proveedores_que_manifestaron", "Numérica (entero)", "Proveedores que manifestaron interés en el proceso", "Entero ≥ 0", "Grupo 1", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["conteo_de_respuestas_a_ofert", "Numérica (entero)", "Número de respuestas hechas de forma directa en las ofertas", "Entero ≥ 0", "Grupo 1", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["proveedores_unicos_con", "Numérica (entero)", "Proveedores únicos que redactaron respuestas en el proceso", "Entero ≥ 0", "Grupo 1 (denominador del ratio de competencia)", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["estado_del_procedimiento", "Categórica", "Estado actual de desarrollo del procedimiento", "Publicado, adjudicado, en ejecución, terminado, cancelado, etc.", "Trazabilidad — filtrado", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["adjudicado", "Categórica (Sí/No)", "Determina si el proceso fue adjudicado", "Sí / No", "Trazabilidad — filtrado", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["nombre_del_adjudicador", "Texto", "Nombre del usuario que ejecutó la acción de adjudicación", "Texto libre", "Grupo 4 (reincidencia adjudicador-proveedor)", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["nombre_del_proveedor", "Texto", "Nombre del proveedor adjudicado", "Texto libre", "Grupo 4", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["nit_del_proveedor_adjudicado", "Texto (identificador)", "NIT del proveedor adjudicado", "NIT colombiano", "Grupo 4 (identificador para medir concentración)", "https://www.rues.org.co/RUP"],
                    ["departamento_proveedor", "Categórica / geográfica", "Departamento en el que está registrado el proveedor adjudicado", "32 departamentos + Bogotá D.C.", "Grupo 4 (comparar con departamento_entidad)", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["ciudad_proveedor", "Categórica / geográfica", "Ciudad en la que está registrado el proveedor adjudicado", "Catálogo DIVIPOLA", "Grupo 4", "https://geoportal.dane.gov.co/laboratorio/codificacion-divipola/"],
                    ["urlproceso", "URL", "Enlace al proceso de compra en la plataforma", "URL válida", "Trazabilidad — verificación puntual", "https://community.secop.gov.co/"],
                ],
            },
            {
                "tipo": "tabla",
                "subtitulo": "Variables derivadas para el análisis de riesgo (calculadas por el equipo, no vienen directas de la API)",
                "encabezados": ["Variable derivada", "Fórmula / regla", "Interpretación de riesgo"],
                "filas": [
                    ["ratio_competencia_real", "proveedores_unicos_con / proveedores_invitados", "Cercano a 0 en procesos formalmente competitivos = posible competencia simulada"],
                    ["ratio_valor_adjudicado_base", "valor_total_adjudicacion / precio_base", "Muy por encima de 1 = posible sobrecosto; muy por debajo = posible oferta artificialmente baja"],
                    ["dias_publicacion_adjudicacion", "fecha_adjudicacion − fecha_de_publicacion_del", "Muy corto frente al promedio de la modalidad = posible direccionamiento del proceso"],
                    ["reincidencia_adjudicador_proveedor", "Conteo de adjudicaciones del mismo 'nombre_del_adjudicador' al mismo 'nit_del_proveedor_adjudicado'", "Valores altos y recurrentes = posible relación irregular"],
                    ["contratacion_directa_sin_justificacion", "modalidad_de_contratacion = 'Contratación directa' y 'justificaci_n_modalidad_de' vacío", "Señal de incumplimiento documental y posible riesgo de direccionamiento"],
                    ["proveedor_fuera_de_region", "departamento_proveedor distinto a departamento_entidad, en montos bajos que no ameritan proveedor foráneo", "Posible indicio de relación previa entidad-proveedor no explicada por especialización técnica"],
                ],
            },
            {
                "tipo": "tabla",
                "subtitulo": "Variables de integración con los niveles regional y global",
                "encabezados": ["Variable", "Tipo de dato", "Descripción", "Dominio", "Fuente de origen", "URL de la fuente"],
                "filas": [
                    ["nivel_comparacion", "Categórica", "Nivel de análisis del registro", "Global, Nacional, Regional", "Construida por el equipo", "—"],
                    ["anio_periodo", "Temporal (año)", "Año de referencia usado para unir un proceso de SECOP con un indicador global/regional del mismo periodo", "AAAA", "Derivada de fecha_de_publicacion_del", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["indicador_apertura_global", "Numérica (índice)", "Indicador de apertura/competencia comparable a nivel país", "Escala del indicador de Benchmarking Public Procurement", "Banco Mundial - Benchmarking Public Procurement", "https://bpp.worldbank.org/en/data/exploreeconomies"],
                ],
            },
            {
                "tipo": "enlaces",
                "subtitulo": "Documentación oficial y diccionarios de datos consultados",
                "lista": [
                    {"texto": "SECOP II — Procesos de Contratación (dataset y diccionario de columnas)", "url": "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"},
                    {"texto": "Codificación DIVIPOLA (DANE) — departamentos y municipios", "url": "https://geoportal.dane.gov.co/laboratorio/codificacion-divipola/"},
                    {"texto": "Catálogo UNSPSC (Naciones Unidas)", "url": "https://www.ungm.org/Public/UNSPSC"},
                    {"texto": "Registro Único de Proponentes (RUP)", "url": "https://www.rues.org.co/RUP"},
                    {"texto": "Colombia Compra Eficiente — normatividad y guías de modalidades de selección", "url": "https://www.colombiacompra.gov.co/"},
                ],
            },
        ],
    },
    {
        "slug": "calidad-inicial-de-los-datos",
        "numero": "07",
        "titulo": "Calidad inicial de los datos",
        "resumen": "Primer diagnóstico de calidad: datos faltantes, duplicados, inconsistencias, etc.",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Resumen del diagnóstico",
                "contenido": (
                    "Este es un diagnóstico preliminar basado en el conocimiento del "
                    "comportamiento habitual de las fuentes utilizadas; los "
                    "porcentajes exactos se calcularán sobre el archivo consolidado "
                    "una vez descargado en su totalidad desde "
                    "https://www.datos.gov.co/resource/p6dx-8zbt.json. Se "
                    "identifican de antemano los siguientes riesgos de calidad, "
                    "característicos de datos administrativos de contratación "
                    "pública: valores faltantes en fechas de terminación de "
                    "contratos aún en ejecución, duplicidad de procesos por adendas "
                    "o republicaciones, inconsistencia en la escritura del nombre de "
                    "una misma entidad (sin estandarizar mayúsculas/tildes), y "
                    "diferencias de granularidad y formato entre la fuente nacional "
                    "y las fuentes globales."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Hallazgos por variable",
                "encabezados": ["Variable", "Tipo de problema", "Problema detectado", "Causa probable", "Acción propuesta", "Fuente donde se verificó"],
                "filas": [
                    ["fecha_fin_ejecucion", "Valores faltantes", "Valores faltantes en procesos activos", "El contrato aún no ha finalizado al momento de la descarga", "Marcar como 'en ejecución' en lugar de imputar una fecha", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["id_del_proceso", "Registros duplicados", "Registros duplicados por adenda o modificación", "SECOP II publica una nueva versión del proceso ante cada modificación", "Conservar solo la versión más reciente por id_del_proceso", "https://community.secop.gov.co/"],
                    ["entidad", "Inconsistencia de formato", "Inconsistencia de formato (mayúsculas, tildes, abreviaturas)", "Digitación manual por parte de cada entidad", "Normalizar texto (minúsculas, sin tildes) y usar catálogo oficial de entidades", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["valor_total_adjudicacion", "Valores fuera de dominio", "Valores en cero, negativos o atípicamente altos frente al resto de su categoría UNSPSC", "Procesos sin oferta económica registrada o errores de digitación", "Marcar como valor no disponible en lugar de eliminar; revisar outliers antes de excluir", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["proveedores_unicos_con", "Valores fuera de dominio", "Valores negativos o mayores a 'proveedores_invitados'", "Errores de captura en el módulo de SECOP II", "Validar contra el rango lógico [0, proveedores_invitados] y marcar como inconsistente si no cumple", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["departamento / municipio", "Diferencias de formato", "Diferencias de codificación entre SECOP y DIVIPOLA (DANE)", "Uso de nombres de texto libre en vez de códigos estandarizados", "Cruzar contra el catálogo DIVIPOLA para unificar nombres", "https://geoportal.dane.gov.co/laboratorio/codificacion-divipola/"],
                    ["moneda / unidad monetaria", "Diferencias de formato", "Diferencia de unidad entre datos nacionales (COP) y globales (USD)", "Cada fuente reporta en su moneda local o de referencia", "Convertir a una unidad común usando tasa de cambio del periodo correspondiente", "https://www.banrep.gov.co/es/estadisticas/trm"],
                    ["nivel_comparacion (integración SECOP–OCDS/Banco Mundial)", "Problema de integración entre fuentes", "Granularidad distinta: SECOP reporta a nivel de proceso individual, mientras OCDS y Benchmarking Public Procurement reportan agregados por país/año", "Diseño metodológico distinto entre fuentes administrativas y fuentes de benchmarking internacional", "Unir por año y país como agregado, no intentar llevar el indicador global al nivel de proceso individual", "https://bpp.worldbank.org/"],
                    ["fecha_de_publicacion_del / fecha_adjudicacion (integración SECOP–Contratación a un Clic)", "Problema de integración entre fuentes", "No siempre existe una llave exacta entre un proceso de SECOP y su referencia en el tablero departamental", "El tablero regional enlaza a SECOP pero no siempre expone el mismo identificador de proceso", "Integrar por combinación de entidad + fecha + valor aproximado cuando no exista el id_del_proceso exacto, documentando el nivel de certeza del cruce", "https://www.cundinamarca.gov.co/web/contratacion"],
                    ["cobertura por entidad", "Sesgo", "Posible sesgo de subregistro en municipios pequeños", "Menor capacidad institucional para publicar oportunamente en SECOP II", "Documentar el sesgo como limitación y evitar comparar municipios con baja tasa de publicación sin ajuste", "https://www.colombiacompra.gov.co/"],
                ],
            },
            {
                "tipo": "texto",
                "subtitulo": "Trazabilidad",
                "contenido": (
                    "Se conservará una copia sin modificar de cada archivo fuente "
                    "descargado (formato original y fecha de descarga), junto con un "
                    "registro de los filtros y transformaciones aplicadas para llegar "
                    "al dataset consolidado, de manera que cualquier resultado pueda "
                    "rastrearse hasta el registro original en SECOP "
                    "(https://community.secop.gov.co/ y "
                    "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt), "
                    "Contratación a un Clic (https://www.cundinamarca.gov.co/web/contratacion), "
                    "OCDS (https://standard.open-contracting.org/latest/en/) o "
                    "Benchmarking Public Procurement (https://bpp.worldbank.org/)."
                ),
            },
        ],
    },
    {
        "slug": "limitaciones-y-consideraciones",
        "numero": "08",
        "titulo": "Limitaciones y consideraciones",
        "resumen": "Restricciones del proyecto y aspectos éticos o técnicos a tener en cuenta.",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Limitaciones",
                "contenido": (
                    "Cobertura temporal: SECOP II inició en 2016 y su adopción por "
                    "parte de las entidades fue gradual, por lo que los primeros años "
                    "tienen menor representatividad; se prioriza 2020-2025.\n"
                    "Cobertura geográfica: no todas las entidades territoriales "
                    "publican con la misma disciplina en SECOP II; algunas pequeñas "
                    "alcaldías aún dependen de SECOP I o de publicación física, lo "
                    "que puede subrepresentar ciertos municipios.\n"
                    "Comparabilidad global: los indicadores de Benchmarking Public "
                    "Procurement y OCDS están agregados a nivel de país/año, con un "
                    "nivel de granularidad mucho menor que los datos de SECOP a nivel "
                    "de proceso, por lo que la comparación global se hará "
                    "principalmente a nivel de indicadores agregados, no de "
                    "registros individuales.\n"
                    "Recursos técnicos: el volumen histórico de SECOP II es de gran "
                    "tamaño, por lo que la descarga y el procesamiento se realizan "
                    "mediante muestreo filtrado por departamento y periodo, no sobre "
                    "la totalidad histórica de la plataforma."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Consideraciones éticas y de privacidad",
                "contenido": (
                    "El dataset incluye identificación de proveedores (NIT, razón "
                    "social) y, en algunos casos, de contratistas personas naturales, "
                    "lo cual constituye un dato de carácter público según la Ley 1712 "
                    "de 2014 (Transparencia y Acceso a la Información Pública), pero "
                    "su tratamiento debe respetar los principios de la Ley 1581 de "
                    "2012 (protección de datos personales) cuando se trate de "
                    "personas naturales. El equipo se compromete a: (1) usar la "
                    "información únicamente con fines académicos y analíticos, (2) "
                    "evitar publicar conclusiones que señalen individualmente a una "
                    "persona natural o entidad como responsable de una irregularidad "
                    "sin el debido soporte estadístico, y (3) documentar que la "
                    "presencia de patrones atípicos (por ejemplo, alta concentración "
                    "de contratos en un proveedor) es un indicio para análisis "
                    "posterior y no una acusación de corrupción o ilegalidad."
                ),
            },
            {
                "tipo": "enlaces",
                "subtitulo": "Marco normativo consultado",
                "lista": [
                    {"texto": "Ley 1712 de 2014 — Transparencia y Acceso a la Información Pública", "url": "https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=56882"},
                    {"texto": "Ley 1581 de 2012 — Protección de Datos Personales", "url": "https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=49981"},
                ],
            },
        ],
    },
]

