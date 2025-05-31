import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from entity.user import User
from entity.expense import Expense
from dao.finance_repository_impl import FinanceRepositoryImpl
from exception.user_not_found_exception import UserNotFoundException
from exception.expense_not_found_exception import ExpenseNotFoundException
from util.db_conn_util import DBConnUtil

class FinanceApp:
    def __init__(self):
        self.repo = FinanceRepositoryImpl()

    def display_menu(self):
        print("\n=== Finance Management System ===")
        print("1. Add User")
        print("2. Add Expense")
        print("3. Delete User")
        print("4. Delete Expense")
        print("5. Update Expense")
        print("6. View All Expenses by User")
        print("7. View All Users")
        print("8. Exit")

    def show_all_users(self):
        print("\nList of Registered Users:")
        try:
            cursor = DBConnUtil.get_connection().cursor()
            cursor.execute("SELECT user_id, username, email FROM Users")
            rows = cursor.fetchall()
            if not rows:
                print("No users found.")
            else:
                for row in rows:
                    print(f"User ID: {row[0]}, Username: {row[1]}, Email: {row[2]}")
            cursor.close()
        except Exception as e:
            print(f"Error fetching users: {e}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            try:
                if choice == '1':
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                    email = input("Enter email: ")
                    user = User(username=username, password=password, email=email)
                    if self.repo.create_user(user):
                        print("User added successfully.")
                        cursor = DBConnUtil.get_connection().cursor()
                        cursor.execute("SELECT TOP 1 user_id FROM Users ORDER BY user_id DESC")
                        user_id = cursor.fetchone()[0]
                        print(f"Your new User ID is: {user_id}")
                        cursor.close()
                    else:
                        print("Failed to add user.")

                elif choice == '2':
                    user_id = int(input("Enter user ID: "))
                    amount = float(input("Enter amount: "))
                    category_id = int(input("Enter category ID (1=Food, 2=Transportation, 3=Utilities): "))
                    if category_id not in [1, 2, 3]:
                        print("Invalid category ID! Please choose from (1=Food, 2=Transportation, 3=Utilities).")
                        continue
                    date = input("Enter date (YYYY-MM-DD): ")
                    description = input("Enter description: ")
                    expense = Expense(user_id=user_id, amount=amount, category_id=category_id, date=date, description=description)
                    if self.repo.create_expense(expense):
                        print("Expense added successfully.")
                    else:
                        print("Failed to add expense.")

                elif choice == '3':
                    user_id = int(input("Enter user ID to delete: "))
                    if self.repo.delete_user(user_id):
                        print("User deleted successfully.")
                    else:
                        print("Failed to delete user.")

                elif choice == '4':
                    expense_id = int(input("Enter expense ID to delete: "))
                    if self.repo.delete_expense(expense_id):
                        print("Expense deleted successfully.")
                    else:
                        print("Failed to delete expense.")

                elif choice == '5':
                    user_id = int(input("Enter user ID: "))
                    expense_id = int(input("Enter expense ID to update: "))
                    amount = float(input("Enter new amount: "))
                    category_id = int(input("Enter new category ID: "))
                    if category_id not in [1, 2, 3]:
                        print("Invalid category ID! Please choose from (1=Food, 2=Transportation, 3=Utilities).")
                        continue
                    date = input("Enter new date (YYYY-MM-DD): ")
                    description = input("Enter new description: ")
                    expense = Expense(expense_id=expense_id, user_id=user_id, amount=amount, category_id=category_id, date=date, description=description)
                    if self.repo.update_expense(user_id, expense):
                        print("Expense updated successfully.")
                    else:
                        print("Failed to update expense.")

                elif choice == '6':
                    user_id = int(input("Enter user ID to view expenses: "))
                    expenses = self.repo.get_all_expenses(user_id)
                    if expenses:
                        print("\nExpenses:")
                        for exp in expenses:
                            print(f"ID: {exp['expense_id']}, Amount: {exp['amount']}, Category: {exp['category_name']}, Date: {exp['date']}, Description: {exp['description']}")
                    else:
                        print("No expenses found.")

                elif choice == '7':
                    self.show_all_users()

                elif choice == '8':
                    print("Exiting...")
                    break

                else:
                    print("Invalid choice! Please try again.")

            except UserNotFoundException as e:
                print(f"Error: {e}")
            except ExpenseNotFoundException as e:
                print(f"Error: {e}")
            except ValueError:
                print("Invalid input! Please enter correct data types.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    app = FinanceApp()
    app.run()
