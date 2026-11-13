# Conocimiento Oculto: ejecución corregida

Esta revisión sustituye las cifras activas del dashboard por resultados calculados
con los archivos versionados. No reproduce retrospectivamente las capturas del
millón de filas ni la antigua exportación de seis clusters.

## Qué datos generan cada resultado

| Producto | Entrada | Alcance |
|---|---|---|
| Supervisado nuevo | `dataset/processed/secop_ii_nacional.csv` → `etapa6/datos/supervisado.tab` | 10.000 filas originales; 9.792 procesos únicos; 208 repeticiones retiradas con iguales variables seleccionadas y objetivo |
| Clustering nuevo | `etapa6/datos/clustering_4000.tab` | 4.000 procesos de esos 9.792; semilla de muestra 42; sin `adjudicado` |
| Métricas históricas del millón | CSV no incluido en el repositorio | No reproducibles con el CSV de 10.000; se retiraron de la presentación activa |
| Seis grupos y 173 alertas históricos | `etapa6/resultados/*muestra_4000.csv` | Solo antecedentes; faltan los registros exactos y su preparación para reproducirlos; no se trasladan al nuevo experimento |
| YouTube revisado | `etapa6/datos/youtube/privado/comentarios_recibidos_anonimizados.csv` (no publicado) | 36 recibidos; cero vacíos; cero duplicados; un descarte; 35 retenidos |

Los hashes de entradas y el detalle de preparación están en
`etapa6/datos/procedencia.json`; las versiones y hashes de scripts, en
`etapa6/resultados/verificados/ejecucion.json`.

## Instalar y repetir

Python 3.12, desde la raíz del repositorio. Mantener separado el entorno analítico
del servidor Flask. En PowerShell:

```powershell
py -3.12 -m venv .venv-orange
.\.venv-orange\Scripts\Activate.ps1
python -m pip install -r requirements-orange.txt
python etapa6/preparar_datos.py
python etapa6/reproducir.py
python etapa6/generar_flujos.py
python etapa6/youtube_preparar.py --csv etapa6/datos/youtube/privado/comentarios_recibidos_anonimizados.csv --metadata etapa6/datos/youtube/procedencia_corpus.json --revision etapa6/datos/youtube/privado/codificacion_asistida.csv
python etapa6/analizar_textos.py
python etapa6/verificar.py
```

En Linux/macOS: `python3.12 -m venv .venv-orange` y
`source .venv-orange/bin/activate`; los comandos posteriores son iguales.
Los pasos no requieren volver a descargar SECOP. Regenerar desde una API pública
cambiante no garantiza recuperar la misma instantánea: los CSV versionados y sus
hashes son la referencia de esta evaluación.

Para Flask basta `python -m pip install -r requirements.txt` y `python app.py`.
La web lee resultados guardados y no entrena modelos al servir páginas.
No requiere Orange instalado en el hosting.

## Abrir los flujos de Orange

Conservar la estructura completa `etapa6/workflows/` y `etapa6/datos/`.
Abrir cada `.ows` en Orange; File usa una ruta `basedir` relativa al flujo.
Descargar un `.ows` aislado desde Flask no descarga automáticamente sus datos.
Para texto hace falta Orange3-Text 1.16.3 (incluido en requirements-orange.txt). Ejecutar analizar_textos.py antes de abrir el flujo para instalar los recursos locales congelados.

### Supervisado

File → Data de Test and Score. Preprocess (media/moda) → **Preprocessor** de
Test and Score. Los tres learners → Learner de Test and Score. Nunca conectar
un dataset globalmente imputado como entrada de evaluación. No se ha usado Rank
para seleccionar variables mirando todos los objetivos.

Test and Score: validación estratificada de 10 folds, semilla interna 42;
seleccionar `Si` para las métricas de la clase positiva. La API de Orange exporta
predicciones fuera de muestra, fold, probabilidades y matriz de cada modelo.
Confusion Matrix: seleccionar **Tree**; no atribuir la antigua imagen a un modelo.

- Naive Bayes: predeterminados; discretización dentro del entrenamiento.
- Tree: profundidad máxima 10, mínimo 10 por hoja y 20 para dividir,
  mayoría suficiente 95%.
- Random Forest: 10 árboles, mínimo 5 para dividir, max_features=sqrt,
  entrenamiento replicable (semilla 0).

Selección: mayor F1 de `Si`; desempate MCC y nombre. Tree: F1 0,7904;
matriz TN=8.909, FP=174, FN=132, TP=577. El 92,76% de accuracy se consigue
prediciendo siempre No, por lo que accuracy sola no basta.

Los predictores son departamento, orden, modalidad, tipo, unidad de duración,
precio base, duración y número de lotes. Se excluyen estado, fase, respuestas,
participación, adjudicatario, montos adjudicados, nombres e IDs como Features.
No hay historial que pruebe los valores exactos al publicar: la evaluación es
retrospectiva, con etiquetas del estado registrado; no equivale a adjudicación
final futura ni a detección de fraude. La selección sobre estos folds requiere
prueba externa y no demuestra superioridad estadística de Tree.

### Clustering

Se seleccionan 4.000 procesos **antes** de ajustar cualquier transformación.
Precio y proveedores se transforman con log1p; se guardan como Features derivadas.
Los originales son metas para interpretar. Impute (media/moda) → Continuize
(z-score numéricas, one-hot completo categorías) → K-Means. El objetivo supervisado
no está en el archivo. La participación es descriptiva aquí, nunca un predictor
anticipado de adjudicación en el supervisado.

Se compara K=2..8, K-Means++, 10 reinicios, 300 iteraciones, semilla 0.
La normalización interna de K-Means está desactivada. K=3 obtiene Silhouette
0,6088, calculado por distancia euclidiana sobre las 4.000 observaciones.
Sin logaritmos K=2 obtiene 0,9711, pero con tamaños 1 y 3.999: segmentación
poco útil dominada por un extremo. Se conserva la comparación de sensibilidad.
Los nombres C1–C3 no corresponden a los históricos C1–C6.

El campo tipo_de_contrato contiene la categoría literal `No`: se conserva
como dificultad documentada de calidad, no se interpreta como tipo contractual
válido. Un cero de proveedores no demuestra falta de competencia. La muestra
SECOP de origen usa cuotas mensuales y primeras fechas; no es una muestra
aleatoria representativa del país. Falta evaluar estabilidad entre semillas.

### YouTube

El CSV recibido contiene 36 comentarios; `fecha` es su publicación, **no la
extracción**. Su intervalo es 2025-11-10 a 2026-10-11. No se conocen fecha
histórica de consulta, total anterior al CSV, búsqueda original ni paginación.
La asociación al video M6aisVwwkEg procede del flujo previo, porque el CSV
no contiene video_id. Estas limitaciones están en `procedencia_corpus.json`.

Se preserva una entrada local anonimizada para revisión autorizada; solo se normalizaron espacios
y una mención nominal al editor. El hash del original recibido también queda
registrado. No se publican nombres de autores ni claves API.

Limpieza: NFKC, HTML y espacios; vacíos; duplicados por texto normalizado sin
mayúsculas. Se descarta `manzana*` por corrección aislada sin contexto analizable.
Se conservan críticas, elogios, audio y comentarios ambiguos para contrastar
contenido institucional con recepción del video. Todos los textos retenidos
están en español; no se tradujeron. Los emojis no determinan por sí solos el tono.

`privado/codificacion_asistida.csv` (no publicada) permite revisar decisiones por comentario. La
codificación fue realizada por el asistente de IA: **no es una validación humana
independiente ni un patrón oro de sentimiento**. Se asigna un tema principal:
8 valor educativo, 9 percepción de sesgo, 10 corrupción/competencia/control,
6 calidad/formato y 2 reacciones ambiguas. Los temas pueden coexistir; elegir
uno principal facilita conteos sin afirmar que sean categorías naturales únicas.

El sentimiento cualitativo global se etiqueta positivo, negativo, mixto, neutro
o incierto; debe distinguirse si evalúa el video o las instituciones. Los casos
irónicos o sin contexto quedan inciertos. No se interpreta el sentimiento como
opinión representativa de la población ni como prueba sobre procesos SECOP.

Para una **nueva** extracción verificable, configurar YOUTUBE_API_KEY en el
entorno o Secrets de Colab y ejecutar:

```powershell
python etapa6/youtube_extraer_comentarios.py --criterio "Describir selección real" --busqueda "Describir búsqueda o selección manual"
```

El script guarda CSV y metadatos en `datos/youtube/privado/` (ignorado por git).
Usa commentThreads.list, primer nivel, orden temporal, paginación y máximo 500;
no recoge respuestas. Una consulta nueva no reconstruye la extracción pasada.
Posibles restricciones: cuotas, permisos, comentarios deshabilitados/eliminados,
orden temporal y límite de extracción. No publicar el archivo original sin
revisar datos personales en el texto.

## Conclusiones y productos pendientes

El supervisado caracteriza la asociación del diseño con adjudicación registrada;
el clustering muestra perfiles de participación/precio; los comentarios aportan
percepciones de control y sesgo junto a reacciones al video. Un comentario sobre
empresas que simulan competencia plantea una hipótesis útil: contar proveedores
no revela beneficiarios comunes. SECOP y este corpus no permiten comprobarla.

Priorizar calidad de registros, comparación entre perfiles y revisión documental
contextualizada. Ningún modelo identifica corrupción verificada. El sentimiento
del video no puede trasladarse a un contrato ni a la población.

Antes de entregar como trabajo final: incorporar o declarar irrecuperables los
metadatos históricos de extracción; contrastar la codificación por el equipo;
verificar URL pública de Flask y enlace de sustentación (aún no aportados).
El informe técnico se marca como borrador mientras falten estos productos.

## Referencias técnicas

- Orange, Test and Score: https://orangedatamining.com/widget-catalog/evaluate/testandscore/
- Orange, Preprocess: https://orangedatamining.com/widget-catalog/data/preprocess/
- Orange, k-Means: https://orangedatamining.com/widget-catalog/unsupervised/kmeans/
- Orange Text Mining: https://orange3-text.readthedocs.io/
- YouTube Data API, commentThreads.list: https://developers.google.com/youtube/v3/docs/commentThreads/list
- SECOP II Procesos de Contratación: https://www.datos.gov.co/resource/p6dx-8zbt.json

## Ejecución textual verificada

Orange3-Text 1.16.3: unigramas, stopwords españolas congeladas, TF-IDF y L2;
LSI de tres componentes con semilla 42 en API (la GUI no expone esta semilla).
Se conservan los términos, pesos y versiones en youtube_texto.json. Los signos
de los componentes no son sentimiento. La agrupación jerárquica con coseno,
enlace promedio y máximo tres grupos devuelve uno por empates: no se interpreta
como segmentación temática útil. No se inventan grupos a partir del dendrograma.

Multilingual Sentiment (es), con lexicones congelados: 12 puntuaciones positivas,
10 negativas y 13 iguales a cero. Cero no prueba neutralidad. El signo coincide
con 11 de 23 etiquetas asistidas comparables, excluyendo mixtos e inciertos;
no es validación contra humanos ni justifica usarlo como conclusión principal.
La interpretación temática se apoya en textos y codificación explícita.

Los recursos se instalan desde el repositorio en las cachés de Orange con
analizar_textos.py, sin depender de descargas remotas de diccionarios. Los hashes
identifican las versiones; sus fuentes se documentan en recursos/README.md.

## Borrador PDF y sustentación

`informe_tecnico_borrador.pdf` está integrado como descarga en las tres ramas de
Flask. Para regenerarlo: instalar `requirements-informe.txt` y ejecutar
`python etapa6/generar_informe.py`. No instalar ReportLab en el hosting solo para
servir el PDF ya generado. La guía de tiempos para el video está en la última
página; el archivo de video y su enlace todavía no se han aportado.

## Acceso al corpus y privacidad

El repositorio público contiene solo resultados agregados del texto. El corpus
completo, las etiquetas por comentario y sus puntuaciones individuales están en
`etapa6/datos/youtube/privado/`, excluido de git y de las rutas de descarga.
Para ejecutar ese flujo hace falta una copia autorizada del CSV aportada por el
equipo, o una nueva extracción con autorización propia. La codificación asistida
puede volver a hacerse con el procedimiento documentado; no se reconstruyen
comentarios de fuentes públicas para eludir esta limitación.

Los análisis supervisado y clustering de SECOP sí incluyen sus entradas públicas
exactas. No se afirma que un tercero pueda reconstruir el corpus histórico de
YouTube únicamente a partir del repositorio.
