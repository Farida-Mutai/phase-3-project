from sqlalchemy.orm import Session
from helper import create_user, create_expense, create_income, create_payment

def seed_data(db: Session):
    # Create Users
    user1 = create_user(db, name="John Doe", email="john@example.com")
    user2 = create_user(db, name="Jane Doe", email="jane@example.com")

    # Create Payments
    create_payment(db, method="Credit Card", user_id=user1.id)
    create_payment(db, method="PayPal", user_id=user2.id)

    # Create Incomes
    create_income(db, source="Job", amount=5000, user_id=user1.id)
    create_income(db, source="Freelance", amount=1500, user_id=user2.id)

    # Create Expenses
    create_expense(db, description="Rent", amount=1200, user_id=user1.id)
    create_expense(db, description="Groceries", amount=300, user_id=user2.id)
