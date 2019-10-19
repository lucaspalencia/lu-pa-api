from enum import Enum


class MatchStatus(Enum):
    STANDBY = 'standby'
    LIVE = 'live'
    OVER = 'over'
