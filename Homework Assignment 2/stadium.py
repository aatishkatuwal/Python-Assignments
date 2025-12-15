def main():
    income_Aseats = 0.0
    income_Bseats = 0.0
    income_Cseats = 0.0
    category = ""
    num_tickets = 0
    seating_price = 0.0
    need_more_tickets = 'Y'
    
    print("Welcome to the Stadium Seating Application")
    print("\nCategory A - $20 \nCategory B - $15 \nCategory C - $10") 

    while need_more_tickets == 'Y':
        category, num_tickets = getUserInput()
        seating_price = getSeatingPrice(category)
        income = seating_price * num_tickets

        if category == 'A':
            income_Aseats += income
        elif category == 'B':
            income_Bseats += income
        elif category == 'C':
            income_Cseats += income

        need_more_tickets = input("Do you need more tickets? Press Y to continue or press N to Quit: ").upper()

    showIncome(income_Aseats, income_Bseats, income_Cseats)

def showIncome(income_Aseats, income_Bseats, income_Cseats):
    total_income = income_Aseats + income_Bseats + income_Cseats
    print("Income from class A seats: $", format(income_Aseats, '.2f'))
    print("Income from class B seats: $", format(income_Bseats, '.2f'))
    print("Income from class C seats: $", format(income_Cseats, '.2f'))
    print("\nTotal income: $", format(total_income, '.2f'))

def getSeatingPrice(category):
    if category == 'A':
        return 20.00
    elif category == 'B':
        return 15.00
    elif category == 'C':
        return 10.00
    else:
        return 0.0

def getUserInput():
    category = input("\nEnter the Category (A, B, or C): ").upper()
    num_tickets = int(input("Enter the number of tickets required: "))
    return category, num_tickets    
    
main()
