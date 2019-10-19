from flask_restful import Resource
from flask.json import jsonify
from http import HTTPStatus

from src.commands.get_event_command import GetEventCommand
from src.common.application_error import ApplicationError

import logging

class EventsController(Resource):
    def get(self):
        try:
            command = GetEventCommand()
            event = command.execute()

            return jsonify(
                status=HTTPStatus.OK,
                data=event
            )

        except ApplicationError as error:
            return jsonify(
                status=HTTPStatus.BAD_REQUEST,
                data=error.to_dict()
            )
