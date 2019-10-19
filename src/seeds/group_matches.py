import itertools
import random

from src.models import db, Group, GroupMatch
from src.models.match_status import MatchStatus

MAX_ROUNDS = 16

def simulate_match(team1, team2):
    teams = [team1, team2]
    
    team1_score = 0
    team2_score = 0
    match_finished = False
    
    while(not match_finished):
        round_winner = random.choice(teams)

        if (round_winner == team1): 
            team1_score += 1
        
        if (round_winner == team2):
            team2_score += 1
        
        if (MAX_ROUNDS in [team1_score, team2_score]):
            match_finished = True
        
        if (team1_score == team2_score == 15):
            match_finished = True

    return {
        'team1': team1_score,
        'team2': team2_score
    }

def create_group_matches(group, team1, team2):
    group_matches = []

    match_scores = simulate_match(team1, team2)

    group_matches.append(
        GroupMatch(
            date = '2019-10-17 06:09:38',
            status = MatchStatus.OVER.value,
            group_id = group.id,
            team1_id = team1.id,
            team1_score = match_scores['team1'],
            team2_id = team2.id,
            team2_score = match_scores['team2']
        )
    )

    db.session.bulk_save_objects(group_matches)
    db.session.commit()

def run_group_matches_seed():
    group_matches_count = db.session.query(GroupMatch.id).count()

    if group_matches_count:
        return

    groups = Group.query.all()

    for group in groups:
        teams = group.teams
        # teams_range = range(1, len(teams) + 1)
        group_matches_teams = list(itertools.combinations(teams, 2))

        for group_match_teams in group_matches_teams:
            create_group_matches(group, group_match_teams[0], group_match_teams[1])
