import random

from src.models import db, Group, Event, PlayoffMatch
from src.models.match_status import MatchStatus

from pprint import pprint

MAX_ROUNDS = 16

import logging

def get_classified_teams(group_matches):
    teams_results = []

    for match in group_matches:
        team1 = match.team1
        team2 = match.team2
        t1_score = match.team1_score
        t2_score = match.team2_score


        team1_results = next((x for x in teams_results if x['team'] == team1), None)
        team2_results = next((x for x in teams_results if x['team'] == team2), None)
    
        if (not team1_results):
            teams_results.append({
                'team': team1,
                'points': 1 if t1_score > t2_score else 0,
                'rounds_won': t1_score
            })
        else:
            if (t1_score > t2_score): team1_results['points'] += 1
            team1_results['rounds_won'] += t1_score
        
        if (not team2_results):
            teams_results.append({
                'team': team2,
                'points': 1 if t2_score > t1_score else 0,
                'rounds_won': t2_score
            })
        else:
            if (t2_score > t1_score): team2_results['points'] += 1
            team2_results['rounds_won'] += t2_score
    
    teams_results_sorted = sorted(
        teams_results,
        key=lambda x: [x['points'], x['rounds_won']],
        reverse=True
    )

    return teams_results_sorted[:2]

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
            team1_score = 18
            match_finished = True

    return {
        'team1': team1_score,
        'team2': team2_score
    }

def run_playoff_matches_seed():
    teams = []
    playoff_matches_count = db.session.query(PlayoffMatch.id).count()
    
    if playoff_matches_count:
        return
    
    event = Event.query.first()
    playoff_matches_teams = create_playoff_matches_teams()
    
    logging.debug('========= PlayOff Matches Teams ========')
    print(len(playoff_matches_teams))
    pprint(playoff_matches_teams)

    playoff_matches = []

    playoff_round_winners = []

    for playoff_match_teams in playoff_matches_teams:
        team1 = playoff_match_teams[0]['team']
        team2 = playoff_match_teams[1]['team']
        
        match_scores = simulate_match(team1, team2)
        team1_score = match_scores['team1']
        team2_score = match_scores['team2']

        winner_team = playoff_match_teams[0] if team1_score > team2_score else playoff_match_teams[1]

        playoff_match = create_playoff_match(event, team1, team2, team1_score, team2_score)
        playoff_matches.append(playoff_match)

        playoff_round_winners.append(winner_team)
    
    playoff_matches_teams = list(group_teams(playoff_round_winners, 2))
    logging.debug('========= PlayOff Matches Teams ========')
    print(len(playoff_matches_teams))
    pprint(playoff_matches_teams)

    playoff_matches = []

    playoff_round_winners = []

    for playoff_match_teams in playoff_matches_teams:
        team1 = playoff_match_teams[0]['team']
        team2 = playoff_match_teams[1]['team']
        
        match_scores = simulate_match(team1, team2)
        team1_score = match_scores['team1']
        team2_score = match_scores['team2']

        winner_team = playoff_match_teams[0] if team1_score > team2_score else playoff_match_teams[1]

        playoff_match = create_playoff_match(event, team1, team2, team1_score, team2_score)
        playoff_matches.append(playoff_match)

        playoff_round_winners.append(winner_team)
    
    playoff_matches_teams = list(group_teams(playoff_round_winners, 2))
    logging.debug('========= PlayOff Matches Teams ========')
    print(len(playoff_matches_teams))
    pprint(playoff_matches_teams)

    playoff_matches = []

    playoff_round_winners = []

    for playoff_match_teams in playoff_matches_teams:
        team1 = playoff_match_teams[0]['team']
        team2 = playoff_match_teams[1]['team']
        
        match_scores = simulate_match(team1, team2)
        team1_score = match_scores['team1']
        team2_score = match_scores['team2']

        winner_team = playoff_match_teams[0] if team1_score > team2_score else playoff_match_teams[1]

        playoff_match = create_playoff_match(event, team1, team2, team1_score, team2_score)
        playoff_matches.append(playoff_match)

        playoff_round_winners.append(winner_team)

    playoff_matches_teams = list(group_teams(playoff_round_winners, 2))
    logging.debug('========= PlayOff Matches Teams ========')
    print(len(playoff_matches_teams))
    pprint(playoff_matches_teams)

    playoff_matches = []

    playoff_round_winners = []

    for playoff_match_teams in playoff_matches_teams:
        team1 = playoff_match_teams[0]['team']
        team2 = playoff_match_teams[1]['team']
        
        match_scores = simulate_match(team1, team2)
        team1_score = match_scores['team1']
        team2_score = match_scores['team2']

        winner_team = playoff_match_teams[0] if team1_score > team2_score else playoff_match_teams[1]

        playoff_match = create_playoff_match(event, team1, team2, team1_score, team2_score)
        playoff_matches.append(playoff_match)

        playoff_round_winners.append(winner_team)

    playoff_matches_teams = list(group_teams(playoff_round_winners, 2))
    logging.debug('========= PlayOff Matches Teams GRAND FINAL ========')
    print(len(playoff_matches_teams))
    pprint(playoff_matches_teams)

    # db.session.bulk_save_objects(playoff_matches)
    # db.session.commit()

def create_playoff_match(event, team1, team2, team1_score, team2_score):
    return PlayoffMatch(
        date = '2019-10-17 06:09:38',
        status = MatchStatus.OVER.value,
        event_id = event.id,
        team1_id = team1.id,
        team1_score = team1_score,
        team2_id = team2.id,
        team2_score = team2_score
    )

def create_playoff_matches_teams():
    groups = Group.query.all()
    playoff_teams = []
    
    for group in groups:
        logging.debug(f'========= {group.name} classified ========')
        classified_teams = get_classified_teams(group.matches)
        pprint(classified_teams)
        playoff_teams += classified_teams
    
    random.shuffle(playoff_teams)

    return list(group_teams(playoff_teams, 2))


def group_teams(inputs, n):
    iters = [iter(inputs)] * n
    return zip(*iters)

    
    

