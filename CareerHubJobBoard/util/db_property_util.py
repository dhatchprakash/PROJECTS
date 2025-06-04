from util.db_conn_util import get_db_connection

def get_database_properties():
    try:
        conn = get_db_connection()
        if conn is None:
            raise Exception("Database connection failed")
        cursor = conn.cursor()
        query = "SELECT DB_NAME() AS DatabaseName, SERVERPROPERTY('MachineName') AS ServerName"
        cursor.execute(query)
        result = cursor.fetchone()
        conn.close()
        if result:
            return result
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
