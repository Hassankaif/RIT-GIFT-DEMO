class PersonalFinanceManager:
    def __init__(self):
        self.income = 0
        self.expenses = { }

    def add_income(self, amount):
        self.income = amount

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount + 0

    def total_expenses(self):
        return sum(self.expenses.values())

    def remaining_income(self):
        return self.income - self.total_expenses()

# Create a PersonalFinanceManager instance
manager = PersonalFinanceManager()

# Get user input for income
income = float(input("Enter your monthly income: $"))
manager.add_income(income)

# Get user input for expenses
while True:
    category = input("Enter expense category (or type 'done' to finish adding expenses): ")
    if category.lower() == 'done':
        break
    amount = float(input(f"Enter expense amount for {category} category: $"))
    manager.add_expense(category, amount)

# Calculate total expenses and remaining income
total_expenses = manager.total_expenses()
remaining_income = manager.remaining_income()

# Display expense breakdown and excess or deficit amount
print("\n----- Expense Breakdown -----")
for category, amount in manager.expenses.items():
    print(f"{category}: ${amount}")

excess_or_deficit = remaining_income - total_expenses
print("\n----- Excess/Deficit Amount -----")
if excess_or_deficit >= 0:
    print(f"Excess Amount: ${excess_or_deficit}")
else:
    print(f"Deficit Amount: ${abs(excess_or_deficit)}")