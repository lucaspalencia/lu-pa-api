from flask import Blueprint
from flask_restful import Api

from src.controllers import HealthCheckController
from src.controllers import EventsController

USER_BLUEPRINT = Blueprint('healthcheck', __name__)
Api(USER_BLUEPRINT).add_resource(HealthCheckController, '/health')

EVENT_BLUEPRINT = Blueprint('events', __name__)
Api(EVENT_BLUEPRINT).add_resource(EventsController, '/events')
