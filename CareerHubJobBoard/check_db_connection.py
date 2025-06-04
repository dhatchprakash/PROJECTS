# database.py

import pyodbc
from util.db_property_util import DBProperties

# Function to get a connection to the database
def get_db_connection():
    try:
        conn = pyodbc.connect(
            driver=DBProperties.DRIVER,
            server=DBProperties.HOSTNAME,
            database=DBProperties.DBNAME,
            trusted_connection='yes'
        )
        return conn
    except pyodbc.Error as e:
        print(f"Error connecting to database: {e}")
        return None


def check_database_connection():
    try:
        # Attempt to establish a connection to the database
        connection = get_db_connection()

        if connection is None:
            print("Failed to connect to the database.")
            return

        # If the connection is successful, execute a simple query
        cursor = connection.cursor()
        cursor.execute('SELECT 1')  # This is a simple query just to verify the connection

        # If no exception occurs, the connection is successful
        print("Database connection is successful!")
        cursor.close()
        connection.close()

    except pyodbc.Error as e:
        print(f"Error connecting to database: {e}")


if __name__ == '__main__':
    check_database_connection()
