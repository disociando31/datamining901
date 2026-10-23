# Informe de Power BI de la etapa 4

El archivo `Etapa4.pbix` contiene cuatro páginas que se muestran desde el
submenú correspondiente de la aplicación:

| Submenú | Página del informe |
| --- | --- |
| Composición y Distribución | Composición |
| Comparación Territorial | Territorio |
| Análisis Multivariado | Multivariado |
| Comportamiento Temporal | Temporalidad |

## Visualización en la aplicación

El PBIX local no se puede renderizar directamente en un navegador. La
aplicación ya usa la URL pública de Power BI compartida por el equipo. Si se
reemplaza, configura `POWERBI_EMBED_URL` en el entorno donde se ejecuta Flask.
La aplicación agrega automáticamente el parámetro `pageName` correspondiente
a cada submenú.

Los gráficos integrados responden a los segmentadores del informe. Los
hallazgos escritos en la página web son interpretaciones fijas del corte
documentado y no se recalculan al cambiar filtros ni cuando se actualiza el
modelo. Para tener narrativas dinámicas, deben construirse dentro de Power BI
con medidas DAX y mostrarse en tarjetas o cuadros de texto vinculados a esas
medidas.

No publiques datos sensibles mediante **Publicar en la web**: ese modo puede
hacer el informe accesible públicamente. Utiliza una opción de inserción
autenticada y los permisos/licencias requeridos por la organización cuando
corresponda.

Si la variable no está configurada, la página explica que el informe todavía
no está conectado. No incluyas credenciales ni tokens privados en el código
fuente.

## Hallazgos de la revisión de la rúbrica

- Las cuatro páginas del PBIX tienen visualizaciones y al menos tres tarjetas
  de indicadores. La página **Composición** tiene una sola visual de
  segmentación; `estado_del_procedimiento` aparece como proyección inactiva en
  esa visual, así que debe agregarse un segundo segmentador independiente.
- Las páginas del PBIX muestran título y pregunta, pero no los tres
  conocimientos completos de ocho elementos. Los textos de la aplicación no
  se insertan automáticamente dentro del PBIX; deben añadirse allí para
  cumplir literalmente ese requisito.
- La pregunta de **Composición** del PBIX menciona presupuesto y orden de la
  entidad, pero sus visuales desglosan conteos por modalidad, tipo y
  departamento; agrega visuales que respondan la pregunta o ajusta esa
  pregunta en Power BI.
- La pregunta de **Temporalidad** del PBIX habla de evolución mensual del
  volumen publicado; los gráficos temporales actuales muestran principalmente
  valores adjudicados por mes. Ajusta la pregunta o agrega el conteo mensual
  de registros para que la evidencia responda exactamente.
- El cuadro de pregunta de **Multivariado** conserva un título de
  “Composición y Distribución”; corrígelo en Power BI.
- Las expresiones DAX de `Cantidad Procesos`, `Contrato Mas Caro`,
  `Presupuesto Total`, `Promedio Adjudicado`, `Promedio Oferentes` y
  `Total Entidades`, además de la columna calculada `Duracion_en_Dias`, fueron
  compartidas por el equipo y están documentadas en la sección “Datos y DAX”
  de la aplicación. `Duracion_en_Dias` solo convierte meses a 30 días; años,
  semanas, horas y unidades no especificadas quedan sin convertir.
- El PBIX y los hallazgos revisados corresponden al CSV de 10.000 filas. La
  etapa 3 describe un resultado de SSIS de 9.792 filas, que no está presente en
  el repositorio. Confirma si el informe debe actualizarse con ese archivo
  tratado antes de la entrega final.
