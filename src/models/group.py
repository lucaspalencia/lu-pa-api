from datetime import datetime
from . import db


group_teams = db.Table(
    'group_teams',
    db.Column(
        'group_id',
        db.Integer,
        db.ForeignKey('groups.id'),
        primary_key=True
    ),
    db.Column(
        'team_id',
        db.Integer,
        db.ForeignKey('teams.id'),
        primary_key=True
    )
)


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    event_id = db.Column(
        db.Integer,
        db.ForeignKey('events.id'),
        nullable=False
    )

    # relationships
    teams = db.relationship('Team', secondary=group_teams, lazy='subquery')
    matches = db.relationship('GroupMatch', backref='group', lazy=True)

    # timestamps
    created_on = db.Column(db.DateTime, default=datetime.now)
    updated_on = db.Column(
        db.DateTime,
        default=datetime.now,
        onupdate=datetime.now
    )

    __tablename__ = 'groups'

    @property
    def ordered_teams(self):
        teams_results = []

        for match in self.matches:
            team1 = match.team1
            team2 = match.team2
            t1_score = match.team1_score
            t2_score = match.team2_score

            team1_results = next(
                (x for x in teams_results if x['team'] == team1),
                None
            )
            team2_results = next(
                (x for x in teams_results if x['team'] == team2),
                None
            )

            if (not team1_results):
                teams_results.append({
                    'team': team1,
                    'points': 1 if t1_score > t2_score else 0,
                    'rounds_won': t1_score
                })
            else:
                if (t1_score > t2_score):
                    team1_results['points'] += 1

                team1_results['rounds_won'] += t1_score

            if (not team2_results):
                teams_results.append({
                    'team': team2,
                    'points': 1 if t2_score > t1_score else 0,
                    'rounds_won': t2_score
                })
            else:
                if (t2_score > t1_score):
                    team2_results['points'] += 1

                team2_results['rounds_won'] += t2_score

        teams_results_sorted = sorted(
            teams_results,
            key=lambda x: [x['points'], x['rounds_won']],
            reverse=True
        )

        return teams_results_sorted

    def get_classified_teams(self):
        teams_results = self.ordered_teams
        return teams_results[:2]
