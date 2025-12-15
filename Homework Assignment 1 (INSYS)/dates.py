month = int(input("Enter the month: "))
day = int(input("Enter the day: "))
year = int(input("Enter year: "))

if month < 1 or month > 12:
    print("Error")
elif day < 1 or day > 31:
    print("Error")
elif year < 0 or year > 99:
    print("Error")
else:
    if month * day == year:
        print("The date is", month,"/", day, "/", year)
        print("This is a magic date!")
    else:
        print("The date is", month,"/", day, "/", year)
        print("This is not a magic date!")
