from orm import ORM

class Category:
    orm = ORM('expenses.db')

    def __init__(self, name):
        self.name = name

    @classmethod
    def create(cls, name):
        cls.orm.execute('INSERT INTO categories (name) VALUES (?)', (name,))

    @classmethod
    def delete(cls, category_id):
        cls.orm.execute('DELETE FROM categories WHERE id = ?', (category_id,))

    @classmethod
    def get_all(cls):
        return cls.orm.fetchall('SELECT * FROM categories')

    @classmethod
    def find(cls, category_id):
        return cls.orm.fetchone('SELECT * FROM categories WHERE id = ?', (category_id,))
