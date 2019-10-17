from datetime import datetime
from . import db
from src.models.match_status import MatchStatus
from src.models.playoff_match_type import PlayoffMatchType


class PlayoffMatch(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Enum(MatchStatus, name='playoffmatchstatus', values_callable=lambda obj: [e.value for e in obj]))
    type = db.Column(db.Enum(PlayoffMatchType, values_callable=lambda obj: [e.value for e in obj]))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    team1_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    team1_score = db.Column(db.Integer)
    team2_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    team2_score = db.Column(db.Integer)

    # timestamps
    created_on = db.Column(db.DateTime, default=datetime.now)
    updated_on = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    __tablename__ = 'playoff_matches'
