from sqlalchemy.orm import Session
from main import User, Payment, Income, Expense

def create_user(db: Session, name: str, email: str) -> User:
    new_user = User(name=name, email=email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user_id: int, name: str = None, email: str = None) -> User:
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        if name:
            user.name = name
        if email:
            user.email = email
        db.commit()
        db.refresh(user)
    return user

def delete_user(db: Session, user_id: int) -> User:
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user

def create_expense(db: Session, description: str, amount: int, user_id: int) -> Expense:
    new_expense = Expense(description=description, amount=amount, user_id=user_id)
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense

def create_income(db: Session, source: str, amount: int, user_id: int) -> Income:
    new_income = Income(source=source, amount=amount, user_id=user_id)
    db.add(new_income)
    db.commit()
    db.refresh(new_income)
    return new_income

def create_payment(db: Session, method: str, user_id: int) -> Payment:
    new_payment = Payment(method=method, user_id=user_id)
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment
