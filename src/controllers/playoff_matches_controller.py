from flask_restful import Resource
from flask.json import jsonify
from http import HTTPStatus

from src.commands.list_playoff_matches_by_event_command \
    import ListPlayoffMatchesByEventCommand


class PlayoffMatchesController(Resource):
    def get(self, event_id):
        command = ListPlayoffMatchesByEventCommand()
        groups = command.execute(event_id)

        return jsonify(
            status=HTTPStatus.OK,
            data=groups
        )
