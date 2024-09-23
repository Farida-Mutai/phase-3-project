import sqlite3

class ORM:
    def __init__(self, db_name= 'expenses.db'):
        self.db_name = db_name

    def execute(self, query, params=None):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params or ())
            conn.commit()

    def fetchall(self, query, params=None):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params or ())
            return cursor.fetchall()

    def fetchone(self, query, params=None):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params or ())
            return cursor.fetchone()