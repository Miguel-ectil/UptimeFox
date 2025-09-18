from flask import Flask
from app.extensions import db, migrate
from app.config import Config
from app.routes import site_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensões
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar rotas
    app.register_blueprint(site_routes.bp)

    return app
