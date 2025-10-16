from flask import Flask
import os
from src.models import Contacto
import click
from src.extensions import db

def create_app(config_object:str| None = None) -> Flask:

    app = Flask(__name__)
    _load_config(app, config_object)
    _register_extensions(app)
    _register_cli(app)
    _register_blueprints(app)
    return app

def _register_extensions(app: Flask) -> None:
    from src.extensions import db, migrate
    db.init_app(app)
    migrate.init_app(app, db)


def _load_config(app: Flask, config_object: str | None) -> None:
    app.config.from_object("src.config.BaseConfig")
    if config_object:
        app.config.from_object(config_object)
    else:
        env_config = os.environ.get("ENV_CONFIG", "DevelopmentConfig")
        app.config.from_object(f"src.config.{env_config}")


def _register_cli(app: Flask) -> None:
    @app.cli.command("seed")
    def seed():
        if Contacto.query.first():
            click.echo("Base de Datos ya sembrada")
            return
        
        c1 = Contacto(nombre="Carlos", tel="6647491327", desc="--")
        db.session.add(c1)
        db.session.commit()

        click.echo("Base de datos sembrada")

def _register_blueprints(app: Flask) -> None:
    from src.api.contactos import bp as ContactBP

    app.register_blueprint(ContactBP, url_prefix = "/contactos")