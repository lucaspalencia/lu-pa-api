from datetime import datetime
from . import db


group_teams = db.Table('group_teams',
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id'), primary_key=True),
    db.Column('team_id', db.Integer, db.ForeignKey('teams.id'), primary_key=True)
)

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    
    # relationships
    teams = db.relationship('Team', secondary=group_teams, lazy='subquery')
    matches = db.relationship('GroupMatch', backref='group', lazy=True)

    # timestamps
    created_on = db.Column(db.DateTime, default=datetime.now)
    updated_on = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    
    __tablename__ = 'groups'
