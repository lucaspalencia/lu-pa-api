import logging

from .event_seed import run_events_seed
from .teams_seed import run_teams_seed
from .groups_seed import run_groups_seed
from .group_teams_seed import run_group_teams_seed
from .group_matches import run_group_matches_seed
from .playoff_matches import run_playoff_matches_seed


def run_seeds():
    logging.info('==== Start executing seeds ====')

    run_events_seed()
    logging.info('events seed executed')
    run_teams_seed()
    logging.info('teams seed executed')
    run_groups_seed()
    logging.info('groups seed executed')
    run_group_teams_seed()
    logging.info('group teams seed executed')
    run_group_matches_seed()
    logging.info('group matches executed')
    run_playoff_matches_seed()
    logging.info('playoff matches executed')

    logging.info('==== Seeds successfully executed ====')
