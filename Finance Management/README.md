# 💰 Finance Management System

The Finance Management System is a comprehensive Python application for managing personal finances. It allows users to register, track expenses, categorize spending, and generate reports, with a live connection to MS SQL Server for data persistence.

---

## 📂 Project Structure

📂 FinanceManagementSystem/
├── 📁 entity/
│   ├── __init__.py
│   ├── user.py
│   ├── expense.py
│   └── expense_category.py
├── 📁 dao/
│   ├── __init__.py
│   ├── ifinance_repository.py
│   └── finance_repository_impl.py
├── 📁 exception/
│   ├── __init__.py
│   ├── user_not_found_exception.py
│   └── expense_not_found_exception.py
├── 📁 util/
│   ├── __init__.py
│   ├── db_property_util.py
│   ├── db_conn_util.py
│   ├── test_connection.py
│   └── database.properties
├── 📁 main/
│   ├── __init__.py
│   └── finance_app.py
├── 📁 tests/
│   ├── __init__.py
│   └── test_finance_system.py
├── ExpenseTracker.sql
├── README.md
└── test.py







## ✅ Key Functionalities

- User Authentication: Secure registration and login for users.
- Expense Management: Add, view, update, and delete expenses.
- Expense Categorization: Assign expenses to categories (e.g., Food, Transportation, Utilities).
- Reports Generation: View all expenses for a user with details.
- Database Connectivity: Real-time interaction with MS SQL Server for persistent storage.
- Exception Handling: Custom exceptions for invalid user or expense operations.
- Unit Testing: Tests for user creation, expense management, and error scenarios.

---

## 🛠 Technologies Used

- Python 3.x
- SQL Server (MS SQL)
- pyodbc (ODBC connector)
- unittest (for testing)

---

## 🚀 How to Run

1. Clone the project
   ```bash
   git clone <your-repo-link>
   cd FinanceManagementSystem
   ```

2. Set up SQL Server
   - Ensure MS SQL Server is running.
   - Create the `ExpenseTracker` database and required tables (Users, ExpenseCategories, Expenses).

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app
   ```bash
   python main/finance_app.py
   ```

   > Make sure your SQL Server is running and the tables are created.

---

## 🧪 Run Unit Tests

```bash
python tests/test_finance_system.py
```

---

## 🧾 SQL Server Tables Required

- Users: Stores user information (user_id, username, password, email).
- ExpenseCategories: Stores expense categories (category_id, category_name).
- Expenses: Stores expense details (expense_id, user_id, amount, category_id, date, description).

---

## 👨‍💻 Author

Created as part of Hexavarsity - Finance Management System Case Study 
Built by: Dhatchitha Prakash
Mentored by: Hexaware Technologies

---

## 📩 Notes

- Ensure the SQL Server ODBC Driver is installed (ODBC Driver 17 for SQL Server).
- Modify `database.properties` if you change your server or database name.
- Uses Windows Authentication for SQL Server; update `util/db_conn_util.py` for other authentication methods.
- Run the application from the `FinanceManagementSystem` directory.

---

Happy budgeting! 💸