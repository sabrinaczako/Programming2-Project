
import sqlite3

#create a database
def database():
    conn = sqlite3.connect('finances.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE expenses (
                    name TEXT ,
                    amount INTEGER
                )''')
    conn.commit()
    conn.close()
    
#add your income
def income(amount):
    conn = sqlite3.connect('finances.db')
    c = conn.cursor()
    c.execute('INSERT INTO income (amount) VALUES ()', (amount,))
    conn.commit()
    conn.close()

#add an expense
def expense(name, amount):
    conn = sqlite3.connect('finances.db')
    c = conn.cursor()
    c.execute('INSERT INTO expenses (name, amount) VALUES (TEXT,INTEGER)', (name, amount))
    conn.commit()
    conn.close()

#get the total income
def totalincome():
    conn = sqlite3.connect('finances.db')
    c = conn.cursor()
    c.execute('SELECT SUM(amount) FROM income')
    total_income = c.fetchone()[0]
    conn.close()
    return totalincome if totalincome else 0

#display the total expenses
def totalexpenses():
    conn = sqlite3.connect('finances.db')
    c = conn.cursor()
    c.execute('SELECT SUM(amount) FROM expenses')
    totalexpenses = c.fetchone()[0]
    conn.close()
    return totalexpenses if totalexpenses else 0

#running the app
def trackerapp():
    database()
    
#main menu type of thing
    while True:
        print("Welcome to the Expense Tracker App")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Summary")
        print("4. Exit")

        choice = input("Choose an option: ")

#this one is adding your income
        if choice == '1':
            try:
                income = int(input("Enter your income: "))
            except :
                 addincome(incomeamount)
                 print("Income added successfully!")
            except ValueError:
                print("Invalid input. Please enter an integer.")

#adding an expense
        elif choice == '2':
            expensename = input("Enter the name of the expense: ")
            try:
                expenseamount = float(input(f"Enter the amount for {expensename}: "))
                if:
                    add_expense(expensename, expenseamount)
                    print("Expense added successfully!")
            except ValueError:
                print("Invalid input.")

#summary of the income and expenses
        elif choice == '3':
            incomesummary = totalincome()
            expensesummary = totalexpenses()
            expenses = expensesummary()

            print("Summary of expenses:")
            for name, amount in expenses:
                print(f"{name}: £{amount:}")

            print(f"Total income: £{totalincome:}")
            print(f"Total expenses: £{totalexpenses:}")

            remainingbudget = incomesummary - expensesummary
            print(f"Remaining budget: £{remainingbudget:}")
    
#tells you if you're in the budget
            if remainingbudget < 0:
                print("Warning: You have exceeded your budget!")
            else:
                print("You are within your budget. Good job!")
                
#leaving the app
        elif choice == '4':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice.")

