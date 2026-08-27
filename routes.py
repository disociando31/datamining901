# -*- coding: utf-8 -*-

"""
routes.py
=============================================================================

Define las rutas de la aplicación mediante un Blueprint de Flask.

Rutas:
    "/"                  -> Página de inicio
    "/etapa1/<slug>"     -> Submenús de la Etapa 1

=============================================================================
"""

from flask import Blueprint, render_template, abort

from contenido import INFO_PROYECTO, ETAPAS, SUBMENUS_ETAPA_1


main_bp = Blueprint("main", __name__)


def _buscar_submenu(slug: str, lista_submenus: list) -> dict | None:
    """
    Busca dentro de una lista de submenús el que tenga el slug indicado.

    Args:
        slug: Identificador único del submenú.
        lista_submenus: Lista de diccionarios de submenús.

    Returns:
        El diccionario del submenú encontrado o None.
    """
    for submenu in lista_submenus:
        if submenu["slug"] == slug:
            return submenu

    return None


@main_bp.route("/")
def index():
    """
    Página de inicio del proyecto.
    """
    return render_template(
        "index.html",
        info=INFO_PROYECTO
    )


@main_bp.route("/etapa1/<string:slug>")
def etapa1_submenu(slug):
    """
    Muestra una sección específica de la Etapa 1.

    El slug identifica uno de los ocho apartados obligatorios:
        1. Problema y contexto
        2. Pregunta principal y preguntas secundarias
        3. Necesidades de información
        4. Fuentes de datos
        5. Dataset
        6. Diccionario de datos
        7. Calidad inicial de los datos
        8. Limitaciones y consideraciones
    """

    submenu = _buscar_submenu(
        slug,
        SUBMENUS_ETAPA_1
    )

    if submenu is None:
        abort(404)

    return render_template(
        "submenu.html",
        submenu=submenu
    )


@main_bp.app_context_processor
def inyectar_datos_globales():
    """
    Hace disponibles los datos globales en todas las plantillas.
    """

    return {
        "etapas": ETAPAS,
        "submenus_etapa_1": SUBMENUS_ETAPA_1,
        "info_proyecto": INFO_PROYECTO,
    }


@main_bp.app_errorhandler(404)
def pagina_no_encontrada(error):
    """
    Página personalizada para errores 404.
    """

    return render_template(
        "404.html",
        info=INFO_PROYECTO
    ), 404