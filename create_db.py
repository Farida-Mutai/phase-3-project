import sqlite3

def create_database():
    
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()

    
    
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

    
    
    create_categories_table = """
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    )
    """

    
    
    create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    """

    
    
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

    
    
    cursor.execute(create_expenses_table)
    cursor.execute(create_categories_table)
    cursor.execute(create_users_table)
    cursor.execute(create_incomes_table)

    
    
    cursor.executemany(
        "INSERT OR IGNORE INTO categories (name) VALUES (?)", 
        [('Groceries',), ('Rent',), ('Utilities',), ('Entertainment',), ('Transportation',), ('Healthcare',)]
    )

    
    cursor.executemany(
        "INSERT OR IGNORE INTO users (username, email) VALUES (?, ?)", 
        [
            ('Ann', 'ann@gmail.com'), 
            ('Kennedy', 'kennedy@gmail.com'), 
            ('Rick', 'rick@gmail.com'),
            ('Farida', 'farida@gmail.com'),
            ('Eugine', 'eugine@gmail.com'),
            ('Frankline', 'frankline@gmail.com'),
            ('Joel', 'joel@gmail.com'),
            ('Alex', 'alex@gmail.com'),
            ('Quincy', 'quincy@gmail.com')
        ]
    )

    
    
    cursor.executemany(
        "INSERT INTO incomes (description, amount, user_id) VALUES (?, ?, ?)", 
        [
            ('Salary', 4000, 1), 
            ('Freelance Work', 2500, 2),
            ('Consulting', 1500, 3),
            ('Teaching', 3000, 4),
            ('Investment Return', 1000, 5),
            ('Business Profit', 3500, 6),
            ('Freelance Design', 2000, 7),
            ('Rental Income', 1800, 8),
            ('E-commerce Sales', 2200, 9)
        ]
    )

    
    cursor.executemany(
        "INSERT INTO expenses (description, amount, category_id) VALUES (?, ?, ?)", 
        [
            ('Grocery Shopping', 150, 1), 
            ('Rent Payment', 850, 2),
            ('Movie Night', 60, 4),
            ('Bus Fare', 25, 5),
            ('Doctor Appointment', 180, 6),
            ('Electricity Bill', 130, 3),
            ('Dinner at Restaurant', 90, 4),
            ('Gas for Car', 70, 5),
            ('Gym Membership', 50, 6),
            ('Water Bill', 40, 3)
        ]
    )

    
    conn.commit()
    conn.close()

    print("Database 'expenses.db' created successfully with seeded data.")

if __name__ == '__main__':
    create_database()
