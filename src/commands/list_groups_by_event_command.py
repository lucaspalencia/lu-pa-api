from src.models.group import Group
from src.dtos.groups import Groups as GroupsDtos


class ListGroupsByEventCommand():
    def execute(self, event_id):
        groups = Group.query.filter_by(event_id=event_id).all()
        return GroupsDtos(groups).items
