import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pyodbc
from entity.applicant import Applicant
from util.db_conn_util import get_db_connection

class ApplicantDAO:
    def __init__(self, conn):
        self.conn = conn

    def insert_applicant(self, applicant):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO Applicants (FirstName, LastName, Email, Phone, Resume)
                VALUES (?, ?, ?, ?, ?)
            """, applicant.first_name, applicant.last_name, applicant.email, applicant.phone, applicant.resume)
            self.conn.commit()
        except Exception as e:
            print(f"Error inserting applicant: {str(e)}")

    def get_applicant_by_id(self, applicant_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM Applicants WHERE ApplicantID = ?", (applicant_id,))
        row = cursor.fetchone()
        if row:
             return Applicant(row.ApplicantID, row.FirstName, row.LastName, row.Email, row.Phone, row.Resume)
        return None

