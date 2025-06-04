class JobApplication:
    def __init__(self, job_listing_id, applicant_id, application_date, cover_letter, application_id=None):
        self.application_id = application_id
        self.job_listing_id = job_listing_id
        self.applicant_id = applicant_id
        self.application_date = application_date
        self.cover_letter = cover_letter

    def __str__(self):
        return f"ApplicationID: {self.application_id}, JobListingID: {self.job_listing_id}, ApplicantID: {self.applicant_id}, Date: {self.application_date}"
