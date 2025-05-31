import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pyodbc
from dao.ifinance_repository import IFinanceRepository
from entity.user import User
from entity.expense import Expense
from util.db_conn_util import DBConnUtil
from exception.user_not_found_exception import UserNotFoundException
from exception.expense_not_found_exception import ExpenseNotFoundException

class FinanceRepositoryImpl(IFinanceRepository):
    def __init__(self):
        self.connection = DBConnUtil.get_connection()

    def create_user(self, user: User) -> bool:
        cursor = self.connection.cursor()
        try:
            # Insert user without specifying user_id (auto-generated)
            cursor.execute(
                "INSERT INTO Users (username, password, email) VALUES (?, ?, ?)",
                (user.username, user.password, user.email)
            )
            self.connection.commit()
            print(f"User {user.username} created successfully.")
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False
        finally:
            cursor.close()

    def create_expense(self, expense: Expense) -> bool:
        cursor = self.connection.cursor()
        try:
            # Check if the user exists before creating expense
            cursor.execute("SELECT user_id FROM Users WHERE user_id = ?", (expense.user_id,))
            if not cursor.fetchone():
                raise UserNotFoundException(f"User with ID {expense.user_id} not found")
            
            cursor.execute(
                "INSERT INTO Expenses (user_id, amount, category_id, date, description) VALUES (?, ?, ?, ?, ?)",
                (expense.user_id, expense.amount, expense.category_id, expense.date, expense.description)
            )
            self.connection.commit()
            print(f"Expense created successfully for user {expense.user_id}.")
            return True
        except UserNotFoundException as e:
            print(f"Error creating expense: {e}")
            raise
        except Exception as e:
            print(f"Error creating expense: {e}")
            return False
        finally:
            cursor.close()

    def delete_user(self, user_id: int) -> bool:
        cursor = self.connection.cursor()
        try:
            # Verify the user exists before deletion
            cursor.execute("SELECT user_id FROM Users WHERE user_id = ?", (user_id,))
            if not cursor.fetchone():
                raise UserNotFoundException(f"User with ID {user_id} not found")
            
            cursor.execute("DELETE FROM Expenses WHERE user_id = ?", (user_id,))
            cursor.execute("DELETE FROM Users WHERE user_id = ?", (user_id,))
            self.connection.commit()
            print(f"User {user_id} and associated expenses deleted successfully.")
            return True
        except UserNotFoundException as e:
            print(f"Error deleting user: {e}")
            raise
        except Exception as e:
            print(f"Error deleting user: {e}")
            return False
        finally:
            cursor.close()

    def delete_expense(self, expense_id: int) -> bool:
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT expense_id FROM Expenses WHERE expense_id = ?", (expense_id,))
            if not cursor.fetchone():
                raise ExpenseNotFoundException(f"Expense with ID {expense_id} not found")
            
            cursor.execute("DELETE FROM Expenses WHERE expense_id = ?", (expense_id,))
            self.connection.commit()
            print(f"Expense {expense_id} deleted successfully.")
            return True
        except ExpenseNotFoundException as e:
            print(f"Error deleting expense: {e}")
            raise
        except Exception as e:
            print(f"Error deleting expense: {e}")
            return False
        finally:
            cursor.close()

    def get_all_expenses(self, user_id: int) -> list:
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT user_id FROM Users WHERE user_id = ?", (user_id,))
            if not cursor.fetchone():
                raise UserNotFoundException(f"User with ID {user_id} not found")
            
            query = """
            SELECT e.expense_id, u.username, ec.category_name, e.amount, e.date, e.description
            FROM Expenses e
            JOIN Users u ON e.user_id = u.user_id
            JOIN ExpenseCategories ec ON e.category_id = ec.category_id
            WHERE e.user_id = ?
            AND e.amount > (
                SELECT AVG(amount)
                FROM Expenses
                WHERE user_id = ?
            )
            ORDER BY e.date DESC
            """

            cursor.execute(query, (user_id, user_id))
            rows = cursor.fetchall()

            expenses = []
            for row in rows:
                expense_data = {
                    'expense_id': row[0],
                    'username': row[1],
                    'category_name': row[2],
                    'amount': row[3],
                    'date': str(row[4]),
                    'description': row[5]
                }
                expenses.append(expense_data)

            return expenses

        except UserNotFoundException as e:
            print(f"Error fetching expenses for user {user_id}: {e}")
            raise
        except Exception as e:
            print(f"Unexpected error while fetching expenses: {e}")
            return []
        finally:
            cursor.close()

    def update_expense(self, user_id: int, expense: Expense) -> bool:
        cursor = self.connection.cursor()
        try:
            # Verify the user exists
            cursor.execute("SELECT user_id FROM Users WHERE user_id = ?", (user_id,))
            if not cursor.fetchone():
                raise UserNotFoundException(f"User with ID {user_id} not found")
            
            # Verify the expense exists
            cursor.execute("SELECT expense_id FROM Expenses WHERE expense_id = ?", (expense.expense_id,))
            if not cursor.fetchone():
                raise ExpenseNotFoundException(f"Expense with ID {expense.expense_id} not found")
            
            cursor.execute(
                "UPDATE Expenses SET amount = ?, category_id = ?, date = ?, description = ? WHERE expense_id = ? AND user_id = ?",
                (expense.amount, expense.category_id, expense.date, expense.description, expense.expense_id, user_id)
            )
            self.connection.commit()
            print(f"Expense {expense.expense_id} updated successfully.")
            return True
        except (UserNotFoundException, ExpenseNotFoundException) as e:
            print(f"Error updating expense: {e}")
            raise
        except Exception as e:
            print(f"Error updating expense: {e}")
            return False
        finally:
            cursor.close()

# Optional test
if __name__ == "__main__":
    print("FinanceRepositoryImpl loaded successfully!")

    repo = FinanceRepositoryImpl()
    
    # Create user without specifying user_id
    test_user = User(username="testuser", password="test123", email="test@example.com")
    
    success = repo.create_user(test_user)

    if success:
        print("User created successfully!")
    else:
        print("Failed to create user.")
