
# Submenús de la Etapa 3.
SUBMENUS_ETAPA_3 = [
    {
        "slug": "objetivos",
        "numero": "01",
        "titulo": "Objetivos",
        "resumen": "",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Objetivo general",
                "contenido": (
                    "Implementar y evaluar un proceso ETL iterativo utilizando "
                    "SQL Server Integration Services (SSIS) para la corrección "
                    "de los problemas de calidad de datos identificados en la "
                    "etapa previa, documentando su evolución y publicando los "
                    "resultados y evidencias en la aplicación web del proyecto "
                    "(Flask)."
                ),
            },
            {
                "tipo": "texto",
                "subtitulo": "Objetivos específicos",
                "contenido": (
                    "1. Construir el flujo de integración y limpieza de datos:\n"
                    "Diseñar un paquete ETL en SSIS que extraiga los datos hacia "
                    "una zona de staging y aplique reglas de negocio mediante "
                    "componentes de transformación (Derived Column, Conditional "
                    "Split, Data Conversion, etc.) para gestionar valores nulos, "
                    "duplicados, formatos atípicos y separar los registros que "
                    "requieran revisión manual.\n\n"
                    "2. Validar y optimizar el tratamiento mediante iteraciones:\n"
                    "Ejecutar tres ciclos iterativos del proceso ETL, documentando "
                    "los ajustes realizados en cada fase, comparando los "
                    "indicadores de calidad frente a los datos originales, "
                    "validando los conteos de trazabilidad (recibidos, aceptados, "
                    "rechazados) y garantizando que la ejecución repetida de un "
                    "lote no genere duplicidad.\n\n"
                    "3. Desplegar y sustentar los resultados del proyecto:\n"
                    "Publicar en la sección de la etapa 3 de la aplicación Flask "
                    "un informe técnico detallado y un video de demostración, "
                    "los cuales deben evidenciar el paso a paso de la "
                    "configuración en SSIS, la comparación de calidad entre "
                    "iteraciones y las mejoras obtenidas."
                ),
            },
        ],
    },
    {
        "slug": "proceso-de-tratamiento-en-ssis",
        "numero": "02",
        "titulo": "Proceso de tratamiento en SSIS",
        "resumen": "",
        "bloques": [],
    },
    {
        "slug": "componentes-necesarios-para-el-tratamiento-de-los-datos",
        "numero": "03",
        "titulo": "Componentes necesarios para el tratamiento de los datos",
        "resumen": "",
        "bloques": [],
    },
    {
        "slug": "tratamiento-de-valores-nulos-duplicados-formatos-inconsistentes-y-valores-invalidos-o-atipicos",
        "numero": "04",
        "titulo": "Tratamiento de valores nulos, duplicados, formatos inconsistentes y valores inválidos o atípicos",
        "resumen": "",
        "bloques": [],
    },
    {
        "slug": "reglas-aplicadas-y-ajustes-realizados",
        "numero": "05",
        "titulo": "Reglas aplicadas y ajustes realizados",
        "resumen": "",
        "bloques": [],
    },
    {
        "slug": "conteos-de-registros",
        "numero": "06",
        "titulo": "Conteos de registros recibidos, aceptados, duplicados y enviados a revisión",
        "resumen": "",
        "bloques": [],
    },
    {
        "slug": "mejoras-obtenidas-y-problemas-pendientes",
        "numero": "07",
        "titulo": "Mejoras obtenidas y problemas pendientes",
        "resumen": "",
        "bloques": [],
    },
    {
        "slug": "video-de-demostracion",
        "numero": "08",
        "titulo": "Video de demostración",
        "resumen": "",
        "bloques": [
            {
                "tipo": "video",
                "subtitulo": "Video de demostración",
                "url": "",
            },
        ],
    },
]
