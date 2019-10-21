from flask_restful import Resource
from http import HTTPStatus

from src.common.auth import auth
from src.commands.get_event_command import GetEventCommand


class EventsController(Resource):
    decorators = [auth]

    def get(self, event_id):
        command = GetEventCommand()
        event = command.execute(event_id)

        return event, HTTPStatus.OK
