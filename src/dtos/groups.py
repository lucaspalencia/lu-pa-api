

class Groups():
    def __init__(self, groups):
        self.items = self.build_itens(groups)

    def build_itens(self, groups):
        items = []

        for group in groups:
            items.append({
                'id': group.id,
                'name': group.name,
                'teams': self.teams_data(group.ordered_teams)
            })

        return items

    def teams_data(self, teams):
        return [
            {
                'id': team['team'].id,
                'name': team['team'].name,
                'points': team['points'],
                'rounds': team['rounds_won']
            }
            for team in teams
        ]
