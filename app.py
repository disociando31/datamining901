# -*- coding: utf-8 -*-
from flask import Flask

# Importamos el Blueprint con todas las rutas desde routes.py
from routes import main_bp


def create_app() -> Flask:
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
