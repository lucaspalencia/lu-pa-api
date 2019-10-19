from src.models import db, Team, Group

TEAMS_PER_GROUP_QUANTITY = 5


def create_group_teams(teams, quantity):
    for i in range(0, len(teams), quantity):
        yield teams[i:i+quantity]


def run_group_teams_seed():
    group_teams_count = db.session \
        .execute('SELECT count(*) from group_teams') \
        .fetchone()[0]

    if group_teams_count:
        return

    teams = Team.query.all()
    groups = Group.query.all()

    group_teams = list(create_group_teams(teams, TEAMS_PER_GROUP_QUANTITY))

    for index, group in enumerate(groups):
        group.teams.extend(group_teams[index])
        db.session.add(group)

    db.session.commit()
