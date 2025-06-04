# application_deadline_exception.py
class ApplicationDeadlineException(Exception):
    def __init__(self, message="The application deadline has passed."):
        self.message = message
        super().__init__(self.message)
