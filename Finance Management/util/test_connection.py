import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from util.db_conn_util import DBConnUtil


try:
    conn = DBConnUtil.get_connection()
    print("Database connection successful!")
    conn.close()
except Exception as e:
    print("Failed to connect to the database.")
    print(f"Error: {e}")
