from flask import Blueprint
from flask_restful import Api

from src.controllers import HealthCheckController
from src.controllers import EventsController
from src.controllers import GroupsController
from src.controllers import PlayoffMatchesController

HEALTH_BLUEPRINT = Blueprint('healthcheck', __name__)

Api(HEALTH_BLUEPRINT).add_resource(
    HealthCheckController,
    '/health'
)

EVENT_BLUEPRINT = Blueprint('event', __name__)
Api(EVENT_BLUEPRINT).add_resource(
    EventsController,
    '/events/<int:event_id>'
)

EVENT_GROUPS_BLUEPRINT = Blueprint('event_groups', __name__)
Api(EVENT_GROUPS_BLUEPRINT).add_resource(
    GroupsController,
    '/events/<int:event_id>/groups'
)

EVENT_PLAYOFF_MATCHES_BLUEPRINT = Blueprint('event_playoff_matches', __name__)
Api(EVENT_PLAYOFF_MATCHES_BLUEPRINT).add_resource(
    PlayoffMatchesController,
    '/events/<int:event_id>/playoff'
)
