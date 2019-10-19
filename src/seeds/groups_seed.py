from src.models import db, Event, Team, Group

TEAMS_PER_GROUP_COUNT = 5

def run_groups_seed():
    groups = []
    groups_count = db.session.query(Group.id).count()
    
    if groups_count:
        return

    event = Event.query.first()
    teams_count = db.session.query(Team.id).count()
    groups_quantity = teams_count // TEAMS_PER_GROUP_COUNT
    
    for x in range(groups_quantity):
        groups.append(
            Group(name=f'Grupo {x + 1}', event_id=event.id)
        )
    
    db.session.bulk_save_objects(groups)
    db.session.commit()
