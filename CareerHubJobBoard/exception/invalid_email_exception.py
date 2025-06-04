# invalid_email_exception.py
class InvalidEmailException(Exception):
    def __init__(self, message="Invalid email format."):
        self.message = message
        super().__init__(self.message)
