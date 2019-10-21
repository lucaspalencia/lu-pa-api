from flask_restful import Resource
from http import HTTPStatus

from src.common.auth import auth
from src.commands.list_playoff_matches_by_event_command \
    import ListPlayoffMatchesByEventCommand


class PlayoffMatchesController(Resource):
    decorators = [auth]

    def get(self, event_id):
        command = ListPlayoffMatchesByEventCommand()
        playoff_matches = command.execute(event_id)

        return playoff_matches, HTTPStatus.OK
