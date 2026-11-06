# -*- coding: utf-8 -*-


import os
import sqlite3
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from flask import Blueprint, abort, current_app, jsonify, render_template, request

from contenido import INFO_PROYECTO, ETAPAS
from submenu import SUBMENUS_ETAPA_1
from submenu2 import SUBMENUS_ETAPA_2
from submenu3 import SUBMENUS_ETAPA_3
from submenu4 import SUBMENUS_ETAPA_4
from submenu5 import SUBMENUS_ETAPA_5
from queries.olap import InvalidSelection, VIEWS, overview_data, view_data


main_bp = Blueprint("main", __name__)

PAGINAS_POWER_BI = {
    "composicion-y-distribucion": "db66590281a598b19287",
    "comparacion-territorial": "2c4aea5678e5d860631a",
    "analisis-multivariado": "a3446f618144b6ce03d7",
    "comportamiento-temporal": "eea5386badcb2c7496ea",
}
POWERBI_EMBED_URL_DEFAULT = (
    "https://app.powerbi.com/view?r="
    "eyJrIjoiZGM2N2NlNzEtZWFhMC00N2M0LTgwYTctMWMzODA4Yzc0NmVmIiwidCI6"
    "IjA3ZGE2N2EwLTFmNDMtNGU4Yy05NzdmLTVmODhiNjQ3MGVlNiIsImMiOjR9"
)


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


def _url_pagina_power_bi(page_name: str) -> str | None:
    embed_url = os.environ.get(
        "POWERBI_EMBED_URL",
        POWERBI_EMBED_URL_DEFAULT,
    ).strip()
    if not embed_url:
        return None

    partes = urlsplit(embed_url)
    if partes.scheme not in {"http", "https"} or not partes.netloc:
        raise ValueError("POWERBI_EMBED_URL debe ser una URL HTTP o HTTPS válida.")

    query = [
        (clave, valor)
        for clave, valor in parse_qsl(partes.query, keep_blank_values=True)
        if clave != "pageName"
    ]
    query.append(("pageName", page_name))

    return urlunsplit(
        (
            partes.scheme,
            partes.netloc,
            partes.path,
            urlencode(query),
            partes.fragment,
        )
    )


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
        submenu=submenu,
        etapa_numero=1,
        submenus=SUBMENUS_ETAPA_1,
        ruta_endpoint="main.etapa1_submenu",
    )


@main_bp.route("/etapa2/<string:slug>")
def etapa2_submenu(slug):
    """
    Muestra una sección específica de la Etapa 2.
    """

    submenu = _buscar_submenu(
        slug,
        SUBMENUS_ETAPA_2
    )

    if submenu is None:
        abort(404)

    return render_template(
        "submenu.html",
        submenu=submenu,
        etapa_numero=2,
        submenus=SUBMENUS_ETAPA_2,
        ruta_endpoint="main.etapa2_submenu",
    )


@main_bp.route("/etapa3/<string:slug>")
def etapa3_submenu(slug):
    """
    Muestra una sección específica de la Etapa 3.
    """

    submenu = _buscar_submenu(
        slug,
        SUBMENUS_ETAPA_3
    )

    if submenu is None:
        abort(404)

    return render_template(
        "submenu.html",
        submenu=submenu,
        etapa_numero=3,
        submenus=SUBMENUS_ETAPA_3,
        ruta_endpoint="main.etapa3_submenu",
    )


@main_bp.route("/etapa4/<string:slug>")
def etapa4_submenu(slug):
    """
    Muestra una sección específica de la Etapa 4.
    """

    if slug == "objetivos":
        slug = "conocimiento-evidente"

    submenu = _buscar_submenu(
        slug,
        SUBMENUS_ETAPA_4
    )

    if submenu is None:
        abort(404)

    return render_template(
        "submenu.html",
        submenu=submenu,
        etapa_numero=4,
        submenus=SUBMENUS_ETAPA_4,
        ruta_endpoint="main.etapa4_submenu",
        powerbi_page_name=PAGINAS_POWER_BI.get(slug),
        powerbi_page_url=(
            _url_pagina_power_bi(PAGINAS_POWER_BI[slug])
            if slug in PAGINAS_POWER_BI
            else None
        ),
    )


@main_bp.route("/etapa5")
def etapa5():
    try:
        resumen_etapa5 = overview_data()
    except FileNotFoundError as error:
        resumen_etapa5 = None
        error_modelo = str(error)
    else:
        error_modelo = None
    return render_template(
        "etapa5/modelo.html",
        etapa_numero=5,
        submenus=SUBMENUS_ETAPA_5,
        resumen_etapa5=resumen_etapa5,
        error_modelo=error_modelo,
    )


@main_bp.route("/etapa5/explorar/<string:slug>")
def etapa5_explorar(slug):
    submenu = next(
        (item for item in SUBMENUS_ETAPA_5 if item["slug"] == slug),
        None,
    )
    if submenu is None or slug not in VIEWS:
        abort(404)
    return render_template(
        "etapa5/explorar.html",
        etapa_numero=5,
        submenus=SUBMENUS_ETAPA_5,
        submenu=submenu,
        view_config=VIEWS[slug],
    )


@main_bp.route("/etapa5/api/<string:slug>")
def etapa5_api(slug):
    if slug not in VIEWS:
        abort(404)
    try:
        payload = view_data(slug, request.args)
    except InvalidSelection as error:
        return jsonify({"error": str(error)}), 400
    except FileNotFoundError as error:
        return jsonify({"error": str(error)}), 503
    except sqlite3.Error:
        current_app.logger.exception("Error al consultar el modelo OLAP de Etapa 5.")
        return jsonify(
            {"error": "No se pudo consultar el modelo multidimensional."}
        ), 500
    return jsonify(payload)


@main_bp.app_context_processor
def inyectar_datos_globales():
    """
    Hace disponibles los datos globales en todas las plantillas.
    """

    return {
        "etapas": ETAPAS,
        "submenus_etapa_1": SUBMENUS_ETAPA_1,
        "submenus_etapa_2": SUBMENUS_ETAPA_2,
        "submenus_etapa_3": SUBMENUS_ETAPA_3,
        "submenus_etapa_4": SUBMENUS_ETAPA_4,
        "submenus_etapa_5": SUBMENUS_ETAPA_5,
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