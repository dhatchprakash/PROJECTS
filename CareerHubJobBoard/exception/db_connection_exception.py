# db_connection_exception.py
class DBConnectionException(Exception):
    def __init__(self, message="Could not connect to the database."):
        self.message = message
        super().__init__(self.message)
