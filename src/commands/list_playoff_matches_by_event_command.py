from src.models.playoff_match import PlayoffMatch
from src.dtos.playoff_matches import PlayoffMatches as PlayoffMatchesDtos

from sqlalchemy import desc


class ListPlayoffMatchesByEventCommand():
    def execute(self, event_id):
        playoff_matches = PlayoffMatch.query \
            .filter_by(event_id=event_id) \
            .order_by(desc(PlayoffMatch.date)) \
            .all()
        return PlayoffMatchesDtos(playoff_matches).items
