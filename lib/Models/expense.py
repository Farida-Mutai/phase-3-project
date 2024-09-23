from orm import ORM

class Expense:
    orm = ORM('expenses.db')

    def __init__(self, description, amount, category_id):
        self.description = description
        self.amount = amount
        self.category_id = category_id
    
    @classmethod
    def create(cls, description, amount, category_id):
        cls.orm.execute('INSERT INTO expenses (description, amount, category_id) VALUES (?, ?, ?)', (description, amount, category_id))

    @classmethod
    def delete(cls, expense_id):
        cls.orm.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))

    @classmethod
    def get_all(cls):
        return cls.orm.fetchall('SELECT * FROM expenses')

    @classmethod
    def find(cls, expense_id):
        return cls.orm.fetchone('SELECT * FROM expenses WHERE id = ?', (expense_id,))