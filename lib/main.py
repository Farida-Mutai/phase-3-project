from Models.expense import Expense
from Models.category import Category
from Models.user import User
from Models.income import Income
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    clear_screen()
    print("Expense Tracker CLI")
    print("===================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Add Category")
    print("6. View Categories")
    print("7. Delete Category")
    print("8. Add User")
    print("9. View Users")
    print("10. Delete User")
    print("11. Add Income")
    print("12. View Incomes")
    print("13. Delete Income")
    print("14. Exit")

    choice = input("Enter your choice: ")
    return choice




def add_expense():
    description = input("Enter the expense description: ")
    amount = input("Enter the amount: ")
    category_id = input("Enter the category ID: ")
    try:
        Expense.create(description, float(amount), int(category_id))
        print("Expense added successfully.")
    except Exception as e:
        print(f"Error adding expense: {e}")

def view_expenses():
    try:
        expenses = Expense.get_all()
        if expenses:
            for exp in expenses:
                print(f"ID: {exp[0]}, Description: {exp[1]}, Amount: {exp[2]}, Category ID: {exp[3]}")
        else:
            print("No expenses found.")
    except Exception as e:
        print(f"Error fetching expenses: {e}")

def update_expense():
    expense_id = input("Enter the expense ID to update: ")
    description = input("Enter the new description: ")
    amount = input("Enter the new amount: ")
    category_id = input("Enter the new category ID: ")
    try:
        Expense.update(int(expense_id), description, float(amount), int(category_id))
        print("Expense updated successfully.")
    except Exception as e:
        print(f"Error updating expense: {e}")

def delete_expense():
    expense_id = input("Enter the expense ID to delete: ")
    try:
        Expense.delete(int(expense_id))
        print("Expense deleted successfully.")
    except Exception as e:
        print(f"Error deleting expense: {e}")




def add_category():
    name = input("Enter the category name: ")
    try:
        Category.create(name)
        print("Category added successfully.")
    except Exception as e:
        print(f"Error adding category: {e}")

def view_categories():
    try:
        categories = Category.get_all()
        if categories:
            for cat in categories:
                print(f"ID: {cat[0]}, Name: {cat[1]}")
        else:
            print("No categories found.")
    except Exception as e:
        print(f"Error fetching categories: {e}")

def delete_category():
    category_id = input("Enter the category ID to delete: ")
    try:
        Category.delete(int(category_id))
        print("Category deleted successfully.")
    except Exception as e:
        print(f"Error deleting category: {e}")

# ---- USER FUNCTIONS ----

def add_user():
    username = input("Enter the username: ")
    email = input("Enter the email: ")
    try:
        User.create(username, email)
        print("User added successfully.")
    except Exception as e:
        print(f"Error adding user: {e}")

def view_users():
    try:
        users = User.get_all()
        if users:
            for user in users:
                print(f"ID: {user[0]}, Username: {user[1]}, Email: {user[2]}")
        else:
            print("No users found.")
    except Exception as e:
        print(f"Error fetching users: {e}")

def delete_user():
    user_id = input("Enter the user ID to delete: ")
    try:
        User.delete(int(user_id))
        print("User deleted successfully.")
    except Exception as e:
        print(f"Error deleting user: {e}")




def add_income():
    description = input("Enter the income description: ")
    amount = input("Enter the amount: ")
    user_id = input("Enter the user ID: ")
    try:
        Income.create(description, float(amount), int(user_id))
        print("Income added successfully.")
    except Exception as e:
        print(f"Error adding income: {e}")

def view_incomes():
    try:
        incomes = Income.get_all()
        if incomes:
            for income in incomes:
                print(f"ID: {income[0]}, Description: {income[1]}, Amount: {income[2]}, User ID: {income[3]}")
        else:
            print("No incomes found.")
    except Exception as e:
        print(f"Error fetching incomes: {e}")

def delete_income():
    income_id = input("Enter the income ID to delete: ")
    try:
        Income.delete(int(income_id))
        print("Income deleted successfully.")
    except Exception as e:
        print(f"Error deleting income: {e}")




def main():
    while True:
        choice = main_menu()
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            update_expense()
        elif choice == '4':
            delete_expense()
        elif choice == '5':
            add_category()
        elif choice == '6':
            view_categories()
        elif choice == '7':
            delete_category()
        elif choice == '8':
            add_user()
        elif choice == '9':
            view_users()
        elif choice == '10':
            delete_user()
        elif choice == '11':
            add_income()
        elif choice == '12':
            view_incomes()
        elif choice == '13':
            delete_income()
        elif choice == '14':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice, please try again.")
        input("Press Enter to continue...")


if __name__ == '__main__':
    main()
