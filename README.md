# PHASE-3-PROJECT

###EXPENSE TRACKER

An Expense Tracker application designed to help users manage their expenses and incomes efficiently. This application provides functionalities for adding, viewing, updating, and deleting expenses and categories. Users can also track their incomes associated with different activities.

####Features

User Management: Create and manage users with unique usernames and email addresses.
Expense Management: Add, update, delete, and view expenses categorized under different types.
Income Tracking: Add and view income records associated with users.
Category Management: Add, delete, and view categories for better expense organization.
SQLite Database: Utilizes SQLite for storing data in a lightweight and efficient manner.
CLI Interface: User-friendly command-line interface for easy navigation and data management.

-------Technologies Used---

Python 3.x
SQLite
Click (for CLI interface)
SQLAlchemy (for ORM functionality)

####CLI Commands

Add Expense: Prompts for expense details (description, amount, category).
View Expenses: Displays a list of all expenses.
Update Expense: Modify an existing expense using its ID.
Delete Expense: Remove an expense using its ID.
Add Category: Add a new category for expenses.
View Categories: List all categories.
Delete Category: Remove a category using its ID.
Exit: Quit the application.

_____Database Schema____
Tables

1:Users

id: Integer, primary key
username: Text, unique
email: Text, unique

2:Categories

id: Integer, primary key
name: Text, unique

3:Expenses

id: Integer, primary key
description: Text
amount: Real
category_id: Integer, foreign key referencing categories(id)
created_at: Timestamp

4;Incomes

id: Integer, primary key
description: Text
amount: Real
user_id: Integer, foreign key referencing users(id)
created_at: Timestamp

###Sample Data
Upon creating the database, sample data will be seeded into the tables. This includes:

Categories: Groceries, Rent, Utilities, Entertainment, Transportation, Healthcare.
Users: Ann, Kennedy, Rick, Farida, Eugine, Frankline, Joel, Alex, Quincy, with corresponding email addresses.

##Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please feel free to submit a pull request my github repository is https://github.com/Farida-Mutai/phase-3-project.
Reach me on my email address farida.mutai@student.moringaschool.com

License
This project is licensed under the Apache 2.0.
