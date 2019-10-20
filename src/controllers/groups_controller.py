from flask_restful import Resource
from flask.json import jsonify
from http import HTTPStatus

from src.common.auth import auth
from src.commands.list_groups_by_event_command import ListGroupsByEventCommand


class GroupsController(Resource):
    decorators = [auth]

    def get(self, event_id):
        command = ListGroupsByEventCommand()
        groups = command.execute(event_id)

        return jsonify(
            status=HTTPStatus.OK,
            data=groups
        )
