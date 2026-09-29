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
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Estructura y orden del flujo",
                "contenido": (
                    "El paquete SSIS (Package.dtsx) tiene un Control Flow con una "
                    "sola tarea, un Data Flow Task, donde ocurre todo el tratamiento. "
                    "Antes de SSIS, un script de Python en Google Colab hizo la "
                    "limpieza inicial y creó las banderas de riesgo; el archivo "
                    "secop_ii_limpio_para_ssis.csv, con 9.792 registros y 59 "
                    "columnas, es la entrada del flujo."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Etapas del flujo de datos",
                "encabezados": ["Etapa", "Componente y función"],
                "filas": [
                    ["Origen", "Flat File Source lee el CSV mediante un administrador de conexión de archivo plano."],
                    ["Nulos", "Conditional Split separa los registros con nulos y Derived Column los corrige."],
                    ["Duplicados", "Sort elimina las filas repetidas."],
                    ["Formatos", "Derived Column normaliza texto, fechas y montos."],
                    ["Tipos de dato", "Data Conversion ajusta los tipos para el paso de CSV a Excel."],
                    ["Unión", "Union All reúne el flujo corregido con los registros válidos."],
                    ["Destino", "Excel Destination genera Datos_Limpios.xlsx y Rechazados.xlsx."],
                ],
            },
        ],
    },
    {
        "slug": "componentes-necesarios-para-el-tratamiento-de-los-datos",
        "numero": "03",
        "titulo": "Componentes necesarios para el tratamiento de los datos",
        "resumen": "",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Herramientas utilizadas y función de cada una en el flujo de limpieza",
                "contenido": (
                    "El tratamiento se hizo en dos herramientas. Primero, un script de "
                    "Python (pandas) ejecutado en Google Colab limpió el archivo crudo "
                    "secop_ii_raw.csv, creó las banderas de riesgo y exportó "
                    "secop_ii_limpio_para_ssis.csv (9.792 registros y 59 columnas). "
                    "Luego, un paquete SSIS (Package.dtsx) con un Data Flow Task "
                    "reproduce el flujo ETL con componentes equivalentes y entrega "
                    "Datos_Limpios.xlsx y Rechazados.xlsx.\n\n"
                    "Componentes:\n"
                    "- Google Colab (pandas y numpy): lee el CSV crudo, elimina "
                    "duplicados, trata nulos, ajusta tipos, calcula las banderas de "
                    "riesgo y exporta el CSV limpio.\n"
                    "- Flat File Source: lee el CSV de SECOP II y expone las columnas "
                    "al flujo.\n"
                    "- Conditional Split: separa los registros con nulos en columnas "
                    "clave mediante condiciones ISNULL unidas con ||.\n"
                    "- Sort: ordena los datos y elimina duplicados.\n"
                    "- Derived Column (nulos): reemplaza nulos con REPLACENULL.\n"
                    "- Derived Column (formatos): normaliza texto, convierte fechas y "
                    "limpia montos.\n"
                    "- Data Conversion: ajusta los tipos de dato.\n"
                    "- Union All: reúne los registros corregidos con los que ya eran "
                    "válidos.\n"
                    "- Excel Destination: escribe los datos tratados y los registros "
                    "enviados a revisión."
                ),
            },
        ],
    },
    {
        "slug": "tratamiento-de-valores-nulos-duplicados-formatos-inconsistentes-y-valores-invalidos-o-atipicos",
        "numero": "04",
        "titulo": "Tratamiento de valores nulos, duplicados, formatos inconsistentes y valores inválidos o atípicos",
        "resumen": "",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Tratamiento aplicado",
                "contenido": (
                    "El diagnóstico de la Etapa 2 identificó problemas de valores "
                    "nulos, duplicados, formatos inconsistentes, valores inválidos "
                    "y valores atípicos. Conditional Split y Derived Column "
                    "tratan los nulos; Sort elimina duplicados; Derived Column "
                    "normaliza texto, fechas y montos; Data Conversion ajusta los "
                    "tipos de dato; y Python calcula flag_atipico_valor mediante "
                    "el rango intercuartílico (IQR)."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Evidencia en los datos de entrada",
                "encabezados": ["Problema", "Lo que se observó", "Resultado"],
                "filas": [
                    ["Nulos", "7 columnas de fecha con nulos", "Tratados con Conditional Split y Derived Column"],
                    ["Datos sin definir", "9.496 registros con 'No Definido' en el NIT del proveedor", "Unificados como 'NO DEFINIDO'"],
                    ["Duplicados", "208 registros repetidos en el archivo crudo", "0 duplicados exactos y 0 por id_del_proceso"],
                    ["Mayúsculas y espacios", "Celdas de texto sin mayúsculas y con espacios sobrantes", "Texto normalizado con UPPER(TRIM())"],
                    ["Fechas", "Formato ISO y valores con T00:00:00.000", "Formato d/mm/aaaa en el resultado"],
                    ["Montos inválidos", "323 valores de precio_base en 0", "Sin regla que los excluya"],
                    ["Atípicos", "706 registros marcados por flag_atipico_valor", "Requiere revisión del umbral"],
                ],
            },
        ],
    },
    {
        "slug": "reglas-aplicadas-y-ajustes-realizados",
        "numero": "05",
        "titulo": "Reglas aplicadas y ajustes realizados",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Reglas de limpieza y ajustes realizados",
                "contenido": (
                    "Las reglas provienen del diagnóstico de la Etapa 2. Las de "
                    "limpieza se programaron en Python y tienen su equivalente en "
                    "componentes de SSIS. Se trataron los duplicados por "
                    "id_del_proceso, se conservaron las filas con nulos para "
                    "mantener la trazabilidad, codigo_entidad se convirtió a texto, "
                    "se excluyeron descripci_n_del_procedimiento y ppi, y se "
                    "normalizaron las fechas al formato d/mm/aaaa."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Reglas aplicadas",
                "encabezados": ["Regla", "Criterio", "Casos marcados"],
                "filas": [
                    ["Duplicados", "Fila exacta repetida o id_del_proceso repetido (se conserva el último)", "Registros: 10.000 a 9.792 (verificar en Colab)"],
                    ["Nulos", "Reemplazo por texto explícito en lugar de eliminar la fila", "Sin eliminación de filas"],
                    ["flag_consistencia_proveedores", "proveedores_unicos_con > proveedores_invitados", "628"],
                    ["flag_adjudicacion_cero", "Valor adjudicado 0, precio base > 0 y adjudicado = 'Si'", "0"],
                    ["flag_directa_sin_just", "Modalidad 'directa' con justificación 'Sin justificación'", "0"],
                    ["flag_atipico_valor", "Valor adjudicado mayor que Q3 + 1,5 x IQR", "706"],
                ],
            },
            {
                "tipo": "texto",
                "subtitulo": "Trazabilidad de la ejecución",
                "contenido": "Entrada y salida de SSIS: 9.792 filas de entrada y 9.792 de salida.",
            },
        ],
    },
    {
        "slug": "conteos-de-registros",
        "numero": "06",
        "titulo": "Conteos de registros recibidos, aceptados, duplicados y enviados a revisión",
        "resumen": "",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Lectura de los conteos",
                "contenido": (
                    "El archivo crudo tenía 10.000 registros. Colab eliminó 208 "
                    "registros repetidos y dejó 9.792 registros para SSIS. El "
                    "flujo recibió y devolvió 9.792 registros, por lo que no se "
                    "eliminaron filas durante esa etapa. La repetición del lote "
                    "no debe duplicar registros porque Sort elimina repetidos."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Conteos por etapa",
                "encabezados": ["Etapa", "Registros", "Observación"],
                "filas": [
                    ["Archivo crudo (secop_ii_raw.csv)", "10.000", "Cifra del informe; verificar en Colab"],
                    ["Duplicados eliminados en Colab", "208", "Exactos y por id_del_proceso"],
                    ["Entrada a SSIS", "9.792", "59 columnas, 0 duplicados"],
                    ["Salida final (Data_Final.xlsx)", "9.792", "55 columnas, 0 duplicados"],
                    ["Aceptados con datos perdidos", "1.834", "Sin precio_base ni fecha_de_publicacion_del"],
                ],
            },
            {
                "tipo": "texto",
                "subtitulo": "Incidencia detectada",
                "contenido": (
                    "Los 1.834 registros aceptados con datos perdidos se detectaron "
                    "al comparar la entrada con la salida: los valores existían en "
                    "el CSV de entrada y desaparecieron durante el paso por SSIS."
                ),
            },
        ],
    },
    {
        "slug": "mejoras-obtenidas-y-problemas-pendientes",
        "numero": "07",
        "titulo": "Mejoras obtenidas y problemas pendientes",
        "resumen": "",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Balance de la calidad lograda",
                "contenido": (
                    "Se compara el estado de los datos a la entrada de SSIS, "
                    "proveniente de Colab, con el resultado final. Se obtuvo un "
                    "registro por proceso, se conservaron las filas para mantener "
                    "la trazabilidad, se generaron cuatro indicadores de riesgo, "
                    "se homogeneizó el texto y el proceso quedó reproducible "
                    "mediante el script de Python y el paquete .dtsx."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Entrada a SSIS frente a resultado final",
                "encabezados": ["Indicador", "Entrada a SSIS", "Resultado final"],
                "filas": [
                    ["Filas", "9.792", "9.792"],
                    ["Columnas", "59", "55 (sin las 4 banderas)"],
                    ["Duplicados exactos", "0", "0"],
                    ["Nulos en precio_base", "0", "1.834"],
                    ["Nulos en fecha_de_publicacion_del", "0", "1.834"],
                    ["Nulos en fecha_de_ultima_publicaci", "0", "8.793"],
                    ["Nulos en fecha_de_publicacion_fase_3", "270", "9.342"],
                ],
            },
            {
                "tipo": "texto",
                "subtitulo": "Problemas pendientes",
                "contenido": (
                    "Data_Final.xlsx no incluye las cuatro banderas de riesgo. "
                    "flag_atipico_valor marca todo valor mayor que 0 (706 casos), "
                    "porque 9.086 de 9.792 valores adjudicados son 0 y el IQR es 0. "
                    "flag_adjudicacion_cero y flag_directa_sin_just dan 0 casos. "
                    "Además, 1.834 filas perdieron precio_base y "
                    "fecha_de_publicacion_del durante el paso por SSIS; las "
                    "columnas de fecha quedaron casi vacías, la guía usa un "
                    "umbral fijo de 150 millones para el atípico y los datos del "
                    "proveedor siguen en 'NO DEFINIDO' en su mayoría."
                ),
            },
        ],
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
