def main():
    budgeted = float(input("Enter amount budgeted for the month: "))
    total_spent = 0.0
    expense = 1

    while expense == 1:
        b = float(input("Enter an amount spend(0 to quit): "))
        if(b == 0):
            expense = 0
        else:
            total_spent += b 

    print("\nBudgeted amount: $", format(budgeted, ',.2f'), sep='')
    print("Spent amount: $", format(total_spent, ',.2f'), sep='')

    if (budgeted > total_spent):
         print("You are $", format(budgeted - total_spent, ',.2f'), " under budget. WELL DONE!", sep='')
    elif budgeted < total_spent:
        print("You are $", format(total_spent - budgeted, ',.2f'), " over budget. PLAN BETTER NEXT TIME!", sep='')
    else:
        print("You spent exactly as much as you budgeted. GOOD PLANNING!")
main()
