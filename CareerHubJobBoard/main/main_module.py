import sys
import os
import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dao.job_listing_dao import JobListingDAO
from dao.company_dao import CompanyDAO
from dao.applicant_dao import ApplicantDAO
from dao.job_application_dao import JobApplicationDAO
from util.db_conn_util import get_db_connection
from entity.job_listing import JobListing
from entity.company import Company
from entity.applicant import Applicant
from entity.job_application import JobApplication


def add_job_listing():
    try:
        job_title = input("Enter Job Title: ")
        job_description = input("Enter Job Description: ")
        job_location = input("Enter Job Location: ")
        salary = float(input("Enter Salary: "))
        job_type = input("Enter Job Type (e.g., Full-time, Part-time): ")
        company_id = int(input("Enter Company ID: "))

        conn = get_db_connection()
        company_dao = CompanyDAO(conn)
        existing_company = company_dao.get_company_by_id(company_id)

        if not existing_company:
            print(f"Company with ID {company_id} does not exist!")
            return

        job_listing = JobListing(
            company_id=company_id,
            job_title=job_title,
            job_description=job_description,
            job_location=job_location,
            salary=salary,
            job_type=job_type,
            posted_date=datetime.datetime.now()
        )

        job_listing_dao = JobListingDAO(conn)
        job_listing_dao.insert_job_listing(job_listing)
        print("Job listing added successfully.")
    except Exception as e:
        print(f"Error inserting job listing: {e}")
    finally:
        conn.close()


def add_company():
    try:
        company_name = input("Enter Company Name: ")
        location = input("Enter Company Location: ")

        company = Company(None, company_name, location)

        conn = get_db_connection()
        company_dao = CompanyDAO(conn)
        company_dao.insert_company(company)
        print("Company added successfully.")
    except Exception as e:
        print(f"Error adding company: {str(e)}")
    finally:
        conn.close()


def add_applicant():
    try:
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone: ")
        resume = input("Enter Resume file path: ")

        conn = get_db_connection()
        applicant_dao = ApplicantDAO(conn)

        applicant = Applicant(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            resume=resume
        )
        applicant_dao.insert_applicant(applicant)
        print("Applicant added successfully.")
    except Exception as e:
        print(f"Error adding applicant: {e}")
    finally:
        conn.close()


def apply_for_job():
    try:
        applicant_id = int(input("Enter Applicant ID: "))
        job_listing_id = int(input("Enter Job Listing ID: "))
        cover_letter = input("Enter Cover Letter: ")

        conn = get_db_connection()
        job_application_dao = JobApplicationDAO(conn)
        applicant_dao = ApplicantDAO(conn)
        job_listing_dao = JobListingDAO(conn)

        existing_applicant = applicant_dao.get_applicant_by_id(applicant_id)
        if not existing_applicant:
            print(f"Applicant with ID {applicant_id} does not exist!")
            return

        existing_job = job_listing_dao.get_job_listing_by_id(job_listing_id)
        if not existing_job:
            print(f"Job Listing with ID {job_listing_id} does not exist!")
            return

        job_application = JobApplication(
            applicant_id=applicant_id,
            job_listing_id=job_listing_id,
            cover_letter=cover_letter,
            application_date=str(datetime.date.today())
        )
        job_application_dao.insert_job_application(job_application)
        print("Job application submitted successfully.")
    except Exception as e:
        print(f"Error inserting job application: {e}")
    finally:
        conn.close()


def view_all_job_listings():
    try:
        conn = get_db_connection()
        job_listing_dao = JobListingDAO(conn)
        listings = job_listing_dao.get_all_job_listings()

        company_dao = CompanyDAO(conn)
        companies = {company.company_id: company for company in company_dao.get_all_companies()}

        print("\n--- All Job Listings ---")
        for job in listings:
            company = companies.get(job.company_id)
            if not company:
                print(f"Company with ID {job.company_id} not found. Skipping job listing.")
                continue
            print(f"Title: {job.job_title}, Company: {company.company_name}, Location: {company.location}, Salary: {job.salary}")
    except Exception as e:
        print(f"Error retrieving job listings: {e}")
    finally:
        conn.close()


def search_jobs_by_salary_range():
    try:
        min_salary = float(input("Enter minimum salary: "))
        max_salary = float(input("Enter maximum salary: "))

        conn = get_db_connection()
        job_listing_dao = JobListingDAO(conn)
        results = job_listing_dao.get_jobs_by_salary_range(min_salary, max_salary)

        company_dao = CompanyDAO(conn)
        companies = {company.company_id: company for company in company_dao.get_all_companies()}

        print("\n--- Jobs in Your Salary Range ---")
        for job in results:
            company = companies.get(job.company_id)
            print(f"Title: {job.job_title}, Company: {company.company_name}, Location: {company.location}, Salary: {job.salary}")
    except Exception as e:
        print(f"Error searching jobs: {e}")
    finally:
        conn.close()


def display_menu():
    print("\nWelcome to the CareerHub Job Board System")
    print("1. Add Job Listing")
    print("2. Add Company")
    print("3. Add Applicant")
    print("4. Apply for Job")
    print("5. View All Job Listings")
    print("6. Search Jobs by Salary Range")
    print("7. Exit")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_job_listing()
        elif choice == "2":
            add_company()
        elif choice == "3":
            add_applicant()
        elif choice == "4":
            apply_for_job()
        elif choice == "5":
            view_all_job_listings()
        elif choice == "6":
            search_jobs_by_salary_range()
        elif choice == "7":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
