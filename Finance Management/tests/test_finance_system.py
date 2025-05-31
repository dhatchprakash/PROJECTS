import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import uuid
from entity.user import User
from entity.expense import Expense
from dao.finance_repository_impl import FinanceRepositoryImpl
from exception.user_not_found_exception import UserNotFoundException
from exception.expense_not_found_exception import ExpenseNotFoundException

class TestFinanceSystem(unittest.TestCase):
    def setUp(self):
        self.repo = FinanceRepositoryImpl()

    def generate_unique_email(self):
        return f"test_{uuid.uuid4().hex[:6]}@example.com"

    def test_create_user_success(self):
        email = self.generate_unique_email()
        user = User(username="testuser", password="testpass", email=email)
        result = self.repo.create_user(user)
        self.assertTrue(result)

    def test_create_expense_success(self):
        email = self.generate_unique_email()
        user = User(username="testuser2", password="testpass", email=email)
        self.repo.create_user(user)
        cursor = self.repo.connection.cursor()
        cursor.execute(f"SELECT user_id FROM Users WHERE email = '{email}'")
        user_id = cursor.fetchone()[0]
        expense = Expense(user_id=user_id, amount=100.0, category_id=1, date="2025-04-05", description="Test expense")
        result = self.repo.create_expense(expense)
        self.assertTrue(result)

    def test_get_all_expenses(self):
        # Create a new user with a unique email
        email = self.generate_unique_email()
        user = User(username="testuser3", password="testpass", email=email)
        self.repo.create_user(user)

        # Fetch the user_id after creating the user
        cursor = self.repo.connection.cursor()
        cursor.execute("SELECT user_id FROM Users WHERE email = ?", (email,))
        user_id = cursor.fetchone()[0]
        print(f"Created user with ID: {user_id}")  # Debugging line

        # Add an expense for the created user
        expense = Expense(user_id=user_id, amount=50.0, category_id=2, date="2025-04-05", description="Test expense")
        expense_result = self.repo.create_expense(expense)
        print(f"Expense created successfully: {expense_result}")  # Debugging line

        # Fetch the expenses for the user
        expenses = self.repo.get_all_expenses(user_id)
        print(f"Fetched expenses: {expenses}")  # Debugging line

    

    def test_user_not_found_exception(self):
        # Try creating an expense for a non-existent user (ID 9999)
        expense = Expense(user_id=9999, amount=100.0, category_id=1, date="2025-04-05", description="Test")
        with self.assertRaises(UserNotFoundException):
            self.repo.create_expense(expense)

    def test_expense_not_found_exception(self):
        # Try deleting an expense that doesn't exist (ID 9999)
        with self.assertRaises(ExpenseNotFoundException):
            self.repo.delete_expense(9999)

if __name__ == '__main__':
    unittest.main()
