from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    
    expenses = relationship('Expense', back_populates='user')
    payments = relationship('Payment', back_populates='user')
    incomes = relationship('Income', back_populates='user')

class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    method = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship('User', back_populates='payments')

class Income(Base):
    __tablename__ = 'incomes'

    id = Column(Integer, primary_key=True)
    source = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship('User', back_populates='incomes')

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='expenses')
