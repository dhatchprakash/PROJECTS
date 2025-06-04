import pyodbc
import configparser
import os

def get_db_connection():
    try:
        config = configparser.ConfigParser()
        path = os.path.join(os.path.dirname(__file__), 'database.properties')  
        config.read(path)

        hostname = config.get('DATABASE', 'hostname')
        dbname = config.get('DATABASE', 'dbname')

        conn_str = f'DRIVER={{SQL Server}};SERVER={hostname};DATABASE={dbname};Trusted_Connection=yes;'
        conn = pyodbc.connect(conn_str)
        return conn
    except pyodbc.Error as e:
        print(f"Error in connection: {e}")
        return None
