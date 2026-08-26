# -*- coding: utf-8 -*-
"""
routes.py
=============================================================================
Este archivo define todas las RUTAS (URLs) de la aplicación usando un
Blueprint de Flask. El archivo app.py importa este Blueprint y lo registra
en la aplicación principal; así mantenemos la lógica de rutas separada del
punto de entrada de la app y del contenido textual (contenido.py).

Rutas definidas:
    "/"                     -> Página de inicio (portada del proyecto)
    "/etapa1/<slug>"        -> Página de un submenú específico de la Etapa 1

Cuando se agregue una nueva etapa (Etapa 2, Etapa 3, ...) solo hay que
copiar el patrón de la ruta "/etapa1/<slug>" cambiando la lista de
contenido que se consulta (ver el punto 4 de contenido.py).
=============================================================================
"""
from flask import Blueprint, render_template, abort

from contenido import INFO_PROYECTO, ETAPAS, SUBMENUS_ETAPA_1

# Un Blueprint permite agrupar rutas y luego registrarlas en la app
# principal (app.py) con app.register_blueprint(main_bp).
main_bp = Blueprint("main", __name__)


def _buscar_submenu(slug: str, lista_submenus: list) -> dict | None:
    """
    Busca dentro de una lista de submenús el que tenga el 'slug' indicado.
    Devuelve el diccionario del submenú o None si no existe.
    """
    for submenu in lista_submenus:
        if submenu["slug"] == slug:
            return submenu
    return None


@main_bp.route("/")
def index():
    """
    Página de inicio (portada).
    Muestra: "Minería de Datos", "Proyecto de la materia" y los
    nombres de los participantes.
    """
    return render_template("index.html", info=INFO_PROYECTO)


@main_bp.route("/etapa1/<string:slug>")
def etapa1_submenu(slug):
    """
    Página de un submenú de la Etapa 1.
    'slug' identifica cuál de los 8 puntos del entregable se debe mostrar
    (por ejemplo: 'problema-y-contexto', 'dataset', etc.).
    Si el slug no existe, se responde con un error 404.
    """
    submenu = _buscar_submenu(slug, SUBMENUS_ETAPA_1)
    if submenu is None:
        abort(404)
    return render_template("submenu.html", submenu=submenu)


@main_bp.app_context_processor
def inyectar_datos_globales():
    """
    Context processor: hace que las variables indicadas estén disponibles
    automáticamente en TODAS las plantillas HTML, sin necesidad de pasarlas
    manualmente en cada 'render_template'. Esto es lo que permite que la
    barra de menú (base.html) siempre pueda dibujar "Etapa 1" y su submenú.
    """
    return {
        "etapas": ETAPAS,
        "submenus_etapa_1": SUBMENUS_ETAPA_1,
        "info_proyecto": INFO_PROYECTO,
    }


@main_bp.app_errorhandler(404)
def pagina_no_encontrada(error):
    """Página de error 404 personalizada (mantiene el mismo diseño del sitio)."""
    return render_template("404.html"), 404
