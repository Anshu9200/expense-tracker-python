from expense import (
    initialize_file,
    add_expense,
    view_expenses,
    search_expense,
    total_expense
)


def main():

    initialize_file()

    while True:

        print("\n========== Expense Tracker ==========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. View Total Expense")
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
