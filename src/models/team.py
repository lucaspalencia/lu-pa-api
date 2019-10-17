from datetime import datetime
from . import db


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    
    # relationships
    won_events = db.relationship('Event', backref='won_team', lazy=True)

    # timestamps
    created_on = db.Column(db.DateTime, default=datetime.now)
    updated_on = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    __tablename__ = 'teams'
