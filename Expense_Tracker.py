def add_expense(expenses, amount, category):
    # Add a new expense as a dictionary with amount and category
    expenses.append({'amount': amount, 'category': category})
    

def print_expenses(expenses):
    # Print all expenses in a readable format
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    

def total_expenses(expenses):
    # Calculate the total sum of all expense amounts
    return sum(map(lambda expense: expense['amount'], expenses))
    

def filter_expenses_by_category(expenses, category):
    # Return only expenses that match the given category
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    # Initialize empty list to store expenses
    expenses = []

    # Infinite loop for the menu-driven program
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
        print('6. Reset all expenses')
       
        # Get user choice
        choice = input('Enter your choice: ')

        if choice == '1':
            # Add a new expense
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            # Display all expenses
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            # Display total of all expenses
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            # Filter expenses by category
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5':
            # Exit the program
            print('Exiting the program.')
            break

        elif choice == '6':
            # Reset all stored expenses
            expenses.clear()
            print('All expenses have been reset.')


# Run the program
main()
