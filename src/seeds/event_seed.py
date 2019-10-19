from src.models import db, Event
from datetime import datetime

def run_events_seed():
    events_count = db.session.query(Event.id).count()
    
    if events_count:
        return

    event = Event(
        name = 'Evento Teste',
        start_date= '2019-10-17 06:09:38',
        end_date = '2019-11-17 06:09:38',
    )
    
    db.session.add(event)
    db.session.commit()
