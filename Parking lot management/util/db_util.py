import pyodbc

class DBConnection:
    def __init__(self):
        self.conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost;'
            'DATABASE=appdb;'
            'Trusted_Connection=yes;'
        )
        self.cursor = self.conn.cursor()
        self.initialize_schema()

    def initialize_schema(self):
        create_table_query = """
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='ParkingSlots' AND xtype='U')
        CREATE TABLE ParkingSlots (
            slot_id INT IDENTITY(1,1) PRIMARY KEY,
            slot_number VARCHAR(50),
            vehicle_type VARCHAR(50),
            is_occupied BIT,
            assigned_vehicle VARCHAR(100)
        )
        """
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def get_cursor(self):
        return self.cursor

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
