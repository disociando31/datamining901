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
                    "un informe técnico detallado, un enlace a Drive con los "
                    "archivos del proyecto y una captura de muestra, como "
                    "evidencia de la configuración en SSIS, la comparación de "
                    "calidad entre iteraciones y las mejoras obtenidas."
                ),
            },
        ],
    },
    {
        "slug": "proceso-tratamiento-ssis",
        "numero": "02",
        "titulo": "Proceso de tratamiento en SSIS",
        "resumen": "",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Estructura y orden del flujo",
                "contenido": (
                    "El paquete SSIS (Package.dtsx) tiene un Control Flow con una "
                    "sola tarea Data Flow Task, donde ocurre el tratamiento. "
                    "El proceso parte de secop_ii_limpio_para_ssis.csv, con "
                    "9.792 registros y 59 columnas."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Etapas del flujo de datos",
                "encabezados": ["Etapa", "Componente y función"],
                "filas": [
                    ["Origen", "Flat File Source lee el CSV mediante un administrador de conexión de archivo plano."],
                    ["Nulos", "Conditional Split separa los registros con nulos; Derived Column los corrige y renombra columnas con nombres inconsistentes."],
                    ["Duplicados", "Sort elimina las filas repetidas."],
                    ["Formatos", "Derived Column normaliza texto (UPPER y TRIM), fechas y montos."],
                    ["Tipos de dato", "Data Conversion ajusta los tipos al pasar de CSV a Excel."],
                    ["Unión", "Union All reúne el flujo corregido con el de registros válidos."],
                    ["Destino", "Excel Destination escribe los datos tratados en Datos_Limpios.xlsx y los registros enviados a revisión en Rechazados.xlsx."],
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
                    "Luego, un paquete SSIS (Package.dtsx) con un Data Flow Task "
                    "reproduce el flujo ETL con componentes equivalentes y entrega "
                    "Datos_Limpios.xlsx \n\n"
                    "Componentes:\n"
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
        "slug": "tratamiento-nulos-duplicados-formatos",
        "numero": "04",
        "titulo": "Tratamiento de valores nulos, duplicados, formatos inconsistentes y valores inválidos o atípicos",
        "resumen": "",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Qué problema se encontró y cómo se trató",
                "contenido": (
                    "El diagnóstico de la Etapa 2 identificó problemas en los "
                    "datos de contratación pública. Para cada uno se definió "
                    "una regla de tratamiento y se asignó un componente de SSIS.\n\n"
                    "Valores nulos: Conditional Split detecta nulos con ISNULL; "
                    "Derived Column los reemplaza con REPLACENULL. En Python se "
                    "rellenaron nombre_del_procedimiento y "
                    "justificacion_modalidad_de sin eliminar filas.\n\n"
                    "Duplicados: en Sort se eliminaron filas repetidas y se "
                    "conservó el último registro por id_del_proceso, ya que SECOP "
                    "publica adendas como registros nuevos.\n\n"
                    "Formatos inconsistentes: Derived Column normaliza espacios "
                    "y mayúsculas con UPPER(TRIM()), convierte fechas con "
                    "(DT_DATE) y limpia caracteres de los montos. codigo_entidad "
                    "se trató como texto.\n\n"
                    "Valores inválidos o atípicos: Data Conversion ajusta los "
                    "tipos de montos y fechas; los valores extremos y en cero "
                    "requieren revisión y no se excluyen automáticamente."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Evidencia en los datos de entrada",
                "encabezados": ["Problema", "Lo que se observó", "Resultado"],
                "filas": [
                    ["Nulos", "7 columnas de fecha con nulos (por ejemplo, fecha_de_publicacion con 9.721 y fecha_adjudicacion con 9.103)", "Tratados con Conditional Split y Derived Column"],
                    ["Datos sin definir", "9.496 registros con 'No Definido' en el NIT del proveedor", "Unificados como 'NO DEFINIDO'"],
                    ["Duplicados", "Se revisaron registros repetidos antes del flujo SSIS", "La línea base de la etapa es de 9.792 registros"],
                    ["Mayúsculas y espacios", "236.875 celdas de texto sin mayúsculas y 3 con espacios sobrantes", "Texto normalizado con UPPER(TRIM())"],
                    ["Fechas", "Formato ISO, algunas con T00:00:00.000", "Formato d/mm/aaaa en el resultado"],
                    ["Montos inválidos", "323 valores de precio_base en 0", "Sin regla que los excluya"],
                    ["Valores extremos", "precio_base con un máximo de 599.971.286.503", "Sin tratamiento automático"],
                    ["Atípicos", "706 registros marcados por flag_atipico_valor", "Requiere revisar el umbral"],
                ],
            },
        ],
    },
    {
        "slug": "reglas-y-ajustes",
        "numero": "05",
        "titulo": "Reglas aplicadas y ajustes realizados",
        "resumen": "",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Ajustes realizados",
                "contenido": (
                    "SECOP publica adendas como registros nuevos; se conservó "
                    "el último publicado según la fecha para dejar un registro "
                    "por id_del_proceso. No se eliminaron filas con nulos para "
                    "mantener la trazabilidad; se rellenaron con 'Sin nombre "
                    "registrado' y 'Sin justificación'. codigo_entidad se trató "
                    "como texto para evitar decimales (.0). También se excluyeron "
                    "descripci_n_del_procedimiento y ppi, y las fechas se "
                    "convirtieron al formato d/mm/aaaa."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Reglas aplicadas",
                "encabezados": ["Regla", "Criterio", "Casos marcados"],
                "filas": [
                    ["Duplicados", "Fila exacta o id_del_proceso repetido; se conserva el último", "9.792 registros al inicio de SSIS"],
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
                "contenido": "Entrada y salida de SSIS: 9.792 filas en cada etapa.",
            },
        ],
    },
    {
        "slug": "conteos-registros",
        "numero": "06",
        "titulo": "Conteos de registros recibidos, aceptados, duplicados y enviados a revisión",
        "resumen": "",
        "bloques": [
            {
                "tipo": "texto",
                "subtitulo": "Lectura de los conteos",
                "contenido": (
                    "La línea base de esta etapa es el archivo "
                    "secop_ii_limpio_para_ssis.csv, con 9.792 registros y "
                    "59 columnas. SSIS produjo 9.792 filas en la salida; sin "
                    "embargo, 1.834 presentan pérdidas en precio_base y "
                    "fecha_de_publicacion_del."
                ),
            },
            {
                "tipo": "tabla",
                "subtitulo": "Conteos por etapa",
                "encabezados": ["Etapa", "Registros", "Observación"],
                "filas": [
                    ["Entrada a SSIS (secop_ii_limpio_para_ssis.csv)", "9.792", "59 columnas"],
                    ["Salida final (Data_Final.xlsx)", "9.792", "55 columnas; sin duplicados reportados"],
                ],
            },
            {
                "tipo": "texto",
                "subtitulo": "Incidencia detectada",
                "contenido": (
                    "Los 1.834 registros con datos perdidos se detectaron al "
                    "comparar la entrada con la salida: precio_base y "
                    "fecha_de_publicacion_del tenían valores en el CSV de entrada "
                    "que desaparecieron durante el paso por SSIS. La ejecución "
                    "conservó el total de filas, pero requiere corregir esta pérdida."
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
                    "con el resultado final. Se obtuvo un "
                    "registro por proceso, se conservaron las filas para mantener "
                    "la trazabilidad, se generaron cuatro indicadores de riesgo, "
                    "se homogeneizó el texto y el proceso quedó reproducible "
                    "mediante el paquete .dtsx."
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
        "slug": "archivos-del-proyecto",
        "numero": "08",
        "titulo": "Archivos del proyecto",
        "resumen": "",
        "bloques": [
            {
                "tipo": "enlaces",
                "subtitulo": "Carpeta de archivos en Google Drive",
                "lista": [
                    {
                        "texto": "Abrir carpeta de archivos en Google Drive",
                        "url": "https://drive.google.com/drive/folders/18HiXtIu1i0vYFe4d3ApXkE1afNN4F0pn?usp=sharing",
                    },
                ],
            },
            {
                "tipo": "captura",
                "subtitulo": "Muestra de los archivos",
                "url": "/static/muestra-archivos-drive.png",
                "alt": "Captura de muestra de los archivos del proyecto",
            },
        ],
    },
]
