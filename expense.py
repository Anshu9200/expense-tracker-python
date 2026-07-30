import csv
import os

FILE_NAME = "expenses.csv"


# Create CSV file with header if it does not exist
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount"])


# Add Expense
def add_expense():
    date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")

    while True:
        try:
            amount = float(input("Enter Amount: "))
            break
        except ValueError:
            print("Invalid amount! Enter numbers only.")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("\nExpense added successfully!")


# View All Expenses
def view_expenses():
    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)

            next(reader, None)  # Skip header

            records = list(reader)

            if not records:
                print("\nNo expense records found.")
                return

            print("\n========== Expense Records ==========")
            print(f"{'Date':<15}{'Category':<20}{'Amount':>10}")
            print("-" * 45)

            for row in records:
                print(f"{row[0]:<15}{row[1]:<20}{row[2]:>10}")

            print("-" * 45)

    except FileNotFoundError:
        print("\nNo expense records found.")


# Search Expense by Category
def search_expense():
    category = input("Enter category to search: ").lower()

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)

            next(reader, None)

            found = False

            print("\n========== Search Results ==========")
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


# Calculate Total Expense
def total_expense():
    total = 0

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file)

            next(reader, None)

            for row in reader:
                total += float(row[2])

            print(f"\nTotal Expense: {total:.2f}")

    except FileNotFoundError:
        print("No expense records found.")
