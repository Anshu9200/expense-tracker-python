from expense import add_expense, view_expenses

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        print("Thank you for using Expense Tracker!")
        break
    else:
        print("Invalid choice! Please try again.")
