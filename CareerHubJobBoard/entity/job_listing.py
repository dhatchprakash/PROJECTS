class JobListing:
    def __init__(self, job_title, job_description, job_location, salary, job_type, company_id, posted_date, job_listing_id=None, company_name=None, company_location=None):
        self.job_listing_id = job_listing_id 
        self.job_title = job_title
        self.job_description = job_description
        self.job_location = job_location
        self.salary = salary
        self.job_type = job_type
        self.company_id = company_id
        self.posted_date = posted_date
        self.company_name = company_name
        self.company_location = company_location

    def __repr__(self):
        return f"<JobListing(JobTitle={self.job_title}, CompanyName={self.company_name}, Salary={self.salary})>"
