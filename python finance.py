 
from datetime import datetime
 
# Initialize empty dictionaries to store income and expense transactions with dates
income_transactions = {}
expense_transactions = {}
 
# Function to add income entry with date
def add_income(amount, description, category, date):
    income_transactions[date] = {"amount": amount, "description": description, "category": category}
    print(f"Income of ${amount} added on {date}: {description} in category: {category}")
 
# Function to add expense entry with date
def add_expense(amount, description, category, date):
    expense_transactions[date] = {"amount": amount, "description": description, "category": category}
    print(f"Expense of ${amount} added on {date}: {description} in category: {category}")
 
# Function to generate a detailed report with expense breakdown by category
def generate_report():
    total_income = sum(transaction["amount"] for transaction in income_transactions.values())
    total_expense = sum(transaction["amount"] for transaction in expense_transactions.values())
    
    print("----- Advanced Finance Report -----")
    print(f"Total Income: ${total_income}")
    print(f"Total Expenses: ${total_expense}")
    print(f"Net Profit/Loss: ${total_income - total_expense}")
    
    # Expense breakdown by category
    expense_by_category = {}
    for transaction in expense_transactions.values():
        category = transaction["category"]
        amount = transaction["amount"]
        if category in expense_by_category:
            expense_by_category[category] += amount
        else:
            expense_by_category[category] = amount
    
    print("Expense Breakdown by Category:")
    for category, amount in expense_by_category.items():
        print(f"{category}: ${amount}")
 
# Test the functions
add_income(1000, "Freelance work", "Work", datetime.now().strftime("%Y-%m-%d"))
add_expense(200, "Groceries", "Food", datetime.now().strftime("%Y-%m-%d"))

generate_report()

 

