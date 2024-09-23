from orm import ORM

class Income:
    orm = ORM('expenses.db')

    def __init__(self, description, amount, user_id):
        self.description = description
        self.amount = amount
        self.user_id = user_id
    
    @classmethod
    def create(cls, description, amount, user_id):
        cls.orm.execute('INSERT INTO incomes (description, amount, user_id) VALUES (?, ?, ?)', (description, amount, user_id))

    @classmethod
    def delete(cls, income_id):
        cls.orm.execute('DELETE FROM incomes WHERE id = ?', (income_id,))

    @classmethod
    def get_all(cls):
        return cls.orm.fetchall('SELECT * FROM incomes')

    @classmethod
    def find(cls, income_id):
        return cls.orm.fetchone('SELECT * FROM incomes WHERE id = ?', (income_id,))
