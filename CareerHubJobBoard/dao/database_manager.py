import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pyodbc
from util.db_conn_util import get_db_connection
from dao.job_listing_dao import JobListingDAO
from dao.company_dao import CompanyDAO
from dao.applicant_dao import ApplicantDAO
from dao.job_application_dao import JobApplicationDAO
from entity.job_listing import JobListing
from entity.company import Company
from entity.applicant import Applicant
from entity.job_application import JobApplication

class DatabaseManager:
    def __init__(self):
        self.conn = get_db_connection()

    def initialize_database(self):
        """Initializes the database by executing the schema.sql file."""
        try:
            with open("database/schema.sql", "r") as schema_file:
                schema_script = schema_file.read()
            cursor = self.conn.cursor()
            cursor.execute(schema_script)
            self.conn.commit()
            print("Database initialized successfully.")
        except Exception as e:
            print(f"Error initializing the database: {e}")
    
    def insert_job_listing(self, job_listing: JobListing):
        """Inserts a new job listing into the Jobs table."""
        try:
            job_listing_dao = JobListingDAO(self.conn)
            job_listing_dao.insert_job_listing(job_listing)
            print("Job listing added successfully.")
        except Exception as e:
            print(f"Error inserting job listing: {e}")
    
    def insert_company(self, company: Company):
        """Inserts a new company into the Companies table."""
        try:
            company_dao = CompanyDAO(self.conn)
            company_dao.insert_company(company)
            print("Company added successfully.")
        except Exception as e:
            print(f"Error inserting company: {e}")

    def insert_applicant(self, applicant: Applicant):
        """Inserts a new applicant into the Applicants table."""
        try:
            applicant_dao = ApplicantDAO(self.conn)
            applicant_dao.insert_applicant(applicant)
            print("Applicant added successfully.")
        except Exception as e:
            print(f"Error inserting applicant: {e}")

    def insert_job_application(self, job_application: JobApplication):
        """Inserts a new job application into the Applications table."""
        try:
            job_application_dao = JobApplicationDAO(self.conn)
            job_application_dao.insert_job_application(job_application)
            print("Job application added successfully.")
        except Exception as e:
            print(f"Error inserting job application: {e}")
    
    def get_all_job_listings(self):
        """Retrieves all job listings."""
        try:
            job_listing_dao = JobListingDAO(self.conn)
            return job_listing_dao.get_all_job_listings()
        except Exception as e:
            print(f"Error retrieving job listings: {e}")
            return []

    def get_all_companies(self):
        """Retrieves all companies."""
        try:
            company_dao = CompanyDAO(self.conn)
            return company_dao.get_all_companies()
        except Exception as e:
            print(f"Error retrieving companies: {e}")
            return []

    def get_all_applicants(self):
        """Retrieves all applicants."""
        try:
            applicant_dao = ApplicantDAO(self.conn)
            return applicant_dao.get_all_applicants()
        except Exception as e:
            print(f"Error retrieving applicants: {e}")
            return []

    def get_applications_for_job(self, job_id: int):
        """Retrieves all applications for a specific job listing."""
        try:
            job_application_dao = JobApplicationDAO(self.conn)
            return job_application_dao.get_applications_for_job(job_id)
        except Exception as e:
            print(f"Error retrieving job applications for job ID {job_id}: {e}")
            return []
