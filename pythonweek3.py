class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

    def view_expenses(self):
        total = 0
        print("Expense Tracker:")
        print("----------------")
        for category, amount in self.expenses.items():
            print(f"{category}: ${amount}")
            total += amount
        print("----------------")
        print(f"Total expenses: ${total}")


def main():
    tracker = ExpenseTracker()
    while True:
        print("\n1. Add an expense")
        print("2. View expenses")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            category = input("Enter the category of expense: ")
            amount = float(input("Enter the amount: "))
            tracker.add_expense(category, amount)
            print("Expense added successfully!")
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
