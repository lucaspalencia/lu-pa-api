from .event_seed import run_events_seed
from .teams_seed import run_teams_seed
from .groups_seed import run_groups_seed
from .group_teams_seed import run_group_teams_seed
from .group_matches import run_group_matches_seed
from .playoff_matches import run_playoff_matches_seed


def run_seeds():
    run_events_seed()
    run_teams_seed()
    run_groups_seed()
    run_group_teams_seed()
    run_group_matches_seed()
    run_playoff_matches_seed()
