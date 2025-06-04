import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pyodbc
from entity.job_application import JobApplication
from util.db_conn_util import get_db_connection

class JobApplicationDAO:
    def __init__(self, conn):
        self.conn = conn

    def insert_job_application(self, job_application):
        cursor = self.conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO JobApplications (JobListingID, ApplicantID, ApplicationDate, CoverLetter)
                VALUES (?, ?, ?, ?)
            """, job_application.job_listing_id, job_application.applicant_id,
                job_application.application_date, job_application.cover_letter)
            self.conn.commit()
        except Exception as e:
            print(f"Error inserting job application: {str(e)}")

    def get_job_application_by_id(self, application_id):
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM JobApplications WHERE ApplicationID = ?
        """, application_id)
        result = cursor.fetchone()
        return result
