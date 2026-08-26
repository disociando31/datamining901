# -*- coding: utf-8 -*-
"""
contenido.py
=============================================================================
Este archivo centraliza TODA la información de texto que se muestra en la
aplicación (nombre del proyecto, participantes y el contenido de cada uno
de los 8 submenús de la "Etapa 1").

¿Por qué un archivo aparte?
- Para que puedas editar el contenido del proyecto SIN tocar la lógica de
  las rutas (routes.py) ni el diseño de las plantillas HTML (templates/).
- Cuando llegue la "Etapa 2", "Etapa 3", etc. solo tienes que agregar un
  nuevo diccionario aquí (ver instrucciones al final del archivo) y un par
  de líneas en routes.py.

Cómo editar tu contenido:
- Reemplaza los textos de ejemplo (marcados como "Escribe aquí...") por la
  información real de tu proyecto.
- Cada submenú es un diccionario dentro de la lista SUBMENUS_ETAPA_1.
- Cada submenú tiene una lista de "bloques". Un bloque puede ser:
    * tipo "texto" -> un subtítulo + un párrafo de contenido.
    * tipo "tabla" -> un subtítulo + encabezados + filas (para mostrar
      información tabular, por ejemplo el diccionario de datos).
- Puedes agregar tantos bloques como necesites en cada submenú.
=============================================================================
"""

# -----------------------------------------------------------------------
# 1. INFORMACIÓN GENERAL DEL PROYECTO (se muestra en la página de inicio)
# -----------------------------------------------------------------------
INFO_PROYECTO = {
    "materia": "Minería de Datos",
    "titulo": "Proyecto de la materia",
    # Agrega o quita nombres según el número real de integrantes.
    "participantes": [
        "Nombre Apellido 1",
        "Nombre Apellido 2",
        "Nombre Apellido 3",
    ],
}

# -----------------------------------------------------------------------
# 2. MENÚ PRINCIPAL
# -----------------------------------------------------------------------
# Cada elemento de esta lista es una "Etapa" que aparecerá como un botón
# en la barra de navegación superior. Por ahora solo existe "Etapa 1",
# pero la estructura ya está lista para que agregues "Etapa 2", "Etapa 3"...
# simplemente copiando este patrón y creando su propia lista de submenús.
ETAPAS = [
    {
        "slug": "etapa-1",          # identificador usado en las URLs
        "nombre": "Etapa 1",        # texto que se muestra en el menú
        "activa": True,             # True = ya tiene contenido disponible
    },
    # Ejemplo de cómo se vería una futura Etapa 2 (queda desactivada):
    # {"slug": "etapa-2", "nombre": "Etapa 2", "activa": False},
]

# -----------------------------------------------------------------------
# 3. SUBMENÚS DE LA ETAPA 1
# -----------------------------------------------------------------------
# "numero" se usa solo para mostrar el número visual (01, 02, ...) ya que
# aquí SÍ existe una secuencia real (los 8 puntos del entregable).
SUBMENUS_ETAPA_1 = [
    {
        "slug": "problema-y-contexto",
        "numero": "01",
        "titulo": "Problema y contexto",
        "resumen": "Descripción del problema que se aborda y el entorno en el que ocurre.",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Descripción del problema",
                "contenido": (
                    "Escribe aquí el problema que motiva el proyecto: ¿qué situación "
                    "actual se quiere entender, mejorar o resolver mediante minería "
                    "de datos?"
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Contexto",
                "contenido": (
                    "Escribe aquí el contexto: sector, organización, población o "
                    "fenómeno estudiado, y por qué es relevante analizarlo en este "
                    "momento."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Justificación",
                "contenido": (
                    "Escribe aquí por qué vale la pena resolver este problema y qué "
                    "impacto tendría encontrar una solución o respuesta."
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
                "contenido": "Escribe aquí la pregunta principal de investigación del proyecto.",
            },
            {
                "tipo": "texto",
                "subtitulo": "Preguntas secundarias",
                "contenido": (
                    "1. Escribe aquí la primera pregunta secundaria.\n"
                    "2. Escribe aquí la segunda pregunta secundaria.\n"
                    "3. Escribe aquí la tercera pregunta secundaria."
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
                "subtitulo": "Información requerida",
                "contenido": (
                    "Escribe aquí qué variables, indicadores o tipos de datos son "
                    "necesarios para poder responder la pregunta principal y las "
                    "preguntas secundarias."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Relación con las preguntas",
                "contenido": (
                    "Escribe aquí cómo cada necesidad de información se relaciona "
                    "directamente con una o varias de las preguntas del punto anterior."
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
                "subtitulo": "Fuentes utilizadas",
                "contenido": (
                    "Escribe aquí las fuentes de datos (portales abiertos, APIs, "
                    "encuestas, bases de datos institucionales, etc.) que se usaron "
                    "o se planean usar."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Detalle de fuentes",
                "encabezados": ["Fuente", "Tipo", "Enlace / referencia", "Fecha de obtención"],
                "filas": [
                    ["Nombre de la fuente 1", "Ej: Portal de datos abiertos", "https://...", "AAAA-MM-DD"],
                    ["Nombre de la fuente 2", "Ej: API pública", "https://...", "AAAA-MM-DD"],
                ],
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
                "subtitulo": "Descripción general",
                "contenido": (
                    "Escribe aquí una descripción general del dataset: número de "
                    "filas, número de columnas, período de tiempo que cubre y "
                    "formato del archivo (csv, xlsx, json, etc.)."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Muestra de los datos",
                "encabezados": ["Columna 1", "Columna 2", "Columna 3", "Columna 4"],
                "filas": [
                    ["Valor ejemplo", "Valor ejemplo", "Valor ejemplo", "Valor ejemplo"],
                    ["Valor ejemplo", "Valor ejemplo", "Valor ejemplo", "Valor ejemplo"],
                    ["Valor ejemplo", "Valor ejemplo", "Valor ejemplo", "Valor ejemplo"],
                ],
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
                "tipo": "tabla",
                "subtitulo": "Variables del dataset",
                "encabezados": ["Variable", "Tipo de dato", "Descripción", "Ejemplo de valor"],
                "filas": [
                    ["nombre_variable_1", "Texto / Numérico / Fecha", "Escribe aquí qué representa", "Ej: 123"],
                    ["nombre_variable_2", "Texto / Numérico / Fecha", "Escribe aquí qué representa", "Ej: Bogotá"],
                    ["nombre_variable_3", "Texto / Numérico / Fecha", "Escribe aquí qué representa", "Ej: 2024-05-10"],
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
                    "Escribe aquí un resumen general del estado de calidad de los "
                    "datos: porcentaje de valores nulos, duplicados encontrados, "
                    "valores atípicos, tipos de datos inconsistentes, etc."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Hallazgos por variable",
                "encabezados": ["Variable", "Problema detectado", "% afectado", "Acción propuesta"],
                "filas": [
                    ["nombre_variable_1", "Ej: valores nulos", "Ej: 5%", "Ej: imputar con la mediana"],
                    ["nombre_variable_2", "Ej: valores duplicados", "Ej: 2%", "Ej: eliminar duplicados"],
                ],
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
                    "Escribe aquí las limitaciones del proyecto: cobertura temporal "
                    "o geográfica de los datos, tamaño de la muestra, disponibilidad "
                    "de información, recursos técnicos, etc."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Consideraciones éticas y de privacidad",
                "contenido": (
                    "Escribe aquí las consideraciones éticas relevantes: manejo de "
                    "datos sensibles, anonimización, consentimiento, sesgos "
                    "potenciales en los datos, etc."
                ),
            },
        ],
    },
]

# -----------------------------------------------------------------------
# 4. PARA AGREGAR UNA NUEVA ETAPA EN EL FUTURO (por ejemplo, Etapa 2)
# -----------------------------------------------------------------------
# 1) Agrega un nuevo diccionario a la lista ETAPAS, por ejemplo:
#       {"slug": "etapa-2", "nombre": "Etapa 2", "activa": True}
# 2) Crea una nueva lista de submenús, por ejemplo SUBMENUS_ETAPA_2,
#    siguiendo exactamente el mismo formato que SUBMENUS_ETAPA_1.
# 3) En routes.py, agrega una nueva ruta "/etapa2/<slug>" que use
#    SUBMENUS_ETAPA_2 (puedes copiar la ruta de la etapa 1 como base).
