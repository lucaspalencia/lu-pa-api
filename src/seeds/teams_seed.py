from src.models import db, Team

TEAMS_QUANTITY = 80

def run_teams_seed():
    teams = []
    teams_count = db.session.query(Team.id).count()
    
    if teams_count:
        return

    for x in range(TEAMS_QUANTITY):
        teams.append(
            Team(name=f'Team {x + 1}')
        )
    
    db.session.bulk_save_objects(teams)
    db.session.commit()
