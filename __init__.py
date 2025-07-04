from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config


db: SQLAlchemy = SQLAlchemy()
migrate: Migrate = Migrate()

def crear_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(obj=Config)

    db.init_app(app=app)
    migrate.init_app(app, db)

    from .routes import contacto_bp

    app.register_blueprint(contacto_bp)

    return app