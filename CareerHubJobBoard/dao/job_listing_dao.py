import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pyodbc
from entity.job_listing import JobListing
from util.db_conn_util import get_db_connection
from entity.company import Company

class JobListingDAO:
    def __init__(self, conn):
        self.conn = conn

    def insert_job_listing(self, job_listing):
        try:
            query = """
            INSERT INTO JobListings (CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor = self.conn.cursor()
            cursor.execute(query, (
                job_listing.company_id,
                job_listing.job_title,
                job_listing.job_description,
                job_listing.job_location,
                job_listing.salary,
                job_listing.job_type,
                job_listing.posted_date
            ))
            self.conn.commit()
        except Exception as e:
            print(f"Error inserting job listing: {e}")
            raise

    def get_job_listing_by_id(self, job_listing_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT * FROM JobListings WHERE JobListingID = ?", (job_listing_id,))
            row = cursor.fetchone()
            if row:
                return JobListing(
                    job_listing_id=row.JobListingID,
                    company_id=row.CompanyID,
                    job_title=row.JobTitle,
                    job_description=row.JobDescription,
                    job_location=row.JobLocation,
                    salary=row.Salary,
                    job_type=row.JobType,
                    posted_date=row.PostedDate
                )
            return None
        except Exception as e:
            print(f"Error fetching job listing by ID: {e}")
            raise

    def get_all_job_listings(self):
        try:
            cursor = self.conn.cursor()
            query = '''
                SELECT jl.JobListingID, jl.JobTitle, jl.Salary, jl.CompanyID, c.CompanyName, c.Location
                FROM JobListings jl
                LEFT JOIN Companies c ON jl.CompanyID = c.CompanyID
            '''
            cursor.execute(query)
            rows = cursor.fetchall()
            listings = []

            for row in rows:
                job_listing_id = row[0]
                job_title = row[1]
                salary = row[2]
                company_id = row[3]
                company_name = row[4]
                company_location = row[5] if row[5] else "Unknown Location"

                # Create the company object
                try:
                    company = Company(company_id=company_id, company_name=company_name, location=company_location)
                except TypeError as e:
                    print(f"Error creating company object: {e}")
                    continue

                # Create the job listing object
                job = JobListing(
                    job_listing_id=job_listing_id,
                    job_title=job_title,
                    job_description=None,  # Can be fetched if needed
                    job_location=None,     # Can be fetched if needed
                    salary=salary,
                    job_type=None,         # Can be fetched if needed
                    company_id=company_id,
                    posted_date=None,      # Can be fetched if needed
                    company_name=company_name,
                    company_location=company_location
                )
                listings.append(job)

            return listings
        except Exception as e:
            print(f"Error fetching all job listings: {e}")
            raise

    def get_jobs_by_salary_range(self, min_salary, max_salary):
        try:
            cursor = self.conn.cursor()
            query = """
                SELECT JobListingID, CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate
                FROM JobListings
                WHERE Salary BETWEEN ? AND ?
            """
            cursor.execute(query, (min_salary, max_salary))
            rows = cursor.fetchall()

            job_listings = []
            for row in rows:
                job_listing = JobListing(
                    job_listing_id=row[0],
                    company_id=row[1],
                    job_title=row[2],
                    job_description=row[3],
                    job_location=row[4],
                    salary=row[5],
                    job_type=row[6],
                    posted_date=row[7]
                )
                job_listings.append(job_listing)

            return job_listings
        except Exception as e:
            print(f"Error fetching jobs by salary range: {e}")
            raise
