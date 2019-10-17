from datetime import datetime
from . import db


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(300), nullable=False)
    prize_pool = db.Column(db.Numeric())
    location = db.Column(db.String(255))
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    won_team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    
    # relationships
    groups = db.relationship('Group', backref='event', lazy=True)
    playoff_matches = db.relationship('PlayoffMatch', backref='event', lazy=True)

    # timestamps
    created_on = db.Column(db.DateTime, default=datetime.now)
    updated_on = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    __tablename__ = 'events'
