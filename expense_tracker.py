def add_expense():
    expense = {}
    while True:
        try:
            amount = float(input("Enter the amount spent: "))
            category = input("Enter the category: ")
            description = input("Enter a brief description: ")
            expense = {"amount": amount, "category": category, "description": description}
            break
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
    return expense
def categorize_expenses(expenses):
    categories = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount
    return categories
def analyze_expenses(expenses):
    total_amount = sum([expense["amount"] for expense in expenses])
    average_amount = total_amount / len(expenses)
    categories = categorize_expenses(expenses)
    print("Total amount spent: ", total_amount)
    print("Average amount spent per day: ", average_amount)
    for category, amount in categories.items():
        print(f"Amount spent in {category}: ", amount)
expenses = []
def main():
    while True:
        print("\n1. Add an expense")
        print("2. Analyze expenses")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            expense = add_expense()
            expenses.append(expense)
        elif choice == "2":
            analyze_expenses(expenses)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter a valid choice.")
if __name__ == "__main__":
    main()