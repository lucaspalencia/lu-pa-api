from flask_restful import Resource
from flask.json import jsonify
from http import HTTPStatus

from src.commands.get_event_command import GetEventCommand


class EventsController(Resource):
    def get(self, event_id):
        command = GetEventCommand()
        event = command.execute(event_id)

        return jsonify(
            status=HTTPStatus.OK,
            data=event
        )
