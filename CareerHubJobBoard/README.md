# CareerHub Job Board System

The CareerHub Job Board System is a Python-based application that allows users to manage job listings, companies, applicants, and job applications. It utilizes object-oriented programming (OOP) principles and interacts with an MS SQL database for data storage and retrieval.

## Features
1. **Add Job Listing**: Allows users to add new job listings to the system.
2. **Add Company**: Enables adding companies that post job listings.
3. **Add Applicant**: Lets users add applicants who can apply for job listings.
4. **Apply for Job**: Allows applicants to apply for available job listings.
5. **View All Job Listings**: Displays all available job listings.
6. **Search Jobs by Salary Range**: Allows users to search job listings within a specified salary range.

## Prerequisites

Before running the application, ensure you have the following installed:
- Python 3.x
- MS SQL Server 
- Required Python libraries 


## File Structure

careerhub-job-board/
│
├── dao/
│   ├── __init__.py
│   ├── applicant_dao.py
│   ├── company_dao.py
│   ├── database_manager.py
│   ├── job_application_dao.py
│   ├── job_listing_dao.py
│   └── __pycache__/
│
├── database/
│   ├── schema.sql
│
├── entity/
│   ├── __init__.py
│   ├── applicant.py
│   ├── company.py
│   ├── job_application.py
│   ├── job_listing.py
│   └── __pycache__/
│
├── exception/
│   ├── __init__.py
│   ├── application_deadline_exception.py
│   ├── db_connection_exception.py
│   ├── file_upload_exception.py
│   ├── invalid_email_exception.py
│   └── salary_calculation_exception.py
│
├── main/
│   ├── __init__.py
│   ├── main_module.py
│
├── util/
│   ├── __init__.py
│   ├── database.properties
│   ├── db_conn_util.py
│   ├── db_property_util.py
│   
│
└── check_db_connection.py
└── README.md



## Example Interaction

After running python main/main_module.py,
Welcome to CareerHub Job Board System!
Please select an option:
1. Add Job Listing
2. Add Company
3. Add Applicant
4. Apply for Job
5. View All Job Listings
6. Search Jobs by Salary Range
7. Exit

## Adding a Job Listing
Enter job title: Software Developer
Enter company ID: 1
Enter salary: 70000
Enter job location: New York
Enter job description: Full stack developer position at TechCorp.
Job Listing Added Successfully!








