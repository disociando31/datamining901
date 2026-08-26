# -*- coding: utf-8 -*-
"""
app.py
=============================================================================
PUNTO DE ENTRADA de la aplicación Flask.

Este archivo es intencionalmente pequeño: solo crea la aplicación Flask
y registra en ella el Blueprint "main_bp" que está definido en routes.py.

Organización del proyecto:
    app.py          -> crea y arranca la aplicación (este archivo)
    routes.py        -> define las rutas / URLs (usa un Blueprint)
    contenido.py      -> contiene todo el texto/contenido del proyecto
    templates/        -> plantillas HTML (base.html, index.html, submenu.html)
    static/style.css  -> estilos visuales de toda la aplicación

Para ejecutar la aplicación:
    1. (Opcional) crea un entorno virtual:  python -m venv venv
    2. Instala Flask:                       pip install -r requirements.txt
    3. Ejecuta:                             python app.py
    4. Abre en el navegador:                http://127.0.0.1:5000
=============================================================================
"""
from flask import Flask

# Importamos el Blueprint con todas las rutas desde routes.py
from routes import main_bp


def create_app() -> Flask:
    """
    Función 'factory' que crea y configura la aplicación Flask.
    Usar una función factory (en vez de crear 'app' directamente aquí)
    es una buena práctica: facilita hacer pruebas y reutilizar la app.
    """
    app = Flask(__name__)

    # Registramos el Blueprint que contiene todas las rutas
    # (definidas en routes.py: "/", "/etapa1/<slug>", etc.)
    app.register_blueprint(main_bp)

    return app


# Instancia de la aplicación que Flask usará para ejecutarse
app = create_app()


if __name__ == "__main__":
    # debug=True: recarga automática y mensajes de error detallados
    # (Recuerda ponerlo en False si algún día despliegas esto en producción)
    app.run(debug=True)
