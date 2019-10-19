import random
import logging

from pprint import pprint
from datetime import datetime

from src.models import db, Group, Event, PlayoffMatch
from src.models.match_status import MatchStatus
from src.common.match_simulator import MatchSimulator
from src.common.datetime_format import ISO_DATETIME_FORMAT


def run_playoff_matches_seed():
    playoff_matches_count = db.session.query(PlayoffMatch.id).count()

    if playoff_matches_count:
        return

    event = Event.query.first()

    playoff_matches_teams = create_playoff_matches_teams()
    event_finished = False
    playoff_matches = []

    while(not event_finished):
        logging.debug('========= Playoff Matches ========')
        pprint(playoff_matches_teams)

        playoff_round = simulate_playoff_round(playoff_matches_teams, event)

        matches = playoff_round['matches']
        winners = playoff_round['round_winners']

        playoff_matches += matches

        playoff_matches_teams = list(group_teams(winners, 2))

        if (len(winners) == 1):
            event_finished = True
            logging.debug('========= Event Winner ========')
            pprint(winners[0]['team'])
            event.won_team_id = winners[0]['team'].id

    # db.session.bulk_save_objects(playoff_matches)
    # db.session.add(event)
    # db.session.commit()


def simulate_playoff_round(playoff_matches_teams, event):
    round_winners = []
    matches = []

    for playoff_match_teams in playoff_matches_teams:
        team1 = playoff_match_teams[0]
        team2 = playoff_match_teams[1]

        match_scores = MatchSimulator.simulate_match(
            team1['team'], team2['team']
        )
        team1_score = match_scores['team1']
        team2_score = match_scores['team2']

        team1['rounds_won'] += team1_score
        team2['rounds_won'] += team2_score

        playoff_match = create_playoff_match(
            event,
            team1['team'],
            team2['team'],
            team1_score,
            team2_score
        )

        winner_team = team1 if team1_score > team2_score else team2

        matches.append(playoff_match)
        round_winners.append(winner_team)

    return {
        'round_winners': round_winners,
        'matches': matches
    }


def create_playoff_match(event, team1, team2, team1_score, team2_score):
    return PlayoffMatch(
        date=datetime.now().strftime(ISO_DATETIME_FORMAT),
        status=MatchStatus.OVER.value,
        event_id=event.id,
        team1_id=team1.id,
        team1_score=team1_score,
        team2_id=team2.id,
        team2_score=team2_score
    )


def get_playoff_teams():
    groups = Group.query.all()
    playoff_teams = []

    for group in groups:
        classified_teams = group.get_classified_teams()
        logging.debug(f'========= {group.name} classified teams ========')
        pprint(classified_teams)
        playoff_teams += classified_teams

    return playoff_teams


def create_playoff_matches_teams():
    playoff_teams = get_playoff_teams()
    random.shuffle(playoff_teams)

    return list(group_teams(playoff_teams, 2))


def group_teams(inputs, n):
    iters = [iter(inputs)] * n
    return zip(*iters)
