from src.common.datetime_format import ISO_DATETIME_FORMAT


class Event():
    def __init__(self, event):
        self.name = event.name
        self.wonTeamName = event.won_team.name if event.won_team else None
        self.startDate = event.start_date.strftime(ISO_DATETIME_FORMAT)
        self.endDate = event.end_date.strftime(ISO_DATETIME_FORMAT)

    def to_dict(self):
        return self.__dict__
