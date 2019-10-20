from src.models.event import Event
from src.dtos.event import Event as EventDtos


class GetEventCommand():
    def execute(self, event_id):
        event = Event.query.filter_by(id=event_id).first()
        if not event:
            return {}
        return EventDtos(event).to_dict()
