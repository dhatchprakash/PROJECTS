class Applicant:
    def __init__(self, first_name, last_name, email, phone, resume, applicant_id=None):
        self.applicant_id = applicant_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.resume = resume


    def __str__(self):
        return f"ApplicantID: {self.applicant_id}, Name: {self.first_name} {self.last_name}, Email: {self.email}"
