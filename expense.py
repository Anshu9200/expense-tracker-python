import csv
import os

FILE_NAME = "expenses.csv"


# Create CSV file with header if it doesn't exist
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount"])


# Add a new expense
def add_expense():
    date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")

    while True:
        try:
            amount = float(input("Enter Amount: "))
            break
        except ValueError:
            print("Invalid amount! Please enter a numeric value.")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("\nExpense added successfully!\n")


# Display all expenses
def view_expenses():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)

            # Skip header
            next(reader, None)

            rows = list(reader)

            if not rows:
                print("\nNo expense records found.\n")
                return

            print("\n========== Expense Records ==========")
            print(f"{'Date':<15}{'Category':<20}{'Amount':>10}")
            print("-" * 45)

            for row in rows:
                print(f"{row[0]:<15}{row[1]:<20}{row[2]:>10}")

            print("-" * 45)

    except FileNotFoundError:
        print("\nNo expense records found.\n")


# Search expenses by category
def search_expense():
    category = input("Enter Category to search: ").strip().lower()

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)

            next(reader, None)

            found = False

            print("\nMatching Expenses")
            print(f"{'Date':<15}{'Category':<20}{'Amount':>10}")
            print("-" * 45)

            for row in reader:
                if row[1].lower() == category:
                    print(f"{row[0]:<15}{row[1]:<20}{row[2]:>10}")
                    found = True

            if not found:
                print("No matching expenses found.")

    except FileNotFoundError:
        print("No expense records found.")


# Calculate total expenses
def total_expense():
    total = 0

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)

            next(reader, None)

            for row in reader:
                total += float(row[2])

        print(f"\nTotal Expenses = {total:.2f}\n")

    except FileNotFoundError:
        print("No expense records found.")


# Main Menu
def main():
    initialize_file()

    while True:
        print("\n========== Expense Tracker ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search by Category")
        print("4. View Total Expenses")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_expense()

        elif choice == "4":
            total_expense()

        elif choice == "5":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
