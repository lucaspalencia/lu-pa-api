import itertools

from src.models import db, Group, GroupMatch
from src.models.match_status import MatchStatus
from src.common.match_simulator import MatchSimulator


def create_group_match(group, team1, team2):
    match_scores = MatchSimulator.simulate_match(team1, team2)

    return GroupMatch(
        date='2019-10-17 06:09:38',
        status=MatchStatus.OVER.value,
        group_id=group.id,
        team1_id=team1.id,
        team1_score=match_scores['team1'],
        team2_id=team2.id,
        team2_score=match_scores['team2']
    )


def run_group_matches_seed():
    group_matches_count = db.session.query(GroupMatch.id).count()

    if group_matches_count:
        return

    groups = Group.query.all()
    group_matches = []

    for group in groups:
        teams = group.teams
        # teams_range = range(1, len(teams) + 1)
        group_matches_teams = list(itertools.combinations(teams, 2))

        for group_match_teams in group_matches_teams:
            group_match = create_group_match(
                group,
                group_match_teams[0],
                group_match_teams[1]
            )
            group_matches.append(group_match)

    db.session.bulk_save_objects(group_matches)
    db.session.commit()
