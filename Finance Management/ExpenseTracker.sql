
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'ExpenseTracker')
BEGIN
    CREATE DATABASE ExpenseTracker;
END;


USE ExpenseTracker;

-- Create Users table
CREATE TABLE Users (
    user_id INT PRIMARY KEY IDENTITY(1,1),
    username NVARCHAR(50) NOT NULL,
    password NVARCHAR(255) NOT NULL,
    email NVARCHAR(100) NOT NULL UNIQUE
);

-- Create ExpenseCategories table
CREATE TABLE ExpenseCategories (
    category_id INT PRIMARY KEY IDENTITY(1,1),
    category_name NVARCHAR(50) NOT NULL UNIQUE
);

-- Create Expenses table with foreign key constraints
CREATE TABLE Expenses (
    expense_id INT PRIMARY KEY IDENTITY(1,1),
    user_id INT NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    category_id INT NOT NULL,
    date DATE NOT NULL,
    description NVARCHAR(MAX),
    CONSTRAINT FK_Expenses_Users FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    CONSTRAINT FK_Expenses_Categories FOREIGN KEY (category_id) REFERENCES ExpenseCategories(category_id) ON DELETE NO ACTION
);

-- Insert default categories
INSERT INTO ExpenseCategories (category_name) VALUES 
('Food'), 
('Transportation'), 
('Utilities');




SELECT * FROM users WHERE email = 'abc@mail';



SELECT * FROM users;

SELECT * FROM Expenses;

SELECT * FROM ExpenseCategories;


SELECT username
FROM Users
WHERE user_id IN (
    SELECT user_id
    FROM Expenses
    GROUP BY user_id
    HAVING SUM(amount) > 100
);


SELECT u.username, SUM(e.amount) AS total_food_expenses
FROM Expenses e
JOIN Users u ON e.user_id = u.user_id
WHERE e.category_id = (SELECT category_id FROM ExpenseCategories WHERE category_name = 'Food')
GROUP BY u.username;



select host_name() as Server_Hostname;
select db_name() as Current_Database;

