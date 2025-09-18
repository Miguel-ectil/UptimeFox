from flask import Flask
from app.extensions import db, celery  # vamos definir celery lá também
from app.routes.site_routes import bp as site_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    # Inicializa extensões
    db.init_app(app)

    # Registra blueprint(s)
    app.register_blueprint(site_bp)

    # Registra celery no app.extensions
    app.extensions['celery'] = celery

    return app
