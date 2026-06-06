import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"


def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense():
    expenses = load_expenses()

    title = input("Enter Expense Title: ")
    category = input("Enter Category: ")

    try:
        amount = float(input("Enter Amount: "))
    except ValueError:
        print("Invalid Amount!")
        return

    expense = {
        "title": title,
        "category": category,
        "amount": amount,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense Added Successfully!")


def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    print("\n===== ALL EXPENSES =====")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['title']} | "
            f"{expense['category']} | "
            f"PKR {expense['amount']} | "
            f"{expense['date']}"
        )


def delete_expense():
    expenses = load_expenses()

    if not expenses:
        print("No expenses available.")
        return

    view_expenses()

    try:
        index = int(input("\nEnter Expense Number to Delete: ")) - 1

        if 0 <= index < len(expenses):
            removed = expenses.pop(index)
            save_expenses(expenses)

            print(f"{removed['title']} deleted successfully!")
        else:
            print("Invalid Number.")

    except ValueError:
        print("Invalid Input.")


def search_expense():
    expenses = load_expenses()

    keyword = input("Enter Expense Title: ").lower()

    found = False

    for expense in expenses:
        if keyword in expense["title"].lower():
            print(
                f"{expense['title']} | "
                f"{expense['category']} | "
                f"PKR {expense['amount']}"
            )
            found = True

    if not found:
        print("No matching expense found.")


def show_summary():
    expenses = load_expenses()

    total_amount = sum(expense["amount"] for expense in expenses)

    print("\n===== SUMMARY =====")
    print(f"Total Expenses: {len(expenses)}")
    print(f"Total Amount: PKR {total_amount:.2f}")

    categories = {}

    for expense in expenses:
        category = expense["category"]
        categories[category] = categories.get(category, 0) + expense["amount"]

    print("\nCategory Wise Spending:")

    for category, amount in categories.items():
        print(f"{category}: PKR {amount:.2f}")


def main():
    while True:

        print("\n===== EXPENSE TRACKER =====\n")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Search Expense")
        print("5. Show Summary")
        print("6. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            delete_expense()

        elif choice == "4":
            search_expense()

        elif choice == "5":
            show_summary()

        elif choice == "6":
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()