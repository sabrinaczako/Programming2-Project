import sqlite3

#create a database
def database():
    conn = sqlite3.connect('finances.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS expenses (
                    name TEXT,
                    amount INTEGER
                )''')
    conn.commit()
    conn.close()
    
#add your income
def add_income(amount):
    conn = sqlite3.connect('finances.db')
    c = conn.cursor()
    c.execute('INSERT INTO income (amount) VALUES (?)', (amount,))
    conn.commit()
    conn.close()

#add an expense
def add_expense(name, amount):
    conn = sqlite3.connect('finances.db')
    c = conn.cursor()
    c.execute('INSERT INTO expenses (name, amount) VALUES (?, ?)', (name, amount))
    conn.commit()
    conn.close()

#get the total income
def total_income():
    conn = sqlite3.connect('finances.db')
    c = conn.cursor()
    c.execute('SELECT SUM(amount) FROM income')
    total_income = c.fetchone()[0]
    conn.close()
    return total_income if total_income else 0

#display the total expenses
def total_expenses():
    conn = sqlite3.connect('finances.db')
    c = conn.cursor()
    c.execute('SELECT SUM(amount) FROM expenses')
    total_expenses = c.fetchone()[0]
    conn.close()
    return total_expenses if total_expenses else 0

#display expenses
def get_expenses():
    conn = sqlite3.connect('finances.db')
    c = conn.cursor()
    c.execute('SELECT name, amount FROM expenses')
    expenses = c.fetchall()
    conn.close()
    return expenses

#running the app
def financeapp():
    database()
    
#main menu type of thing
    while True:
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Summary")
        print("4. Exit")

        choice = input("Choose an option: ")

#this one is adding your income
        if choice == '1':
            try:
                income_amount = float(input("Enter your income: "))
                add_income(income_amount)
                print("Income added successfully!")
            except ValueError:
                print("Invalid input.")

#adding an expense
        elif choice == '2':
            expense_name = input("Enter the name of the expense: ")
            try:
                expense_amount = int(input("Enter the amount: "))
                add_expense(expense_name, expense_amount)
                print("Expense added successfully!")
            except ValueError:
                print("Invalid input.")

#summary of income and expenses
        elif choice == '3':
            income_summary = total_income()
            expense_summary = total_expenses()
            expenses = get_expenses()

            print("Summary of expenses:")
            for name, amount in expenses:
                print(f"{name}: £{amount}")

            print(f"Total income: £{income_summary}")
            print(f"Total expenses: £{expense_summary}")

            remaining_budget = income_summary - expense_summary
            print(f"Remaining budget: £{remaining_budget}")
    
#tells you if you're in the budget
            if remaining_budget < 0:
                print(" You have exceeded your budget!")
            else:
                print("You are within your budget.")
                
#leaving the app
        elif choice == '4':
            print("Goodbye")


# Start the app
financeapp()
