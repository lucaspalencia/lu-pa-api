from src.models.event import Event

class GetEventCommand():
    def execute(self):
        event = Event.query.first()
        
        return {
            'name': event.name,
            'startDate': event.start_date,
            'endDate': event.end_date
        }
