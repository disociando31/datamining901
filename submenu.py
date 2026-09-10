

# Submens de la Etapa 1.
SUBMENUS_ETAPA_1 = [
    {
        "slug": "problema-y-contexto",
        "numero": "01",
        "titulo": "Problema y contexto",
        "resumen": "DescripciÃ³n del problema que se aborda y el entorno en el que ocurre.",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Contexto general",
                "contenido": (
                    "La contrataciÃ³n pÃºblica es el mecanismo mediante el cual los "
                    "gobiernos adquieren bienes, servicios y obras usando recursos "
                    "pÃºblicos. Representa entre el 12% y el 20% del PIB en la mayorÃ­a "
                    "de paÃ­ses (OCDE), lo que la convierte en un Ã¡rea crÃ­tica para la "
                    "eficiencia del gasto, la transparencia y la lucha contra la "
                    "corrupciÃ³n. A nivel global, iniciativas como el Open Contracting "
                    "Data Standard (OCDS) buscan estandarizar y abrir estos datos. En "
                    "Colombia, la plataforma SECOP (Sistema ElectrÃ³nico de "
                    "ContrataciÃ³n PÃºblica) centraliza los procesos de contrataciÃ³n "
                    "estatal, generando grandes volÃºmenes de datos susceptibles de "
                    "anÃ¡lisis."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "DescripciÃ³n del problema",
                "contenido": (
                    "Existe una asimetrÃ­a entre el volumen de datos abiertos de "
                    "contrataciÃ³n pÃºblica disponibles y su uso efectivo para "
                    "identificar patrones de riesgo, ineficiencia o irregularidad en "
                    "la asignaciÃ³n de recursos pÃºblicos. Muchas entidades "
                    "territoriales no cuentan con herramientas analÃ­ticas que les "
                    "permitan comparar su desempeÃ±o contractual frente a estÃ¡ndares "
                    "nacionales o internacionales, ni detectar anomalÃ­as (sobrecostos, "
                    "concentraciÃ³n de proveedores, retrasos, modalidades de "
                    "contrataciÃ³n atÃ­picas)."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "AnÃ¡lisis por niveles",
                "contenido": (
                    "Global: estÃ¡ndares de datos abiertos de contrataciÃ³n (OCDS), "
                    "Ã­ndices de transparencia (Open Contracting Partnership, Banco "
                    "Mundial - Procurement) y comparaciÃ³n entre paÃ­ses en eficiencia "
                    "y riesgo de corrupciÃ³n en compras pÃºblicas.\n\n"
                    "Nacional (Colombia): datos de SECOP I y II, Colombia Compra "
                    "Eficiente, anÃ¡lisis de modalidades de contrataciÃ³n, entidades "
                    "contratantes, montos y proveedores frecuentes.\n\n"
                    "Regional: comportamiento contractual por departamento/municipio "
                    "(concentraciÃ³n de contratos, entidades con mayor gasto, "
                    "disparidades regionales en ejecuciÃ³n de recursos), tomando "
                    "Cundinamarca como departamento de referencia."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "JustificaciÃ³n",
                "contenido": (
                    "Identificar patrones y factores de riesgo en la contrataciÃ³n "
                    "pÃºblica permite fortalecer la transparencia, optimizar el uso de "
                    "recursos pÃºblicos y generar alertas tempranas frente a posibles "
                    "irregularidades. El impacto potencial abarca desde el diseÃ±o de "
                    "polÃ­ticas pÃºblicas hasta el desarrollo de herramientas de "
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
                    "Â¿QuÃ© patrones y factores de riesgo se pueden identificar en los "
                    "procesos de contrataciÃ³n pÃºblica mediante tÃ©cnicas de minerÃ­a "
                    "de datos?"
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Preguntas secundarias",
                "contenido": (
                    "1. Â¿CuÃ¡les son las modalidades de contrataciÃ³n mÃ¡s utilizadas en "
                    "Colombia y cÃ³mo varÃ­an entre departamentos/regiones?\n"
                    "2. Â¿Existe concentraciÃ³n de contratos en un nÃºmero reducido de "
                    "proveedores (posible indicador de riesgo de corrupciÃ³n o falta "
                    "de competencia)?\n"
                    "3. Â¿QuÃ© relaciÃ³n existe entre el monto de los contratos, el tipo "
                    "de entidad contratante y el tiempo de ejecuciÃ³n o retrasos?\n"
                    "4. Â¿CÃ³mo se compara el nivel de apertura y estandarizaciÃ³n de "
                    "los datos de contrataciÃ³n colombianos frente a los estÃ¡ndares "
                    "globales (OCDS)?\n"
                    "5. Â¿QuÃ© sectores (salud, infraestructura, educaciÃ³n, etc.) "
                    "concentran mayor volumen de recursos y cÃ³mo ha evolucionado "
                    "esto en el tiempo?"
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Conocimiento esperado",
                "contenido": (
                    "Se espera identificar patrones de concentraciÃ³n de proveedores y "
                    "entidades (clustering), anomalÃ­as o outliers en montos y plazos "
                    "que sugieran riesgo (detecciÃ³n de anomalÃ­as), relaciones entre "
                    "variables como tipo de entidad, sector, modalidad y monto "
                    "(asociaciÃ³n/correlaciÃ³n), tendencias temporales en el gasto "
                    "pÃºblico por sector y regiÃ³n, y comparativos entre el desempeÃ±o "
                    "de Colombia y estÃ¡ndares/benchmarks globales, asÃ­ como entre "
                    "regiones dentro del paÃ­s."
                ),
            },
        ],
    },
    {
        "slug": "necesidades-de-informacion",
        "numero": "03",
        "titulo": "Necesidades de informaciÃ³n",
        "resumen": "QuÃ© informaciÃ³n se necesita recolectar para responder las preguntas planteadas.",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Entidades involucradas",
                "contenido": (
                    "Colombia Compra Eficiente (ANCP-CCE), entidad rectora del "
                    "sistema de compra pÃºblica y administradora de SECOP I y SECOP "
                    "II. Entidades estatales contratantes de los tres niveles "
                    "(nacional, departamental y municipal), en particular la "
                    "GobernaciÃ³n de Cundinamarca y sus dependencias. Proveedores y "
                    "contratistas registrados en el Registro Ãšnico de Proponentes "
                    "(RUP). A nivel global, Open Contracting Partnership (OCP), "
                    "responsable del estÃ¡ndar OCDS, y el Banco Mundial, a travÃ©s de "
                    "su iniciativa Benchmarking Public Procurement, que compara la "
                    "regulaciÃ³n y desempeÃ±o de la contrataciÃ³n pÃºblica entre paÃ­ses."
                ),
            },
            {
                "tipo": "enlaces",
                "subtitulo": "Enlaces de las entidades involucradas",
                "lista": [
                    {"texto": "Colombia Compra Eficiente (ANCP-CCE)", "url": "https://www.colombiacompra.gov.co/"},
                    {"texto": "SECOP I - Consulta de procesos", "url": "https://www.contratos.gov.co/consultas/inicioConsulta.do"},
                    {"texto": "SECOP II - Portal transaccional", "url": "https://community.secop.gov.co/"},
                    {"texto": "Registro Ãšnico de Proponentes (RUP) - CÃ¡mara de Comercio", "url": "https://www.rues.org.co/RUP"},
                    {"texto": "GobernaciÃ³n de Cundinamarca", "url": "https://www.cundinamarca.gov.co/"},
                    {"texto": "Open Contracting Partnership (OCP)", "url": "https://www.open-contracting.org/"},
                    {"texto": "Open Contracting Data Standard (OCDS)", "url": "https://standard.open-contracting.org/latest/en/"},
                    {"texto": "Banco Mundial - Benchmarking Public Procurement", "url": "https://bpp.worldbank.org/"},
                ],
            },
            {
                "tipo": "texto",
                "subtitulo": "Variables relevantes y su justificaciÃ³n (nombres reales de la API SECOP II)",
                "contenido": (
                    "Las variables se agrupan segÃºn el tipo de patrÃ³n de riesgo/fraude "
                    "que permiten detectar, usando los nombres de campo reales de la "
                    "API de SECOP II (ver diccionario de datos oficial, disponible en "
                    "el portal de datos.gov.co, secciÃ³n 'InformaciÃ³n Adicional' del "
                    "conjunto de datos SECOP II â€” Procesos de ContrataciÃ³n):\n\n"
                    "Grupo 1 â€” Competencia simulada o insuficiente (indicador central "
                    "de riesgo de colusiÃ³n): 'proveedores_invitados', "
                    "'proveedores_con_invitacion' (directa), "
                    "'proveedores_que_manifestaron' (interÃ©s), "
                    "'respuestas_al_procedimiento', 'respuestas_externas', "
                    "'conteo_de_respuestas_a_ofert' (as), 'proveedores_unicos_con' "
                    "(respuestas). Con estas se calcula un ratio de competencia real "
                    "(respuestas Ãºnicas / invitados); un proceso formalmente "
                    "competitivo con un solo oferente efectivo es la seÃ±al de riesgo "
                    "mÃ¡s documentada en la literatura de contrataciÃ³n pÃºblica.\n\n"
                    "Grupo 2 â€” Uso atÃ­pico de la modalidad de contrataciÃ³n: "
                    "'modalidad_de_contratacion', 'justificaci_n_modalidad_de', "
                    "'tipo_de_contrato', 'subtipo_de_contrato', "
                    "'codigo_principal_de_categoria' (UNSPSC). Permiten detectar si "
                    "una entidad usa contrataciÃ³n directa muy por encima de lo "
                    "esperado para su categorÃ­a de compra, o sin justificaciÃ³n "
                    "registrada.\n\n"
                    "Grupo 3 â€” AnomalÃ­as de tiempo y de valor: 'precio_base' y "
                    "'valor_total_adjudicacion' (ratio adjudicado/base, para detectar "
                    "sobreprecio o precios sospechosamente bajos); "
                    "'fecha_de_publicacion_del', 'fecha_de_recepcion_de' "
                    "(respuestas), 'fecha_de_apertura_de_respuesta', "
                    "'fecha_de_apertura_efectiva', 'fecha_adjudicacion', 'duracion' y "
                    "'unidad_de_duracion'. Con las fechas se calcula el nÃºmero de "
                    "dÃ­as entre publicaciÃ³n y adjudicaciÃ³n: plazos anormalmente "
                    "cortos reducen la posibilidad real de que otros proveedores "
                    "compitan.\n\n"
                    "Grupo 4 â€” ConcentraciÃ³n y relaciones entidad-proveedor-"
                    "adjudicador (posible colusiÃ³n o direccionamiento): 'entidad', "
                    "'nit_entidad', 'nombre_del_adjudicador', 'nombre_del_proveedor', "
                    "'nit_del_proveedor_adjudicado', 'departamento_proveedor' y "
                    "'ciudad_proveedor' comparados contra 'departamento_entidad' y "
                    "'ciudad_entidad'. Permiten construir una red entidadâ†’"
                    "adjudicadorâ†’proveedor y medir reincidencia (mismo adjudicador "
                    "favoreciendo repetidamente al mismo proveedor) o contratos "
                    "adjudicados a proveedores fuera de su regiÃ³n de forma atÃ­pica.\n\n"
                    "Variables de trazabilidad y filtrado (no son indicador de "
                    "riesgo por sÃ­ mismas, pero son obligatorias para poder unir, "
                    "depurar y comparar): 'id_del_proceso', 'referencia_del_proceso', "
                    "'urlproceso', 'codigo_entidad', 'departamento_entidad', "
                    "'ciudad_entidad', 'ordenentidad' (Nacional/Regional), "
                    "'estado_del_procedimiento', 'estado_resumen' y 'adjudicado'.\n\n"
                    "Variables descartadas por bajo valor analÃ­tico para este "
                    "objetivo (no se incluyen en el dataset consolidado, o se dejan "
                    "como opcionales): 'descripcion_del_procedimiento' (texto libre, "
                    "solo Ãºtil si se hace minerÃ­a de texto en una etapa posterior), "
                    "'ppi', 'id_del_portafolio', 'categorias_adicionales', "
                    "'numero_de_lotes' y 'visualizaciones_del_procedimiento' (mide "
                    "interÃ©s pÃºblico, no riesgo de contrataciÃ³n)."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Periodo de anÃ¡lisis",
                "contenido": (
                    "Se tomarÃ¡ como periodo de anÃ¡lisis 2020-2025 para SECOP II, por "
                    "ser el rango en el que la plataforma transaccional ya cuenta con "
                    "una adopciÃ³n amplia y estable por parte de las entidades "
                    "estatales, lo cual reduce el sesgo de subregistro propio de los "
                    "primeros aÃ±os de la plataforma (lanzada en 2016). Para los "
                    "indicadores globales de referencia se usarÃ¡ la Ãºltima "
                    "publicaciÃ³n disponible de cada fuente."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Cobertura geogrÃ¡fica",
                "contenido": (
                    "Global: muestra de paÃ­ses incluidos en OCDS/Benchmarking Public "
                    "Procurement, usados como referencia comparativa.\n"
                    "Nacional: todo el territorio colombiano (32 departamentos y "
                    "BogotÃ¡ D.C.), segÃºn registro de SECOP I y II.\n"
                    "Regional: departamento de Cundinamarca y sus municipios, tomado "
                    "como caso de estudio regional."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "PoblaciÃ³n / unidad de anÃ¡lisis y granularidad",
                "contenido": (
                    "La unidad de anÃ¡lisis principal es el proceso de contrataciÃ³n "
                    "(y, cuando aplica, el contrato derivado de dicho proceso), "
                    "publicado por una entidad estatal colombiana. Se trabajarÃ¡ con "
                    "granularidad a nivel de proceso individual (no agregados "
                    "mensuales o anuales), lo que permite luego construir agregados "
                    "propios por entidad, sector, modalidad, departamento o periodo "
                    "segÃºn se requiera en el anÃ¡lisis, evitando partir de datos ya "
                    "agregados que limiten el detalle del estudio."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Variables para comparar escalas global-nacional-regional",
                "contenido": (
                    "Para permitir la comparaciÃ³n entre niveles se estandarizarÃ¡n al "
                    "menos las siguientes variables comunes: (1) monto contratado, "
                    "normalizado a USD o como porcentaje del gasto total del periodo, "
                    "para comparar magnitudes entre paÃ­s/departamento; (2) sector u "
                    "objeto del contrato, mapeado a una clasificaciÃ³n comÃºn de tipo "
                    "CPV/CPC; (3) aÃ±o/periodo de referencia, para alinear series de "
                    "tiempo entre fuentes con distinta frecuencia de publicaciÃ³n; y "
                    "(4) un indicador de nivel de apertura/competencia (por ejemplo, "
                    "nÃºmero de oferentes o modalidad con/sin pluralidad de "
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
        "resumen": "Origen de los datos utilizados: de dÃ³nde provienen y cÃ³mo se obtuvieron.",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Criterio de clasificaciÃ³n",
                "contenido": (
                    "Se documentan al menos dos fuentes por nivel (global, nacional y "
                    "regional), procurando que en conjunto queden representados los "
                    "tres tipos de fuente exigidos: primarias (registro directo del "
                    "proceso de contrataciÃ³n hecho por la propia entidad), "
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
                "subtitulo": "Nivel Nacional â€” Colombia",
                "encabezados": ["Campo", "Fuente 1", "Fuente 2", "Fuente 3"],
                "filas": [
                    ["Nombre", "Consulta de procesos SECOP I (detalleProceso)", "SECOP II - Procesos de ContrataciÃ³n", "Portal de Datos Abiertos del Estado Colombiano"],
                    ["InstituciÃ³n responsable", "Colombia Compra Eficiente (ANCP-CCE)", "Colombia Compra Eficiente (ANCP-CCE)", "MinTIC / ANCP-CCE"],
                    ["URL", "https://www.contratos.gov.co/consultas/inicioConsulta.do", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt", "https://www.datos.gov.co/"],
                    ["Tipo de fuente", "Primaria", "Secundaria", "Terciaria"],
                    ["Cobertura geogrÃ¡fica", "Nacional (todas las entidades registradas)", "Nacional", "Nacional"],
                    ["Periodo disponible", "HistÃ³rico por proceso, variable segÃºn entidad", "2016 (lanzamiento SECOP II) a la fecha", "Depende de cada conjunto de datos publicado"],
                    ["Formato", "Consulta web individual (HTML por proceso)", "CSV / JSON vÃ­a API Socrata (SODA)", "CSV / JSON / API Socrata"],
                    ["MÃ©todo de adquisiciÃ³n", "Consulta manual proceso por proceso mediante nÃºmero de constancia", "Descarga masiva o consulta a la API pÃºblica (endpoint /resource)", "Descarga desde el catÃ¡logo del portal"],
                    ["NÂº aprox. de registros", "1 (por consulta); se usa como verificaciÃ³n puntual, no como fuente masiva", "Del orden de varios millones de procesos acumulados desde 2016 (cifra exacta a validar al momento de la descarga)", "Cientos de conjuntos de datos de contrataciÃ³n disponibles"],
                    ["Variables disponibles", "Entidad, objeto, modalidad, valor, proveedor, fechas, estado, documentos del proceso", "entidad, nit_entidad, departamento, ciudad, orden, sector, modalidad_de_contratacion, tipo_de_contrato, precio_base, valor_del_contrato, fecha_de_firma, fecha_de_inicio, fecha_de_fin, estado_del_procedimiento, proveedor_adjudicado, nit_proveedor, urlproceso", "Metadatos de cada conjunto: nombre, entidad publicadora, columnas, frecuencia de actualizaciÃ³n"],
                    ["Fecha de consulta", "Agosto de 2026", "Agosto de 2026", "Agosto de 2026"],
                    ["Restricciones de uso", "Uso pÃºblico, sujeto a Ley 1712 de 2014 (transparencia); no permite descarga masiva automatizada", "Datos abiertos, licencia de datos abiertos de Colombia (uso libre citando la fuente)", "Licencia de datos abiertos de Colombia"],
                    ["Enlace directo de consulta / API", "https://www.contratos.gov.co/consultas/inicioConsulta.do", "https://www.datos.gov.co/resource/p6dx-8zbt.json (endpoint API Socrata)", "https://www.datos.gov.co/browse?category=Gastos+Gubernamentales"],
                ],
            },
            {
                "tipo": "enlaces",
                "subtitulo": "Referencias â€” Nivel Nacional",
                "lista": [
                    {"texto": "SECOP I â€” Consulta de procesos (contratos.gov.co)", "url": "https://www.contratos.gov.co/consultas/inicioConsulta.do"},
                    {"texto": "SECOP II â€” Procesos de ContrataciÃ³n (datos.gov.co, dataset p6dx-8zbt)", "url": "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"},
                    {"texto": "API Socrata (SODA) del dataset SECOP II", "url": "https://www.datos.gov.co/resource/p6dx-8zbt.json"},
                    {"texto": "Portal de Datos Abiertos del Estado Colombiano", "url": "https://www.datos.gov.co/"},
                    {"texto": "Colombia Compra Eficiente â€” sitio institucional", "url": "https://www.colombiacompra.gov.co/"},
                    {"texto": "Ley 1712 de 2014 (Transparencia y Acceso a la InformaciÃ³n PÃºblica)", "url": "https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=56882"},
                ],
            },
            {
                "tipo": "texto",
                "subtitulo": "JustificaciÃ³n â€” Nivel Nacional",
                "contenido": (
                    "Pertinencia: SECOP II es la fuente oficial y mÃ¡s granular de "
                    "procesos de contrataciÃ³n en Colombia, y es la Ãºnica que permite "
                    "responder directamente las preguntas sobre modalidades, montos, "
                    "proveedores y retrasos planteadas en el punto 2. Confiabilidad: "
                    "es administrada por Colombia Compra Eficiente, entidad rectora "
                    "del sistema de compra pÃºblica, con obligaciÃ³n legal de "
                    "publicaciÃ³n (Ley 1712 de 2014), lo que reduce el riesgo de datos "
                    "manipulados, aunque no elimina errores de digitaciÃ³n de cada "
                    "entidad. Actualidad: los datos se publican en tiempo real a "
                    "medida que las entidades gestionan sus procesos. Cobertura: "
                    "incluye, en principio, a todas las entidades estatales "
                    "obligadas a contratar por SECOP II, cubriendo el territorio "
                    "nacional; el uso de la consulta puntual en contratos.gov.co y "
                    "del catÃ¡logo de datos.gov.co permite ademÃ¡s verificar y "
                    "contrastar registros individuales frente al conjunto masivo."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Nivel Regional â€” Cundinamarca",
                "encabezados": ["Campo", "Fuente 1", "Fuente 2"],
                "filas": [
                    ["Nombre", "ContrataciÃ³n a un Clic", "Planes Anuales de Adquisiciones (PAA) de la GobernaciÃ³n"],
                    ["InstituciÃ³n responsable", "GobernaciÃ³n de Cundinamarca", "GobernaciÃ³n de Cundinamarca (dependencias del sector central)"],
                    ["URL", "https://www.cundinamarca.gov.co/web/contratacion", "https://www.cundinamarca.gov.co/web/transparencia/planeacion/planes-anuales-de-adquisiciones"],
                    ["Tipo de fuente", "Terciaria", "Primaria"],
                    ["Cobertura geogrÃ¡fica", "Departamento de Cundinamarca", "Departamento de Cundinamarca"],
                    ["Periodo disponible", "Vigencias publicadas por la GobernaciÃ³n (Ãºltimos aÃ±os)", "Vigencia fiscal en curso y anteriores publicadas"],
                    ["Formato", "Tablero web / enlaces a SECOP", "PDF / Excel"],
                    ["MÃ©todo de adquisiciÃ³n", "Consulta en lÃ­nea del tablero de contrataciÃ³n departamental", "Descarga directa de los documentos publicados"],
                    ["NÂº aprox. de registros", "Variable segÃºn vigencia y dependencia consultada", "Decenas a cientos de Ã­tems de adquisiciÃ³n planeada por vigencia"],
                    ["Variables disponibles", "Dependencia, proceso, estado, enlace a SECOP, valor estimado", "Objeto a contratar, valor estimado, modalidad prevista, fecha estimada de inicio, dependencia"],
                    ["Fecha de consulta", "Agosto de 2026", "Agosto de 2026"],
                    ["Restricciones de uso", "Uso pÃºblico, informaciÃ³n de carÃ¡cter informativo/consulta", "Uso pÃºblico bajo Ley 1712 de 2014"],
                    ["Enlace directo de consulta", "https://www.cundinamarca.gov.co/web/contratacion", "https://www.cundinamarca.gov.co/web/transparencia/planeacion/planes-anuales-de-adquisiciones"],
                ],
            },
            {
                "tipo": "enlaces",
                "subtitulo": "Referencias â€” Nivel Regional",
                "lista": [
                    {"texto": "GobernaciÃ³n de Cundinamarca â€” Portal institucional", "url": "https://www.cundinamarca.gov.co/"},
                    {"texto": "ContrataciÃ³n a un Clic â€” Cundinamarca", "url": "https://www.cundinamarca.gov.co/web/contratacion"},
                    {"texto": "Planes Anuales de Adquisiciones â€” Transparencia Cundinamarca", "url": "https://www.cundinamarca.gov.co/web/transparencia/planeacion/planes-anuales-de-adquisiciones"},
                ],
            },
            {
                "tipo": "texto",
                "subtitulo": "JustificaciÃ³n â€” Nivel Regional",
                "contenido": (
                    "Pertinencia: Cundinamarca se toma como caso de estudio regional "
                    "porque rodea a BogotÃ¡ y agrupa municipios con capacidades "
                    "institucionales muy distintas, lo que la hace representativa "
                    "para observar disparidades regionales en la ejecuciÃ³n de "
                    "recursos. Confiabilidad: ambas fuentes son publicadas "
                    "directamente por la GobernaciÃ³n, aunque ContrataciÃ³n a un Clic "
                    "depende de que cada dependencia mantenga actualizado el "
                    "tablero, por lo que se usarÃ¡ principalmente como punto de "
                    "verificaciÃ³n y enlace hacia SECOP, no como fuente masiva. "
                    "Actualidad: los Planes Anuales de Adquisiciones se publican por "
                    "vigencia fiscal y se actualizan ante modificaciones. Cobertura: "
                    "cubre el sector central del departamento; no incluye "
                    "necesariamente a todos los municipios ni a entidades "
                    "descentralizadas, lo cual se documenta como limitaciÃ³n en el "
                    "punto 8."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Nivel Global",
                "encabezados": ["Campo", "Fuente 1", "Fuente 2"],
                "filas": [
                    ["Nombre", "Open Contracting Data Standard (OCDS) / Open Contracting Partnership", "Benchmarking Public Procurement (Banco Mundial)"],
                    ["InstituciÃ³n responsable", "Open Contracting Partnership (OCP)", "Banco Mundial (World Bank Group)"],
                    ["URL", "https://standard.open-contracting.org/latest/en/", "https://bpp.worldbank.org/"],
                    ["Tipo de fuente", "Secundaria", "Secundaria"],
                    ["Cobertura geogrÃ¡fica", "MÃºltiples paÃ­ses que publican en formato OCDS", "MÃ¡s de 180 economÃ­as"],
                    ["Periodo disponible", "Depende de cada paÃ­s publicador", "Reportes periÃ³dicos (ediciones anuales/bienales)"],
                    ["Formato", "JSON estandarizado (esquema OCDS)", "Reportes e indicadores tabulares (PDF/Excel)"],
                    ["MÃ©todo de adquisiciÃ³n", "Descarga de paquetes OCDS publicados por cada paÃ­s", "Descarga de indicadores del reporte pÃºblico"],
                    ["NÂº aprox. de registros", "Variable por paÃ­s (miles a millones de procesos publicados en formato abierto)", "1 indicador por paÃ­s/ediciÃ³n, agregable por aÃ±o"],
                    ["Variables disponibles", "Comprador, proveedor, valor, fechas, Ã­tems, modalidad (esquema comÃºn OCDS)", "Ã�ndice de regulaciÃ³n, tiempo de trÃ¡mite, transparencia, uso de e-procurement, por paÃ­s"],
                    ["Fecha de consulta", "Agosto de 2026", "Agosto de 2026"],
                    ["Restricciones de uso", "Datos abiertos, licencia Open Data Commons", "Uso pÃºblico con atribuciÃ³n al Banco Mundial"],
                    ["Enlace directo de consulta", "https://www.open-contracting.org/data/", "https://bpp.worldbank.org/en/data/exploreeconomies"],
                ],
            },
            {
                "tipo": "enlaces",
                "subtitulo": "Referencias â€” Nivel Global",
                "lista": [
                    {"texto": "Open Contracting Partnership â€” sitio institucional", "url": "https://www.open-contracting.org/"},
                    {"texto": "Open Contracting Data Standard (OCDS) â€” documentaciÃ³n del esquema", "url": "https://standard.open-contracting.org/latest/en/"},
                    {"texto": "OCP â€” Explorador de datos publicados por paÃ­s", "url": "https://www.open-contracting.org/data/"},
                    {"texto": "Banco Mundial â€” Benchmarking Public Procurement (portal principal)", "url": "https://bpp.worldbank.org/"},
                    {"texto": "Banco Mundial â€” Explorar economÃ­as (indicadores por paÃ­s)", "url": "https://bpp.worldbank.org/en/data/exploreeconomies"},
                ],
            },
            {
                "tipo": "texto",
                "subtitulo": "JustificaciÃ³n â€” Nivel Global",
                "contenido": (
                    "Pertinencia: OCDS y Benchmarking Public Procurement son las "
                    "referencias estÃ¡ndar de facto para comparar contrataciÃ³n "
                    "pÃºblica entre paÃ­ses, lo que permite responder la pregunta "
                    "secundaria sobre el nivel de apertura de Colombia frente a "
                    "estÃ¡ndares globales. Confiabilidad: son mantenidas por "
                    "organizaciones internacionales (Open Contracting Partnership y "
                    "Banco Mundial) con metodologÃ­as pÃºblicas y auditables. "
                    "Actualidad: OCDS depende de la frecuencia de publicaciÃ³n de "
                    "cada paÃ­s; Benchmarking Public Procurement se actualiza por "
                    "ediciones periÃ³dicas del Banco Mundial. Cobertura: amplia a "
                    "nivel de paÃ­ses, pero con una granularidad mucho menor "
                    "(indicadores agregados por paÃ­s/aÃ±o) que las fuentes "
                    "nacionales y regionales, lo cual se documenta como limitaciÃ³n "
                    "de comparabilidad en el punto 8."
                ),
            },
        ],
    },
    {
        "slug": "dataset",
        "numero": "05",
        "titulo": "Dataset",
        "resumen": "DescripciÃ³n general del conjunto de datos final utilizado en el proyecto.",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Estado actual",
                "contenido": (
                    "En esta etapa se define el diseÃ±o del dataset consolidado, "
                    "construido principalmente a partir de SECOP II (nivel "
                    "nacional/regional), complementado con el tablero de "
                    "ContrataciÃ³n a un Clic y los Planes Anuales de Adquisiciones de "
                    "Cundinamarca (nivel regional) y con los indicadores de OCDS y "
                    "Benchmarking Public Procurement (nivel global). La construcciÃ³n "
                    "definitiva del archivo consolidado (mÃ­nimo 10.000 registros) se "
                    "realiza mediante descarga vÃ­a API de SECOP II "
                    "(https://www.datos.gov.co/resource/p6dx-8zbt.json), filtrando "
                    "por departamento y fecha, integrando despuÃ©s las variables "
                    "comparativas de nivel global y regional descritas en la secciÃ³n "
                    "de necesidades de informaciÃ³n."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Estrategia de integraciÃ³n",
                "contenido": (
                    "La integraciÃ³n entre niveles se realiza mediante dos llaves "
                    "comunes: geogrÃ¡fica (paÃ­s / departamento / municipio, "
                    "normalizados a un mismo catÃ¡logo de nombres) y temporal (aÃ±o de "
                    "publicaciÃ³n o firma del proceso). A cada registro nacional o "
                    "regional se le aÃ±ade una columna de 'nivel_comparacion' que "
                    "permite unir, en el anÃ¡lisis, un proceso puntual de SECOP con el "
                    "indicador global o departamental del mismo periodo."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Estructura prevista del dataset consolidado (muestra ilustrativa, nombres reales de campo SECOP II)",
                "encabezados": ["id_del_proceso", "departamento_entidad", "modalidad_de_contratacion", "precio_base", "valor_total_adjudicacion", "proveedores_invitados", "proveedores_unicos_con", "fecha_de_publicacion_del", "fecha_adjudicacion", "nit_del_proveedor_adjudicado", "nivel_comparacion", "urlproceso"],
                "filas": [
                    ["CO1.PCCNTR.001", "Cundinamarca", "ContrataciÃ³n directa", "185000000", "185000000", "1", "1", "2024-03-01", "2024-03-15", "900123456-1", "Regional", "https://community.secop.gov.co/Public/Tendering/OpportunityDetail/Index?noticeUID=CO1.PCCNTR.001"],
                    ["CO1.PCCNTR.002", "BogotÃ¡ D.C.", "LicitaciÃ³n pÃºblica", "3000000000", "3200000000", "8", "5", "2023-05-10", "2023-07-02", "800987654-2", "Nacional", "https://community.secop.gov.co/Public/Tendering/OpportunityDetail/Index?noticeUID=CO1.PCCNTR.002"],
                    ["CO1.PCCNTR.003", "Antioquia", "MÃ­nima cuantÃ­a", "12000000", "12500000", "3", "2", "2024-11-05", "2024-11-20", "901234567-3", "Nacional", "https://community.secop.gov.co/Public/Tendering/OpportunityDetail/Index?noticeUID=CO1.PCCNTR.003"],
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
                "subtitulo": "Cumplimiento de requisitos mÃ­nimos",
                "contenido": (
                    "El diseÃ±o garantiza al menos 10 variables, con variables "
                    "numÃ©ricas ('precio_base', 'valor_total_adjudicacion', "
                    "'proveedores_invitados', 'proveedores_unicos_con'), variables "
                    "categÃ³ricas ('departamento_entidad', 'modalidad_de_contratacion', "
                    "'estado_del_procedimiento'), variable temporal "
                    "('fecha_de_publicacion_del' / 'fecha_adjudicacion') y variable "
                    "geogrÃ¡fica ('departamento_entidad' / 'departamento_proveedor'), "
                    "ademÃ¡s del indicador derivado 'nivel_comparacion' "
                    "(global/nacional/regional) que permite filtrar y comparar las "
                    "tres escalas exigidas por el proyecto. El volumen meta de "
                    "10.000 registros se cubre principalmente con procesos de "
                    "SECOP II, dado que es la fuente con mayor granularidad y "
                    "volumen disponible."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Potencial para minerÃ­a de datos",
                "contenido": (
                    "La estructura del dataset se diseÃ±Ã³ pensando en las tÃ©cnicas que "
                    "se aplicarÃ¡n en etapas posteriores: 'ratio_valor_adjudicado_base' "
                    "y 'ratio_competencia_real' permiten detecciÃ³n de anomalÃ­as "
                    "(outliers que sugieran sobrecostos o baja competencia); "
                    "'nombre_del_adjudicador', 'nit_del_proveedor_adjudicado' y "
                    "'valor_total_adjudicacion' permiten clustering y anÃ¡lisis de "
                    "redes para identificar concentraciÃ³n y reincidencia; "
                    "'modalidad_de_contratacion', 'codigo_principal_de_categoria' y "
                    "'estado_del_procedimiento' permiten reglas de asociaciÃ³n entre "
                    "tipo de proceso y resultado; y 'fecha_de_publicacion_del'/"
                    "'fecha_adjudicacion' junto con 'duracion' permiten anÃ¡lisis de "
                    "series de tiempo y modelos predictivos de retrasos. La columna "
                    "derivada 'nivel_comparacion' es la que habilita, de forma "
                    "transversal, la comparaciÃ³n global-nacional-regional exigida en "
                    "el problema de investigaciÃ³n."
                ),
            },
        ],
    },
    {
        "slug": "diccionario-de-datos",
        "numero": "06",
        "titulo": "Diccionario de datos",
        "resumen": "DefiniciÃ³n de cada variable del dataset: nombre, tipo de dato y significado.",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Unidad de anÃ¡lisis y registro",
                "contenido": (
                    "Unidad de anÃ¡lisis: el proceso de contrataciÃ³n pÃºblica "
                    "adelantado por una entidad estatal colombiana (y el contrato "
                    "derivado de ese proceso, cuando aplica). Registro: cada fila "
                    "del dataset corresponde a un Ãºnico proceso/contrato, "
                    "identificado por 'id_del_proceso', con sus atributos asociados "
                    "(entidad, ubicaciÃ³n, modalidad, valor, fechas, proveedor y "
                    "estado). Cuando se incorporan indicadores de nivel global o "
                    "regional agregados (por ejemplo, el indicador de apertura de "
                    "Benchmarking Public Procurement), estos se anexan como columnas "
                    "adicionales al registro mediante las llaves geogrÃ¡fica y "
                    "temporal descritas en el punto 'Dataset', y no como filas "
                    "independientes, para conservar 'un registro = un proceso' como "
                    "unidad de anÃ¡lisis principal."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Variables base tomadas directamente de la API de SECOP II",
                "encabezados": ["Variable (campo API)", "Tipo de dato", "DescripciÃ³n", "Unidad / dominio", "Grupo de riesgo al que aporta", "Fuente / documentaciÃ³n"],
                "filas": [
                    ["entidad", "Texto", "Nombre de la entidad que publica el proceso", "CatÃ¡logo de entidades pÃºblicas", "Trazabilidad / Grupo 4", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["nit_entidad", "Texto (identificador)", "NIT de la entidad que publicÃ³ el proceso", "NIT colombiano", "Trazabilidad / Grupo 4", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["departamento_entidad", "CategÃ³rica / geogrÃ¡fica", "Departamento en el cual estÃ¡ registrada la entidad", "32 departamentos + BogotÃ¡ D.C.", "Trazabilidad / Grupo 4 (comparar con departamento_proveedor)", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["ciudad_entidad", "CategÃ³rica / geogrÃ¡fica", "Ciudad en la cual estÃ¡ registrada la entidad", "CatÃ¡logo DIVIPOLA", "Grupo 4", "https://geoportal.dane.gov.co/laboratorio/codificacion-divipola/"],
                    ["ordenentidad", "CategÃ³rica", "Orden de la entidad (Nacional, Regional)", "Nacional / Regional", "Necesidades de informaciÃ³n â€” comparaciÃ³n nacional-regional", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["id_del_proceso", "Texto (identificador)", "Identificador Ãºnico del proceso, generado por la plataforma", "CÃ³digo alfanumÃ©rico SECOP", "Trazabilidad / llave primaria del registro", "https://community.secop.gov.co/"],
                    ["modalidad_de_contratacion", "CategÃ³rica", "Modalidad de selecciÃ³n bajo la cual se desarrolla el proceso", "LicitaciÃ³n pÃºblica, contrataciÃ³n directa, mÃ­nima cuantÃ­a, selecciÃ³n abreviada, concurso de mÃ©ritos, otras", "Grupo 2", "https://www.colombiacompra.gov.co/"],
                    ["justificaci_n_modalidad_de", "Texto", "JustificaciÃ³n de la modalidad de selecciÃ³n elegida", "Texto libre / puede estar vacÃ­o", "Grupo 2 (ausencia de justificaciÃ³n = seÃ±al de riesgo)", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["tipo_de_contrato", "CategÃ³rica", "Tipo de contrato definido para el proceso", "CatÃ¡logo SECOP (obra, consultorÃ­a, suministro, etc.)", "Grupo 2", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["codigo_principal_de_categoria", "CategÃ³rica", "CÃ³digo UNSPSC de la categorÃ­a principal del bien/servicio", "CatÃ¡logo UNSPSC", "Grupo 2 (referencia de precio esperado por categorÃ­a)", "https://www.ungm.org/Public/UNSPSC"],
                    ["precio_base", "NumÃ©rica (decimal)", "Precio base proyectado del proceso de compra", "Pesos colombianos (COP)", "Grupo 3", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["valor_total_adjudicacion", "NumÃ©rica (decimal)", "Valor total adjudicado", "Pesos colombianos (COP)", "Grupo 3 (ratio adjudicado/base)", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["fecha_de_publicacion_del", "Temporal (fecha)", "Fecha de publicaciÃ³n inicial del proceso", "AAAA-MM-DD", "Grupo 3", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["fecha_de_recepcion_de", "Temporal (fecha)", "Fecha asignada para la recepciÃ³n de respuestas de proveedores", "AAAA-MM-DD", "Grupo 3", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["fecha_de_apertura_efectiva", "Temporal (fecha)", "Fecha real de apertura de las respuestas", "AAAA-MM-DD", "Grupo 3 (comparar con fecha estimada)", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["fecha_adjudicacion", "Temporal (fecha)", "Fecha en la que se adjudicÃ³ el proceso al proveedor seleccionado", "AAAA-MM-DD", "Grupo 3 (dÃ­as entre publicaciÃ³n y adjudicaciÃ³n)", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["duracion", "NumÃ©rica (entero)", "DuraciÃ³n estimada del proceso de compra", "SegÃºn 'unidad_de_duracion'", "Grupo 3", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["unidad_de_duracion", "CategÃ³rica", "Unidad que aplica a la duraciÃ³n estimada", "DÃ­as, meses, aÃ±os", "Grupo 3", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["proveedores_invitados", "NumÃ©rica (entero)", "NÃºmero total de proveedores invitados a participar", "Entero â‰¥ 0", "Grupo 1", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["proveedores_con_invitacion", "NumÃ©rica (entero)", "Proveedores con invitaciÃ³n directa a participar", "Entero â‰¥ 0", "Grupo 1", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["proveedores_que_manifestaron", "NumÃ©rica (entero)", "Proveedores que manifestaron interÃ©s en el proceso", "Entero â‰¥ 0", "Grupo 1", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["conteo_de_respuestas_a_ofert", "NumÃ©rica (entero)", "NÃºmero de respuestas hechas de forma directa en las ofertas", "Entero â‰¥ 0", "Grupo 1", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["proveedores_unicos_con", "NumÃ©rica (entero)", "Proveedores Ãºnicos que redactaron respuestas en el proceso", "Entero â‰¥ 0", "Grupo 1 (denominador del ratio de competencia)", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["estado_del_procedimiento", "CategÃ³rica", "Estado actual de desarrollo del procedimiento", "Publicado, adjudicado, en ejecuciÃ³n, terminado, cancelado, etc.", "Trazabilidad â€” filtrado", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["adjudicado", "CategÃ³rica (SÃ­/No)", "Determina si el proceso fue adjudicado", "SÃ­ / No", "Trazabilidad â€” filtrado", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["nombre_del_adjudicador", "Texto", "Nombre del usuario que ejecutÃ³ la acciÃ³n de adjudicaciÃ³n", "Texto libre", "Grupo 4 (reincidencia adjudicador-proveedor)", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["nombre_del_proveedor", "Texto", "Nombre del proveedor adjudicado", "Texto libre", "Grupo 4", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["nit_del_proveedor_adjudicado", "Texto (identificador)", "NIT del proveedor adjudicado", "NIT colombiano", "Grupo 4 (identificador para medir concentraciÃ³n)", "https://www.rues.org.co/RUP"],
                    ["departamento_proveedor", "CategÃ³rica / geogrÃ¡fica", "Departamento en el que estÃ¡ registrado el proveedor adjudicado", "32 departamentos + BogotÃ¡ D.C.", "Grupo 4 (comparar con departamento_entidad)", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["ciudad_proveedor", "CategÃ³rica / geogrÃ¡fica", "Ciudad en la que estÃ¡ registrado el proveedor adjudicado", "CatÃ¡logo DIVIPOLA", "Grupo 4", "https://geoportal.dane.gov.co/laboratorio/codificacion-divipola/"],
                    ["urlproceso", "URL", "Enlace al proceso de compra en la plataforma", "URL vÃ¡lida", "Trazabilidad â€” verificaciÃ³n puntual", "https://community.secop.gov.co/"],
                ],
            },
            {
                "tipo": "tabla",
                "subtitulo": "Variables derivadas para el anÃ¡lisis de riesgo (calculadas por el equipo, no vienen directas de la API)",
                "encabezados": ["Variable derivada", "FÃ³rmula / regla", "InterpretaciÃ³n de riesgo"],
                "filas": [
                    ["ratio_competencia_real", "proveedores_unicos_con / proveedores_invitados", "Cercano a 0 en procesos formalmente competitivos = posible competencia simulada"],
                    ["ratio_valor_adjudicado_base", "valor_total_adjudicacion / precio_base", "Muy por encima de 1 = posible sobrecosto; muy por debajo = posible oferta artificialmente baja"],
                    ["dias_publicacion_adjudicacion", "fecha_adjudicacion âˆ’ fecha_de_publicacion_del", "Muy corto frente al promedio de la modalidad = posible direccionamiento del proceso"],
                    ["reincidencia_adjudicador_proveedor", "Conteo de adjudicaciones del mismo 'nombre_del_adjudicador' al mismo 'nit_del_proveedor_adjudicado'", "Valores altos y recurrentes = posible relaciÃ³n irregular"],
                    ["contratacion_directa_sin_justificacion", "modalidad_de_contratacion = 'ContrataciÃ³n directa' y 'justificaci_n_modalidad_de' vacÃ­o", "SeÃ±al de incumplimiento documental y posible riesgo de direccionamiento"],
                    ["proveedor_fuera_de_region", "departamento_proveedor distinto a departamento_entidad, en montos bajos que no ameritan proveedor forÃ¡neo", "Posible indicio de relaciÃ³n previa entidad-proveedor no explicada por especializaciÃ³n tÃ©cnica"],
                ],
            },
            {
                "tipo": "tabla",
                "subtitulo": "Variables de integraciÃ³n con los niveles regional y global",
                "encabezados": ["Variable", "Tipo de dato", "DescripciÃ³n", "Dominio", "Fuente de origen", "URL de la fuente"],
                "filas": [
                    ["nivel_comparacion", "CategÃ³rica", "Nivel de anÃ¡lisis del registro", "Global, Nacional, Regional", "Construida por el equipo", "â€”"],
                    ["anio_periodo", "Temporal (aÃ±o)", "AÃ±o de referencia usado para unir un proceso de SECOP con un indicador global/regional del mismo periodo", "AAAA", "Derivada de fecha_de_publicacion_del", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["indicador_apertura_global", "NumÃ©rica (Ã­ndice)", "Indicador de apertura/competencia comparable a nivel paÃ­s", "Escala del indicador de Benchmarking Public Procurement", "Banco Mundial - Benchmarking Public Procurement", "https://bpp.worldbank.org/en/data/exploreeconomies"],
                ],
            },
            {
                "tipo": "enlaces",
                "subtitulo": "DocumentaciÃ³n oficial y diccionarios de datos consultados",
                "lista": [
                    {"texto": "SECOP II â€” Procesos de ContrataciÃ³n (dataset y diccionario de columnas)", "url": "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"},
                    {"texto": "CodificaciÃ³n DIVIPOLA (DANE) â€” departamentos y municipios", "url": "https://geoportal.dane.gov.co/laboratorio/codificacion-divipola/"},
                    {"texto": "CatÃ¡logo UNSPSC (Naciones Unidas)", "url": "https://www.ungm.org/Public/UNSPSC"},
                    {"texto": "Registro Ãšnico de Proponentes (RUP)", "url": "https://www.rues.org.co/RUP"},
                    {"texto": "Colombia Compra Eficiente â€” normatividad y guÃ­as de modalidades de selecciÃ³n", "url": "https://www.colombiacompra.gov.co/"},
                ],
            },
        ],
    },
    {
        "slug": "calidad-inicial-de-los-datos",
        "numero": "07",
        "titulo": "Calidad inicial de los datos",
        "resumen": "Primer diagnÃ³stico de calidad: datos faltantes, duplicados, inconsistencias, etc.",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Resumen del diagnÃ³stico",
                "contenido": (
                    "Este es un diagnÃ³stico preliminar basado en el conocimiento del "
                    "comportamiento habitual de las fuentes utilizadas; los "
                    "porcentajes exactos se calcularÃ¡n sobre el archivo consolidado "
                    "una vez descargado en su totalidad desde "
                    "https://www.datos.gov.co/resource/p6dx-8zbt.json. Se "
                    "identifican de antemano los siguientes riesgos de calidad, "
                    "caracterÃ­sticos de datos administrativos de contrataciÃ³n "
                    "pÃºblica: valores faltantes en fechas de terminaciÃ³n de "
                    "contratos aÃºn en ejecuciÃ³n, duplicidad de procesos por adendas "
                    "o republicaciones, inconsistencia en la escritura del nombre de "
                    "una misma entidad (sin estandarizar mayÃºsculas/tildes), y "
                    "diferencias de granularidad y formato entre la fuente nacional "
                    "y las fuentes globales."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Hallazgos por variable",
                "encabezados": ["Variable", "Tipo de problema", "Problema detectado", "Causa probable", "AcciÃ³n propuesta", "Fuente donde se verificÃ³"],
                "filas": [
                    ["fecha_fin_ejecucion", "Valores faltantes", "Valores faltantes en procesos activos", "El contrato aÃºn no ha finalizado al momento de la descarga", "Marcar como 'en ejecuciÃ³n' en lugar de imputar una fecha", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["id_del_proceso", "Registros duplicados", "Registros duplicados por adenda o modificaciÃ³n", "SECOP II publica una nueva versiÃ³n del proceso ante cada modificaciÃ³n", "Conservar solo la versiÃ³n mÃ¡s reciente por id_del_proceso", "https://community.secop.gov.co/"],
                    ["entidad", "Inconsistencia de formato", "Inconsistencia de formato (mayÃºsculas, tildes, abreviaturas)", "DigitaciÃ³n manual por parte de cada entidad", "Normalizar texto (minÃºsculas, sin tildes) y usar catÃ¡logo oficial de entidades", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["valor_total_adjudicacion", "Valores fuera de dominio", "Valores en cero, negativos o atÃ­picamente altos frente al resto de su categorÃ­a UNSPSC", "Procesos sin oferta econÃ³mica registrada o errores de digitaciÃ³n", "Marcar como valor no disponible en lugar de eliminar; revisar outliers antes de excluir", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["proveedores_unicos_con", "Valores fuera de dominio", "Valores negativos o mayores a 'proveedores_invitados'", "Errores de captura en el mÃ³dulo de SECOP II", "Validar contra el rango lÃ³gico [0, proveedores_invitados] y marcar como inconsistente si no cumple", "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt"],
                    ["departamento / municipio", "Diferencias de formato", "Diferencias de codificaciÃ³n entre SECOP y DIVIPOLA (DANE)", "Uso de nombres de texto libre en vez de cÃ³digos estandarizados", "Cruzar contra el catÃ¡logo DIVIPOLA para unificar nombres", "https://geoportal.dane.gov.co/laboratorio/codificacion-divipola/"],
                    ["moneda / unidad monetaria", "Diferencias de formato", "Diferencia de unidad entre datos nacionales (COP) y globales (USD)", "Cada fuente reporta en su moneda local o de referencia", "Convertir a una unidad comÃºn usando tasa de cambio del periodo correspondiente", "https://www.banrep.gov.co/es/estadisticas/trm"],
                    ["nivel_comparacion (integraciÃ³n SECOPâ€“OCDS/Banco Mundial)", "Problema de integraciÃ³n entre fuentes", "Granularidad distinta: SECOP reporta a nivel de proceso individual, mientras OCDS y Benchmarking Public Procurement reportan agregados por paÃ­s/aÃ±o", "DiseÃ±o metodolÃ³gico distinto entre fuentes administrativas y fuentes de benchmarking internacional", "Unir por aÃ±o y paÃ­s como agregado, no intentar llevar el indicador global al nivel de proceso individual", "https://bpp.worldbank.org/"],
                    ["fecha_de_publicacion_del / fecha_adjudicacion (integraciÃ³n SECOPâ€“ContrataciÃ³n a un Clic)", "Problema de integraciÃ³n entre fuentes", "No siempre existe una llave exacta entre un proceso de SECOP y su referencia en el tablero departamental", "El tablero regional enlaza a SECOP pero no siempre expone el mismo identificador de proceso", "Integrar por combinaciÃ³n de entidad + fecha + valor aproximado cuando no exista el id_del_proceso exacto, documentando el nivel de certeza del cruce", "https://www.cundinamarca.gov.co/web/contratacion"],
                    ["cobertura por entidad", "Sesgo", "Posible sesgo de subregistro en municipios pequeÃ±os", "Menor capacidad institucional para publicar oportunamente en SECOP II", "Documentar el sesgo como limitaciÃ³n y evitar comparar municipios con baja tasa de publicaciÃ³n sin ajuste", "https://www.colombiacompra.gov.co/"],
                ],
            },
            {
                "tipo": "texto",
                "subtitulo": "Trazabilidad",
                "contenido": (
                    "Se conservarÃ¡ una copia sin modificar de cada archivo fuente "
                    "descargado (formato original y fecha de descarga), junto con un "
                    "registro de los filtros y transformaciones aplicadas para llegar "
                    "al dataset consolidado, de manera que cualquier resultado pueda "
                    "rastrearse hasta el registro original en SECOP "
                    "(https://community.secop.gov.co/ y "
                    "https://www.datos.gov.co/Gastos-Gubernamentales/SECOP-II-Procesos-de-Contrataci-n/p6dx-8zbt), "
                    "ContrataciÃ³n a un Clic (https://www.cundinamarca.gov.co/web/contratacion), "
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
        "resumen": "Restricciones del proyecto y aspectos Ã©ticos o tÃ©cnicos a tener en cuenta.",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Limitaciones",
                "contenido": (
                    "Cobertura temporal: SECOP II iniciÃ³ en 2016 y su adopciÃ³n por "
                    "parte de las entidades fue gradual, por lo que los primeros aÃ±os "
                    "tienen menor representatividad; se prioriza 2020-2025.\n"
                    "Cobertura geogrÃ¡fica: no todas las entidades territoriales "
                    "publican con la misma disciplina en SECOP II; algunas pequeÃ±as "
                    "alcaldÃ­as aÃºn dependen de SECOP I o de publicaciÃ³n fÃ­sica, lo "
                    "que puede subrepresentar ciertos municipios.\n"
                    "Comparabilidad global: los indicadores de Benchmarking Public "
                    "Procurement y OCDS estÃ¡n agregados a nivel de paÃ­s/aÃ±o, con un "
                    "nivel de granularidad mucho menor que los datos de SECOP a nivel "
                    "de proceso, por lo que la comparaciÃ³n global se harÃ¡ "
                    "principalmente a nivel de indicadores agregados, no de "
                    "registros individuales.\n"
                    "Recursos tÃ©cnicos: el volumen histÃ³rico de SECOP II es de gran "
                    "tamaÃ±o, por lo que la descarga y el procesamiento se realizan "
                    "mediante muestreo filtrado por departamento y periodo, no sobre "
                    "la totalidad histÃ³rica de la plataforma."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Consideraciones Ã©ticas y de privacidad",
                "contenido": (
                    "El dataset incluye identificaciÃ³n de proveedores (NIT, razÃ³n "
                    "social) y, en algunos casos, de contratistas personas naturales, "
                    "lo cual constituye un dato de carÃ¡cter pÃºblico segÃºn la Ley 1712 "
                    "de 2014 (Transparencia y Acceso a la InformaciÃ³n PÃºblica), pero "
                    "su tratamiento debe respetar los principios de la Ley 1581 de "
                    "2012 (protecciÃ³n de datos personales) cuando se trate de "
                    "personas naturales. El equipo se compromete a: (1) usar la "
                    "informaciÃ³n Ãºnicamente con fines acadÃ©micos y analÃ­ticos, (2) "
                    "evitar publicar conclusiones que seÃ±alen individualmente a una "
                    "persona natural o entidad como responsable de una irregularidad "
                    "sin el debido soporte estadÃ­stico, y (3) documentar que la "
                    "presencia de patrones atÃ­picos (por ejemplo, alta concentraciÃ³n "
                    "de contratos en un proveedor) es un indicio para anÃ¡lisis "
                    "posterior y no una acusaciÃ³n de corrupciÃ³n o ilegalidad."
                ),
            },
            {
                "tipo": "enlaces",
                "subtitulo": "Marco normativo consultado",
                "lista": [
                    {"texto": "Ley 1712 de 2014 â€” Transparencia y Acceso a la InformaciÃ³n PÃºblica", "url": "https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=56882"},
                    {"texto": "Ley 1581 de 2012 â€” ProtecciÃ³n de Datos Personales", "url": "https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=49981"},
                ],
            },
        ],
    },
]
