import sqlite3

def create_database():
    
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()

    # Create expenses table
    create_expenses_table = """
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        amount REAL NOT NULL,
        category_id INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )
    """

    # Create categories table
    create_categories_table = """
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    )
    """

    # Create users table
    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    """

    # Create incomes table
    create_incomes_table = """
    CREATE TABLE IF NOT EXISTS incomes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        amount REAL NOT NULL,
        user_id INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """

    # Execute table creation queries
    cursor.execute(create_expenses_table)
    cursor.execute(create_categories_table)
    cursor.execute(create_users_table)
    cursor.execute(create_incomes_table)

    # Insert seed data for categories
    cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES ('Groceries'), ('Rent'), ('Utilities')")

    # Insert seed data for users
    cursor.execute("INSERT OR IGNORE INTO users (username, email) VALUES ('John Doe', 'john@example.com'), ('Jane Smith', 'jane@example.com')")

    # Insert seed data for incomes
    cursor.execute("INSERT INTO incomes (description, amount, user_id) VALUES ('Salary', 3000, 1), ('Freelance Work', 1500, 2)")

    # Insert seed data for expenses
    cursor.execute("INSERT INTO expenses (description, amount, category_id) VALUES ('Grocery Shopping', 100, 1), ('Rent Payment', 800, 2)")

    # Commit and close connection
    conn.commit()
    conn.close()

    print("Database 'expenses.db' created successfully with seeded data.")

if __name__ == '__main__':
    create_database()
