from src.common.datetime_format import ISO_DATETIME_FORMAT


class PlayoffMatches():
    def __init__(self, playoff_matches):
        self.items = self.build_itens(playoff_matches)

    def build_itens(self, playoff_matches):
        items = []

        for match in playoff_matches:
            items.append({
                'team1': match.team1.name,
                'team1Score': match.team1_score,
                'team2': match.team2.name,
                'team2Score': match.team2_score,
                'date': match.date.strftime(ISO_DATETIME_FORMAT)
            })

        return items
