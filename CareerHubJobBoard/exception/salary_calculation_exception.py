# salary_calculation_exception.py
class SalaryCalculationException(Exception):
    def __init__(self, message="Salary cannot be negative or invalid."):
        self.message = message
        super().__init__(self.message)
