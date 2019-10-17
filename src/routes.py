from flask import Blueprint
from flask_restful import Api

from src.handlers import HealthCheckHandler

USER_BLUEPRINT = Blueprint('healthcheck', __name__)
Api(USER_BLUEPRINT).add_resource(HealthCheckHandler, '/health')
