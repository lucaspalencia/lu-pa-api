class ApplicationError(Exception):
    def __init__(self, message, details=None):
        self.name = self.__class__.__name__
        self.message = message
        self.details = details if details else {}

    def to_dict(self):
        return {
            **self.details,
            'name': self.name,
            'message': self.message
        }
