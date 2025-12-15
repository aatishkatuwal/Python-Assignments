def main():
    total_pay = 0
    pennies = 0.01 #salary

    days = int(input("Number of days: "))

    print("Day\tPennies")
    print("----------------")

    for day in range(1, days+1):
        print(day,"$", format(pennies))
        total_pay += pennies
        pennies *= 2

    print("\nThe total salary for", days, "days is: $", format(total_pay,".2f"))

main()
    
