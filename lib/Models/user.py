from orm import ORM

class User:
    orm = ORM('expenses.db')

    def __init__(self, username, email):
        self.username = username
        self.email = email

    @classmethod
    def create(cls, username, email):
        cls.orm.execute('INSERT INTO users (username, email) VALUES (?, ?)', (username, email))

    @classmethod
    def delete(cls, user_id):
        cls.orm.execute('DELETE FROM users WHERE id = ?', (user_id,))

    @classmethod
    def get_all(cls):
        return cls.orm.fetchall('SELECT * FROM users')

    @classmethod
    def find(cls, user_id):
        return cls.orm.fetchone('SELECT * FROM users WHERE id = ?', (user_id,))
