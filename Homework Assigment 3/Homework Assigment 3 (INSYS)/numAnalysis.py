def main():
    total = 0
    lowest = 0
    highest = 0
    average = 0.0

    number_list = []

    for i in range(1,11):
        num = float(input("Enter number "+ str(i) + " of 10: "))
        number_list.append(num)

    lowest = min(number_list)
    print("\nLow: ", format(lowest,'.2f'))

    highest = max(number_list)
    print("High: ", format(highest,'.2f'))

    total = sum(number_list)
    print("Total: ", format(total,'.2f'))

    average = total / len(number_list)
    print("Average: ", format(average,'.2f'))

main()
