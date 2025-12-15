def main():
    numbers = input("Enter a series of single-digit numbers: ")
    total = total_string(numbers)
    print("The sum of all single digit numbers is:", total)


def total_string(numbers):
    total = 0
    for char in numbers:
        total += int(char)
    return total

main()
