# Submenús de la Etapa 4
SUBMENUS_ETAPA_4 = [
    {
        "slug": "conocimiento-evidente",
        "numero": "01",
        "titulo": "Conocimiento Evidente",
        "resumen": (
            "Análisis exploratorio de los procesos de contratación pública "
            "de SECOP II para identificar patrones y formular preguntas "
            "sobre su distribución, territorio, temporalidad y características."
        ),
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Propósito de la etapa",
                "contenido": (
                    "Esta etapa presenta un análisis exploratorio de una "
                    "muestra de procesos de contratación pública publicados "
                    "en SECOP II Nacional. Mediante indicadores comparativos "
                    "y visualizaciones se busca describir patrones en las "
                    "modalidades, entidades, territorios, valores y fechas "
                    "de publicación, y aportar evidencia para explorar "
                    "posibles riesgos de gestión. Los patrones observados "
                    "son señales para analizar y no constituyen, por sí solos, "
                    "prueba de irregularidades."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Contexto de los datos",
                "contenido": (
                    "Fuente: SECOP II Nacional, conjunto de datos de procesos "
                    "de contratación pública.\n"
                    "Periodo observado: del 1 de enero de 2020 al 1 de "
                    "diciembre de 2025, según fecha de publicación del "
                    "proceso.\n"
                    "Unidad de análisis: cada fila representa un registro "
                    "de proceso de contratación; no necesariamente un "
                    "contrato firmado ni un proceso único. El archivo "
                    "contiene 79 filas exactamente duplicadas y 208 "
                    "repeticiones de id_del_proceso; los conteos se "
                    "refieren a filas hasta depurar esos casos.\n"
                    "Cobertura del archivo: 10.000 registros y 34 variables. "
                    "Es la muestra consolidada en el CSV del proyecto, no "
                    "la totalidad de los procesos publicados en SECOP II. "
                    "La descarga usa cuotas mensuales casi iguales y orden "
                    "ascendente por fecha, por lo que no es una muestra "
                    "aleatoria."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Preguntas de análisis",
                "contenido": (
                    "1. Composición y distribución: ¿Cómo se distribuyen "
                    "los registros por modalidad, tipo de contrato y "
                    "departamento de la entidad, y qué categorías concentran "
                    "el mayor volumen?\n\n"
                    "2. Comparación territorial: ¿Cómo difieren el volumen "
                    "de registros y el valor adjudicado entre órdenes de "
                    "entidad y territorios reportados por la entidad?\n\n"
                    "3. Comportamiento temporal: ¿Cómo se distribuye por "
                    "mes el valor adjudicado registrado para procesos "
                    "publicados en 2025 y qué modalidades concentran esos "
                    "montos? La fecha usada es de publicación, no de "
                    "adjudicación, firma ni desembolso.\n\n"
                    "4. Análisis multivariado: ¿Cómo varían el conteo de "
                    "registros y el valor adjudicado al cruzar modalidad, "
                    "tipo de contrato, orden de entidad y proveedores "
                    "únicos? Las asociaciones observadas no implican "
                    "causalidad."
                ),
            },
        ],
    },
    {
    "slug": "composicion-y-distribucion",
    "numero": "02",
    "titulo": "Composición y Distribución",
    "resumen": (
        "Descripción de cómo se distribuyen los procesos según la "
        "modalidad de contratación, el tipo de contrato y el "
        "departamento de la entidad, como señales para analizar y no "
        "como prueba de irregularidades."
    ),
    "bloques": [
        {
            "tipo": "texto",
            "subtitulo": "Conocimiento 1: Concentración en modalidades de selección directa",
            "contenido": (
                "Pregunta: ¿Cuál es la modalidad de contratación más "
                "utilizada por las entidades públicas en la muestra?\n\n"
                "Variables: modalidad_de_contratacion y Cantidad de "
                "Procesos (conteo de registros).\n\n"
                "Procedimiento: Se contaron los procesos y se calculó la "
                "participación porcentual de cada modalidad. El denominador "
                "es el total de 10.000 registros de la muestra.\n\n"
                "Evidencia: Gráfico circular de Cantidad de Procesos por "
                "modalidad_de_contratacion, ubicado en la parte superior de "
                "la página de Power BI.\n\n"
                "Hallazgo: El 84,94 % de los procesos se concentra en dos "
                "modalidades: Contratación directa (45,36 %) y Contratación "
                "régimen especial (39,58 %). El denominador de ambos "
                "porcentajes es el total de 10.000 registros.\n\n"
                "Interpretación: Estas son las dos categorías más "
                "frecuentes de la muestra. El conteo no permite concluir "
                "por sí solo cuántos oferentes participaron ni si un "
                "proceso tuvo competencia efectiva; además, las categorías "
                "de SECOP no equivalen directamente a una medida de "
                "pluralidad.\n\n"
                "Utilidad: Permite priorizar auditorías preventivas sobre "
                "los procesos de contratación directa y régimen especial, "
                "para verificar que su uso esté justificado.\n\n"
                "Limitación: El gráfico cuenta procesos, no presupuesto. "
                "Las licitaciones públicas, aunque sean pocas, podrían "
                "concentrar gran parte del valor. Además, la muestra no "
                "representa la totalidad de SECOP II."
            ),
        },
        {
            "tipo": "texto",
            "subtitulo": "Conocimiento 2: Predominio de la prestación de servicios",
            "contenido": (
                "Pregunta: ¿Qué tipo de contrato genera el mayor volumen de "
                "procesos?\n\n"
                "Variables: tipo_de_contrato y Cantidad de Procesos (conteo "
                "de registros).\n\n"
                "Procedimiento: Se contaron los procesos por tipo de "
                "contrato y se ordenaron de mayor a menor en un gráfico de "
                "barras horizontales. El denominador es el total de 10.000 "
                "registros de la muestra.\n\n"
                "Evidencia: Gráfico de barras de Cantidad de Procesos por "
                "tipo_de_contrato, ubicado en la parte inferior izquierda "
                "de la página de Power BI.\n\n"
                "Hallazgo: \"Prestación de servicios\" reúne 6.731 procesos "
                "(67,31 % de los 10.000 registros); el segundo tipo, "
                "\"Decreto 092 de 2017\", reúne 1.270 (12,70 %).\n\n"
                "Interpretación: La prestación de servicios predomina por "
                "cantidad en esta muestra. El resultado no indica por sí "
                "solo si las funciones podían ser cubiertas por personal "
                "de planta. Aunque el CSV incluye el NIT del proveedor, "
                "9.614 filas (96,14 %) tienen ese dato como \"No Definido\", "
                "por lo que no se puede establecer con fiabilidad cuántos "
                "proveedores únicos hay.\n\n"
                "Utilidad: Puede orientar una revisión de la planeación de "
                "la contratación de servicios, contrastando cada necesidad "
                "con su justificación y alcance.\n\n"
                "Limitación: El indicador cuenta filas y no compara el "
                "valor adjudicado; el NIT faltante limita la identificación "
                "de proveedores repetidos y no identifica a las personas "
                "naturales detrás de cada proveedor. El conjunto es una "
                "muestra, no la totalidad de SECOP II."
            ),
        },
        {
            "tipo": "texto",
            "subtitulo": "Conocimiento 3: Distribución territorial y calidad del dato de departamento",
            "contenido": (
                "Pregunta: ¿Cómo se distribuyen los procesos de "
                "contratación según el departamento de la entidad?\n\n"
                "Variables: departamento_entidad y Cantidad de Procesos "
                "(conteo de registros).\n\n"
                "Procedimiento: Se contaron los procesos por departamento y "
                "se representaron en un mapa de árbol, donde el tamaño de "
                "cada bloque indica su proporción. El denominador es el "
                "total de 10.000 registros. Los registros con valor \"No "
                "definido\" se mantuvieron como una categoría aparte y no "
                "se asimilaron a ningún departamento.\n\n"
                "Evidencia: Mapa de árbol de Cantidad de Procesos por "
                "departamento_entidad, ubicado en la parte inferior derecha "
                "de la página de Power BI.\n\n"
                "Hallazgo: Bogotá D.C. registra 2.874 procesos (28,74 %), "
                "Antioquia 1.088 (10,88 %) y \"No Definido\" 697 (6,97 %), "
                "sobre los 10.000 registros.\n\n"
                "Interpretación: Bogotá D.C. y Antioquia son los dos "
                "departamentos con más registros. \"No Definido\" es un "
                "dato faltante de ubicación, no un departamento ni una "
                "respuesta negativa, y reduce la cobertura territorial "
                "interpretable.\n\n"
                "Utilidad: Respalda la propuesta de agregar reglas de "
                "validación para que el campo de departamento no quede "
                "vacío o con valor \"No definido\" al registrar un proceso.\n\n"
                "Limitación: El departamento corresponde a la sede de la "
                "entidad. Las entidades nacionales con sede en Bogotá "
                "pueden ejecutar contratos en otras regiones, por lo que "
                "el mapa no muestra dónde se ejecutan realmente. Un valor "
                "\"No definido\" es un dato faltante, no una respuesta "
                "negativa."
            ),
        },
        {
            "tipo": "texto",
            "subtitulo": "Informe de Power BI",
            "contenido": (
                "El tablero interactivo de esta pregunta se muestra en la "
                "parte superior de esta sección."
            ),
        },
    ],
},
    {
    "slug": "comparacion-territorial",
    "numero": "03",
    "titulo": "Comparación Territorial",
    "resumen": (
        "Comparación del volumen de procesos, del presupuesto y de la "
        "calidad de la ubicación entre entidades del orden nacional y "
        "territorial, como señales para analizar y no como prueba de "
        "irregularidades."
    ),
    "bloques": [
        {
            "tipo": "texto",
            "subtitulo": "Contexto de la página",
            "contenido": (
                "Pregunta general: ¿Qué diferencias existen en la "
                "concentración del presupuesto adjudicado y en el volumen "
                "de procesos al comparar las entidades del orden nacional "
                "con las del orden territorial en los distintos "
                "departamentos?\n\n"
                "Variables de la página: ordenentidad, departamento_entidad, "
                "ciudad_entidad, Presupuesto Total (suma del precio base o "
                "valor adjudicado) y Cantidad de Procesos (conteo de "
                "registros).\n\n"
                "Visualizaciones: un mapa de distribución geográfica de las "
                "entidades, un gráfico de columnas con el conteo de procesos "
                "por orden de entidad y un gráfico de columnas con el "
                "presupuesto total por orden de entidad."
            ),
        },
        {
            "tipo": "texto",
            "subtitulo": "Conocimiento 1: Distribución de la carga de procesos entre el nivel nacional y el territorial",
            "contenido": (
                "Pregunta: ¿Cómo se distribuye el volumen de procesos entre "
                "las entidades del orden nacional y las del orden "
                "territorial?\n\n"
                "Variables: ordenentidad y Cantidad de Procesos (conteo de "
                "registros de departamento_entidad).\n\n"
                "Procedimiento: Se contaron los registros de la muestra y se "
                "agruparon por orden de la entidad. El denominador de las "
                "comparaciones es el total de 10.000 registros del archivo.\n\n"
                "Evidencia: Gráfico de columnas con el conteo de procesos por "
                "orden de entidad, ubicado en la parte superior derecha de "
                "la página de Power BI.\n\n"
                "Hallazgo: Las entidades territoriales registran 6.199 "
                "procesos (61,99 %); las nacionales 3.645 (36,45 %) y las "
                "corporaciones autónomas 156 (1,56 %). El denominador es "
                "el total de 10.000 registros.\n\n"
                "Interpretación: En esta muestra, la mayor parte de los "
                "procesos publicados proviene de entidades territoriales. "
                "Una hipótesis, que los datos no permiten comprobar, es que "
                "esto refleje un uso más intensivo de la plataforma en "
                "alcaldías y gobernaciones.\n\n"
                "Utilidad: Aporta un insumo para priorizar la capacitación y "
                "el soporte a los usuarios de entidades territoriales.\n\n"
                "Limitación: El conteo asume que todos los procesos "
                "demandan el mismo esfuerzo, y un proceso nacional puede "
                "ser más complejo que varios territoriales. Además, la "
                "muestra no representa la totalidad de SECOP II, por lo que "
                "las proporciones pueden cambiar con la población completa."
            ),
        },
        {
            "tipo": "texto",
            "subtitulo": "Conocimiento 2: Concentración del presupuesto según el orden de la entidad",
            "contenido": (
                "Pregunta: ¿Qué orden de entidad concentra el mayor "
                "presupuesto adjudicado?\n\n"
                "Variables: ordenentidad y Presupuesto Total, que en el "
                "modelo corresponde a la suma de "
                "valor_total_adjudicacion.\n\n"
                "Procedimiento: Se sumó valor_total_adjudicacion por orden "
                "de entidad. El denominador de las participaciones es la "
                "suma de esa variable en los 10.000 registros; los valores "
                "cero se conservan y no aportan a la suma.\n\n"
                "Evidencia: Gráfico de columnas con el presupuesto total por "
                "orden de entidad, ubicado en la parte inferior derecha de "
                "la página de Power BI.\n\n"
                "Hallazgo: Las entidades territoriales suman "
                "$173.608.354.138 (58,10 % del total); las nacionales, "
                "$111.650.841.967 (37,36 %); y las corporaciones autónomas, "
                "$13.554.056.283 (4,54 %). El total de la muestra es "
                "$298.813.252.388.\n\n"
                "Interpretación: En esta muestra, el presupuesto se "
                "concentra en mayor medida en las entidades territoriales. "
                "Esta diferencia es una asociación observada y no indica por "
                "sí sola un mejor o peor manejo de los recursos.\n\n"
                "Utilidad: Puede ayudar a los entes de control a priorizar "
                "la revisión de los procesos de mayor valor en gobernaciones "
                "y alcaldías.\n\n"
                "Limitación: La suma es sensible a valores extremos y no "
                "mide por sí sola la calidad del gasto. El dataset es una "
                "muestra de 10.000 registros; no representa el universo "
                "completo de SECOP II."
            ),
        },
        {
            "tipo": "texto",
            "subtitulo": "Conocimiento 3: Calidad de la ubicación registrada por las entidades",
            "contenido": (
                "Pregunta: ¿Qué tan confiable es la información de "
                "ubicación que reportan las entidades en sus registros?\n\n"
                "Variables: departamento_entidad, ciudad_entidad y "
                "ordenentidad.\n\n"
                "Procedimiento: Se compararon los campos de departamento y "
                "ciudad con el orden de la entidad en el mapa. Se contaron "
                "por separado los registros marcados \"No Definido\". El "
                "denominador para los porcentajes es el total de 10.000 "
                "registros.\n\n"
                "Evidencia: Mapa de distribución geográfica de "
                "departamento_entidad, ciudad_entidad y ordenentidad. En el "
                "CSV hay 697 departamentos (6,97 %) y 2.489 ciudades "
                "(24,89 %) con valor \"No Definido\".\n\n"
                "Hallazgo: Una proporción de los registros carece de "
                "ubicación departamental o municipal definida. El mapa "
                "geocodifica texto y no aporta coordenadas verificadas; "
                "por ello, el CSV no permite confirmar cuántos puntos "
                "quedan fuera de Colombia.\n\n"
                "Interpretación: Los valores faltantes limitan la "
                "comparación territorial. Una marca del mapa en una "
                "ubicación inesperada debe revisarse contra el registro "
                "original antes de clasificarla como error.\n\n"
                "Utilidad: Priorizar la validación de los campos de "
                "departamento y ciudad y, cuando sea posible, usar "
                "catálogos territoriales o coordenadas verificadas.\n\n"
                "Limitación: El mapa representa la ubicación reportada de "
                "la entidad, no necesariamente el lugar de ejecución del "
                "contrato. \"No Definido\" es un dato faltante, no una "
                "respuesta negativa."
            ),
        },
        {
            "tipo": "texto",
            "subtitulo": "Cierre del análisis",
            "contenido": (
                "Limitación general: La comparación territorial puede estar "
                "limitada por los registros con ubicación \"No Definido\" "
                "(6,97 % en departamento y 24,89 % en ciudad). "
                "Los resultados corresponden a una muestra de 10.000 "
                "registros.\n\n"
                "Decisión sustentada en los datos: Priorizar la revisión "
                "del gasto de las entidades territoriales y depurar las "
                "ubicaciones anómalas antes de emitir informes oficiales de "
                "ejecución regional."
            ),
        },
        {
            "tipo": "texto",
            "subtitulo": "Informe de Power BI",
            "contenido": (
                "El tablero interactivo de esta pregunta se muestra en la "
                "parte superior de esta sección."
            ),
        },
    ],
},
    {
        "slug": "comportamiento-temporal",
        "numero": "04",
        "titulo": "Comportamiento Temporal",
        "resumen": (
            "Comparación mensual de los valores adjudicados registrados "
            "según la fecha de publicación, con énfasis descriptivo en 2025."
        ),
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Pregunta, variables y alcance",
                "contenido": (
                    "Pregunta: ¿Cómo varía por mes el valor adjudicado "
                    "registrado para los procesos publicados en 2025, y qué "
                    "modalidades concentran esos valores?\n\n"
                    "Variables: fecha_de_publicacion_del (año y mes), "
                    "valor_total_adjudicacion, modalidad_de_contratacion y "
                    "Duracion_en_Dias, campo del modelo usado en el gráfico "
                    "combinado.\n\n"
                    "Procedimiento: El segmentador de fecha filtra el año; "
                    "los gráficos agrupan por mes y calculan la suma del "
                    "valor adjudicado. El gráfico apilado al 100 % usa como "
                    "denominador la suma mensual de "
                    "valor_total_adjudicacion. La duración se presenta en "
                    "el gráfico combinado, no como fecha de adjudicación.\n\n"
                    "Alcance: El archivo contiene 1.666 filas de 2025, con "
                    "138 o 139 registros por mes. La construcción del "
                    "dataset asignó cuotas mensuales casi iguales y ordenó "
                    "la descarga por fecha ascendente. Estos datos describen "
                    "la muestra y no permiten estimar estacionalidad ni "
                    "ejecución presupuestal de todo SECOP II."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Conocimiento 1: Picos mensuales del valor adjudicado registrado en 2025",
                "contenido": (
                    "Pregunta: ¿En qué meses se observan los mayores valores "
                    "adjudicados registrados para procesos publicados en "
                    "2025?\n\n"
                    "Variables: fecha_de_publicacion_del (mes) y "
                    "valor_total_adjudicacion.\n\n"
                    "Procedimiento: Se filtró el año 2025 y se sumó "
                    "valor_total_adjudicacion por mes. La suma anual de la "
                    "muestra (denominador para las participaciones) es "
                    "$44.932.217.929, distribuida en 1.666 registros.\n\n"
                    "Evidencia: Gráfico \"Presupuesto por Mes\" y gráfico "
                    "combinado \"Relación Presupuesto vs Duración en días\" "
                    "de la página Temporalidad.\n\n"
                    "Hallazgo: Agosto presenta la mayor suma, "
                    "$18.190.337.243 (40,48 % del total anual de la muestra); "
                    "abril ocupa el segundo lugar con $11.928.692.378 "
                    "(26,55 %). En conjunto representan 67,03 %. Febrero "
                    "registra el menor valor, $4.000.000.\n\n"
                    "Interpretación: En esta muestra, los valores "
                    "adjudicados asociados a procesos publicados en abril "
                    "y agosto son superiores a los de los demás meses. La "
                    "fecha corresponde a publicación del proceso: no "
                    "establece cuándo se adjudicó, comprometió o desembolsó "
                    "el dinero, ni demuestra estacionalidad.\n\n"
                    "Utilidad: Orientar una revisión documental de los "
                    "procesos de mayor valor de abril y agosto, verificando "
                    "fecha de adjudicación, objeto, modalidad y expediente.\n\n"
                    "Limitación: La muestra fue construida con cuotas "
                    "mensuales similares y descarga ordenada por fecha; no "
                    "es una muestra aleatoria ni representa el gasto total. "
                    "Los montos son sensibles a unos pocos valores altos."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Conocimiento 2: Concentración mensual del valor por modalidad",
                "contenido": (
                    "Pregunta: ¿Cómo se reparte entre modalidades el valor "
                    "adjudicado registrado en cada mes de 2025?\n\n"
                    "Variables: fecha_de_publicacion_del (mes), "
                    "modalidad_de_contratacion y "
                    "valor_total_adjudicacion.\n\n"
                    "Procedimiento: Se agrupó la suma adjudicada por mes y "
                    "modalidad en un gráfico de columnas apiladas al 100 %. "
                    "El denominador de cada columna es la suma de "
                    "valor_total_adjudicacion de ese mes; los registros con "
                    "valor cero no aportan al porcentaje.\n\n"
                    "Evidencia: Gráfico inferior \"Tipos de contratación "
                    "por mes\" de la página Temporalidad.\n\n"
                    "Hallazgo: En 5 de los 12 meses (enero, febrero, marzo, "
                    "junio y diciembre), una sola modalidad reúne el 100 % "
                    "del valor adjudicado positivo registrado. En abril, "
                    "la modalidad con mayor participación aporta 94,97 %; "
                    "en mayo, 97,72 %. Por tanto, no son 8 de 12 meses con "
                    "un único mecanismo.\n\n"
                    "Interpretación: El valor adjudicado de la muestra "
                    "está concentrado en una modalidad en esos cinco "
                    "meses. Esto no equivale a falta de pluralidad de "
                    "oferentes: el gráfico no cuenta oferentes ni procesos "
                    "por modalidad, y los ceros pueden corresponder a "
                    "procesos sin valor adjudicado registrado.\n\n"
                    "Utilidad: Usar la distribución como punto de partida "
                    "para revisar qué procesos y justificaciones explican "
                    "la concentración mensual, sin inferir irregularidades.\n\n"
                    "Limitación: El porcentaje describe montos registrados "
                    "en la muestra; no permite evaluar la legalidad de la "
                    "modalidad ni la competencia efectiva."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Conocimiento 3: Modalidad con mayor participación en agosto",
                "contenido": (
                    "Pregunta: ¿Qué modalidad aporta la mayor proporción "
                    "del valor adjudicado registrado en el mes de mayor "
                    "suma, agosto de 2025?\n\n"
                    "Variables: fecha_de_publicacion_del (año y mes), "
                    "modalidad_de_contratacion y "
                    "valor_total_adjudicacion.\n\n"
                    "Procedimiento: Se filtró agosto de 2025, se sumó "
                    "valor_total_adjudicacion por modalidad y se dividió "
                    "cada suma entre el total del mes, "
                    "$18.190.337.243.\n\n"
                    "Evidencia: Contraste entre \"Presupuesto por Mes\" y "
                    "la columna de agosto del gráfico apilado al 100 % "
                    "\"Tipos de contratación por mes\".\n\n"
                    "Hallazgo: \"Contratación régimen especial (con "
                    "ofertas)\" aporta $16.299.101.442, equivalente al "
                    "89,60 % del total de agosto en la muestra. La "
                    "participación se refiere al valor, no al número de "
                    "contratos.\n\n"
                    "Interpretación: El valor de agosto está fuertemente "
                    "concentrado en esa categoría. Esta asociación "
                    "descriptiva no prueba direccionamiento, ausencia de "
                    "competencia ni una infracción.\n\n"
                    "Utilidad: Priorizar una revisión proporcional de los "
                    "expedientes que conforman ese monto, incluyendo "
                    "justificación de la modalidad, número de procesos y "
                    "documentación de selección.\n\n"
                    "Limitación: La visualización agrega varios procesos "
                    "en una sola suma y no permite saber si el monto "
                    "corresponde a uno o muchos contratos. Además, la "
                    "muestra mensual no es aleatoria y la fecha usada es "
                    "la de publicación, no la de adjudicación o pago."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Informe de Power BI",
                "contenido": (
                    "El tablero interactivo de esta pregunta se muestra en la "
                    "parte superior de esta sección."
                ),
            },
        ],
    },
    {
    "slug": "analisis-multivariado",
    "numero": "05",
    "titulo": "Análisis Multivariado",
    "resumen": (
        "Exploración conjunta de tres o más variables para identificar "
        "perfiles de contratación, niveles de competencia y distribución "
        "del gasto, como señales para analizar y no como prueba de "
        "irregularidades."
    ),
    "bloques": [
        {
            "tipo": "texto",
            "subtitulo": "Conocimiento 1: Concentración del esfuerzo contractual en el nivel territorial",
            "contenido": (
                "Pregunta: ¿Cómo interactúa el orden de la entidad con el "
                "tipo de contrato frente al volumen de procesos?\n\n"
                "Variables: tipo_de_contrato, ordenentidad y Cantidad de "
                "Procesos (conteo de registros).\n\n"
                "Procedimiento: Se cruzaron las tres variables en un "
                "gráfico de columnas apiladas. El tipo de contrato se ubicó "
                "en el eje X y cada columna se dividió por el orden de la "
                "entidad (nacional, territorial, corporación autónoma). El "
                "denominador de las comparaciones es el total de procesos "
                "de cada tipo de contrato.\n\n"
                "Evidencia: Gráfico de columnas apiladas, ubicado en la "
                "parte inferior izquierda de la página de Power BI.\n\n"
                "Hallazgo: El tipo de contrato \"Prestación de servicios\" "
                "acumula 6.731 procesos: 4.234 territoriales (62,90 %), "
                "2.380 nacionales (35,36 %) y 117 de corporaciones "
                "autónomas (1,74 %). El denominador es los 6.731 registros "
                "de prestación de servicios.\n\n"
                "Interpretación: Dentro de esta categoría, la mayor "
                "proporción de registros corresponde a entidades "
                "territoriales. La asociación no explica por qué se "
                "contrató ni determina si la necesidad podía cubrirse con "
                "personal de planta.\n\n"
                "Utilidad: Permite priorizar la revisión de la "
                "justificación de estas contrataciones en las entidades "
                "territoriales.\n\n"
                "Limitación: El gráfico cuenta procesos, no valores. Los "
                "procesos nacionales podrían ser menos numerosos pero de "
                "mayor valor. Además, la muestra es de 10.000 registros y "
                "no representa la totalidad de SECOP II."
            ),
        },
        {
            "tipo": "texto",
            "subtitulo": "Conocimiento 2: Presupuesto, modalidad y pluralidad de oferentes",
            "contenido": (
                "Pregunta: ¿Qué relación existe entre el presupuesto "
                "asignado, la modalidad elegida y la cantidad de oferentes "
                "que compiten?\n\n"
                "Variables: Presupuesto Total "
                "(valor_total_adjudicacion), Promedio Oferentes y "
                "modalidad_de_contratacion. El cálculo reproducido en el "
                "CSV promedia proveedores_unicos_con; se debe confirmar "
                "que la medida DAX del visual use esa misma columna.\n\n"
                "Procedimiento: Se construyó un gráfico de dispersión con "
                "el promedio de oferentes en el eje X y el presupuesto "
                "total en el eje Y, con un punto por cada modalidad. El "
                "promedio de oferentes se calcula sobre los procesos de "
                "cada modalidad.\n\n"
                "Evidencia: Gráfico de dispersión, ubicado en la parte "
                "superior izquierda de la página de Power BI.\n\n"
                "Hallazgo: \"Selección Abreviada de Menor Cuantía\" suma "
                "$57.718.420.574 adjudicados en 271 procesos y presenta "
                "1,22 proveedores únicos por proceso en promedio. "
                "\"Licitación pública\" suma $76.015.605.131 en 59 procesos "
                "y promedia 12,25 proveedores únicos. El presupuesto es "
                "la suma de valor_total_adjudicacion; cada promedio usa "
                "los procesos de su modalidad.\n\n"
                "Interpretación: En la muestra, las modalidades difieren "
                "en valores agregados y promedio registrado de proveedores "
                "únicos. No es una comparación de valores por contrato ni "
                "demuestra que una modalidad cause más competencia.\n\n"
                "Utilidad: Revisar los expedientes de alto valor y "
                "contrastar los conteos de proveedores con las ofertas "
                "efectivamente recibidas y el estado de cada proceso.\n\n"
                "Limitación: El promedio reproducido incluye los ceros "
                "registrados en proveedores_unicos_con y puede verse "
                "afectado por registros cuyo significado debe verificarse; "
                "un cero no demuestra por sí solo que no hubo oferentes ni "
                "que el proceso fue desierto. La expresión DAX del visual "
                "debe confirmarse; la muestra no representa la totalidad "
                "de SECOP II."
            ),
        },
        {
            "tipo": "texto",
            "subtitulo": "Conocimiento 3: Distribución del gasto en el concurso de méritos",
            "contenido": (
                "Pregunta: ¿Cómo se distribuye el presupuesto de la "
                "modalidad \"Concurso de méritos abierto\" según el orden "
                "de la entidad?\n\n"
                "Variables: ordenentidad, modalidad_de_contratacion y "
                "Presupuesto Total.\n\n"
                "Procedimiento: Se construyó una matriz que filtra la "
                "modalidad específica y reparte su presupuesto entre los "
                "órdenes de entidad. El denominador de los porcentajes es "
                "el presupuesto total de esa modalidad.\n\n"
                "Evidencia: Matriz ubicada en la parte inferior derecha "
                "de la página de Power BI.\n\n"
                "Hallazgo: En los 34 procesos de \"Concurso de méritos "
                "abierto\", el total adjudicado es $5.183.077.121. Las "
                "entidades territoriales suman $2.715.085.757 (52,39 %), "
                "las nacionales $2.285.203.595 (44,09 %) y las "
                "corporaciones autónomas $182.787.769 (3,53 %). El "
                "denominador es el total de esa modalidad.\n\n"
                "Interpretación: En esta modalidad, usada habitualmente "
                "para consultorías, los recursos se reparten de forma "
                "relativamente equilibrada entre el nivel nacional y el "
                "territorial.\n\n"
                "Utilidad: Aporta evidencia para evaluar cómo se reparte "
                "el gasto en consultorías entre niveles de gobierno.\n\n"
                "Limitación: El resultado corresponde a 34 procesos de "
                "esta muestra y no debe extrapolarse a todos los concursos "
                "de méritos. Un cero en la matriz es distinto de un valor "
                "faltante."
            ),
        },
        {
            "tipo": "texto",
            "subtitulo": "Informe de Power BI",
            "contenido": (
                "El tablero interactivo de esta pregunta se muestra en la "
                "parte superior de esta sección."
            ),
        },
    ],
    },
        {
        "slug": "datos-y-dax",
        "numero": "06",
        "titulo": "Datos y DAX",
        "resumen": (
            "Documentación del tratamiento de los datos, el modelo de "
            "Power BI y las medidas DAX utilizadas para construir los "
            "indicadores de la etapa."
        ),
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Tratamiento previo de los datos",
                "contenido": (
                    "Fuente: SECOP II Nacional, API del conjunto de datos "
                    "de procesos de contratación pública "
                    "(https://www.datos.gov.co/resource/p6dx-8zbt.json).\n"
                    "Archivo usado por el informe: "
                    "dataset/processed/secop_ii_nacional.csv, con 10.000 "
                    "filas y 34 variables; periodo de publicación "
                    "2020-01-01 a 2025-12-01.\n"
                    "Tratamiento verificable en construir_dataset.py: "
                    "descarga por cuotas mensuales, orden ascendente por "
                    "fecha y selección de 34 columnas. Ese script no "
                    "elimina duplicados ni realiza imputación o "
                    "estandarización.\n"
                    "Continuidad con la etapa 3: la documentación de esa "
                    "etapa menciona un archivo ETL de 9.792 registros, "
                    "pero ese resultado no está en el repositorio ni es "
                    "el CSV de 10.000 filas incorporado aquí. Se debe "
                    "confirmar si el PBIX debe actualizarse con el archivo "
                    "final de SSIS antes de entregar."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Problemas de calidad que persisten",
                "contenido": (
                    "1. Duplicados: 79 filas exactamente repetidas "
                    "(0,79 %) y 208 repeticiones de id_del_proceso (2,08 % "
                    "de las filas exceden el conteo de IDs únicos). No "
                    "deben interpretarse automáticamente como errores sin "
                    "revisar la regla de unicidad.\n\n"
                    "2. Ubicación: 697 filas (6,97 %) tienen "
                    "departamento_entidad = \"No Definido\" y 2.489 "
                    "(24,89 %) tienen ciudad_entidad = \"No Definido\". "
                    "Son valores faltantes categorizados, no respuestas "
                    "negativas.\n\n"
                    "3. valor_total_adjudicacion contiene 9.127 ceros "
                    "(91,27 %). El cero no debe confundirse con un nulo "
                    "ni asumirse como error: puede corresponder a un "
                    "proceso sin adjudicación registrada.\n\n"
                    "4. El archivo está balanceado artificialmente por "
                    "cuotas mensuales y descargado por fecha ascendente. "
                    "No permite inferir proporciones poblacionales ni "
                    "estacionalidad de SECOP II.\n\n"
                    "5. No hay celdas vacías en este CSV, pero sí valores "
                    "categóricos \"No Definido\". No hay fecha de firma. "
                    "El NIT del proveedor figura como \"No Definido\" en "
                    "9.614 filas (96,14 %), lo que impide contar con "
                    "fiabilidad proveedores únicos."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Modelo de datos en Power BI",
                "contenido": (
                    "Los campos de los visuales revisados pertenecen a "
                    "secop_ii_nacional; la fecha usa la jerarquía "
                    "automática Año/Trimestre/Mes/Día. No se observan "
                    "relaciones con otras tablas en las consultas de las "
                    "páginas.\n\n"
                    "Control necesario: Cantidad Procesos cuenta filas, "
                    "no IDs únicos. En el CSV actual arroja 10.000, pero "
                    "hay 9.792 IDs distintos y 79 filas exactamente "
                    "duplicadas. Por eso los indicadores y porcentajes "
                    "actuales describen filas de la muestra, no procesos "
                    "únicos depurados."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Medidas DAX principales",
                "contenido": (
                    "Cantidad Procesos\n"
                    "Qué calcula: cuenta filas, respetando los filtros "
                    "activos; no cuenta IDs únicos.\n"
                    "Fórmula: COUNTROWS('secop_ii_nacional')\n\n"
                    "Presupuesto Total\n"
                    "Qué calcula: suma de valor_total_adjudicacion; no es "
                    "la suma del precio base.\n"
                    "Fórmula: SUM('secop_ii_nacional'"
                    "[valor_total_adjudicacion])\n\n"
                    "Promedio Adjudicado\n"
                    "Qué calcula: promedio de "
                    "valor_total_adjudicacion sobre las filas visibles; "
                    "los ceros afectan el promedio.\n"
                    "Fórmula: AVERAGE('secop_ii_nacional'"
                    "[valor_total_adjudicacion])\n\n"
                    "Contrato Mas Caro\n"
                    "Qué calcula: máximo valor adjudicado dentro del "
                    "contexto de filtros; no identifica por sí solo el "
                    "contrato ni su entidad.\n"
                    "Fórmula: MAX('secop_ii_nacional'"
                    "[valor_total_adjudicacion])\n\n"
                    "Promedio Oferentes\n"
                    "Qué calcula: promedio de proveedores únicos "
                    "registrados por fila; incluye los ceros.\n"
                    "Fórmula: AVERAGE('secop_ii_nacional'"
                    "[proveedores_unicos_con])\n\n"
                    "Total Entidades\n"
                    "Qué calcula: cantidad de nombres distintos en "
                    "entidad bajo los filtros activos, no un conteo de "
                    "procesos.\n"
                    "Fórmula: DISTINCTCOUNT('secop_ii_nacional'"
                    "[entidad])\n\n"
                    "Duracion_en_Dias (columna calculada)\n"
                    "Qué calcula: multiplica por 30 la duración cuando "
                    "unidad_de_duracion es \"Mes(es)\"; para cualquier "
                    "otra unidad devuelve el valor original.\n"
                    "Fórmula: IF('secop_ii_nacional'"
                    "[unidad_de_duracion] = \"Mes(es)\", "
                    "'secop_ii_nacional'[duracion] * 30, "
                    "'secop_ii_nacional'[duracion])\n"
                    "Cautela: el resultado no convierte años, semanas ni "
                    "horas a días, aunque la columna se llame "
                    "Duracion_en_Dias. En el CSV hay 50 registros en años, "
                    "2 en semanas, 17 en horas y 8 \"No Especificado\". "
                    "Antes de analizarla como días, conviertan cada unidad "
                    "o excluyan/documenten las unidades no comparables.\n\n"
                    "Participación porcentual\n"
                    "En el gráfico circular es el porcentaje del total "
                    "visible después de aplicar filtros; no es una medida "
                    "DAX explícita en las fórmulas compartidas."
                ),
            },
        ],
    },
]
