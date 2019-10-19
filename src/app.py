from flask import Flask
from flask.blueprints import Blueprint

from src.config import config_by_environment
import src.routes as routes

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s",
    datefmt="%d/%m/%y %H:%M:%S",
)

def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(config_by_environment[environment])
    register_blueprints(app)
    return app


def register_blueprints(app):
    for blueprint in vars(routes).values():
        if isinstance(blueprint, Blueprint):
            app.register_blueprint(blueprint)
