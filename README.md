# Minería de Datos — Contratación Pública y Gestión de Recursos

Aplicación Flask para documentar las etapas del proyecto y explorar el dataset
SECOP II Nacional. La Etapa 5 agrega un modelo dimensional SQLite y cuatro
consultas interactivas ejecutadas desde el mismo modelo.

## Requisitos

- Python 3.10 o posterior.
- Las dependencias web de `requirements.txt` (Flask y Gunicorn).
- El módulo SQLite incluido en la biblioteca estándar de Python.
- El CSV tratado que ya utiliza el proyecto:
  `dataset/processed/secop_ii_nacional.csv`.

Las visualizaciones de Etapa 5 se construyen en el navegador con HTML, CSS y
JavaScript nativos; no requieren una biblioteca de gráficas ni un servicio
externo. Power BI continúa siendo el mecanismo de visualización documentado
para la Etapa 4.

El ETL de la Etapa 5 usa únicamente la biblioteca estándar de Python. Algunos
scripts previos de construcción/diagnóstico de datos importan `pandas` o
`requests`; no forman parte del camino de carga ni del arranque descrito aquí.

## Instalación y carga del modelo

Desde la raíz del repositorio, en Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python etl\load_star_schema.py
python etl\validate_star_schema.py
```

El ETL lee el CSV sin modificarlo y crea/reconstruye `data/etapa5.sqlite`.
Omitirá filas exactamente duplicadas, conservará filas distintas con el mismo
`id_del_proceso` y registrará el conteo de origen y de destino. La carga puede
usar rutas explícitas:

```powershell
python etl\load_star_schema.py --csv ruta\secop_ii_nacional.csv --db ruta\etapa5.sqlite
python etl\validate_star_schema.py --csv ruta\secop_ii_nacional.csv --db ruta\etapa5.sqlite
```

La base SQLite generada no se versiona; puede reconstruirse en cualquier
momento ejecutando el ETL sobre el CSV incluido en el proyecto.

## Ejecutar Flask

```powershell
python app.py
```

La aplicación local se sirve en [http://127.0.0.1:5000](http://127.0.0.1:5000).
La portada contiene el enlace **Ver etapa 5**; sus páginas son `/etapa5` y
`/etapa5/explorar/<vista>`. La API de lectura comienza en
`/etapa5/api/<vista>`. Si la base todavía no se generó, ejecuta el ETL y vuelve
a cargar la página.

## Etapa 5

- SQL parametrizado de referencia y consultas de aplicación: `queries/`
- Esquema SQLite: `sql/schema.sql`
- Carga y validaciones reproducibles: `etl/`

Las consultas distinguen filas, `COUNT(DISTINCT id_del_proceso)`, sumas y
promedios. Los promedios se recalculan por nivel; no se suman porcentajes ni
promedios. Las comparaciones temporales usan los mismos pares de mes y día
observados en todos los años comparados; tanto sus indicadores como sus
gráficos usan ese corte equivalente. Los resultados son descriptivos y no
implican causalidad.
