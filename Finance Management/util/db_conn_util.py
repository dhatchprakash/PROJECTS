import pyodbc
from util.db_property_util import DBPropertyUtil

class DBConnUtil:
    _connection = None

    @staticmethod
    def get_connection():
        if DBConnUtil._connection is None or DBConnUtil._connection.closed:
            conn_string = DBPropertyUtil.get_property_string('util/database.properties')
            DBConnUtil._connection = pyodbc.connect(conn_string)
        return DBConnUtil._connection


if __name__ == "__main__":
    print("This is a utility module. Please import it instead of running directly.")
