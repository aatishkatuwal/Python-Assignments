def prime_or_composite(n):
    has_divisor = False
    for i in range(2, n):
        if n % i == 0:
            has_divisor = True
    if has_divisor:
        print(n, "is composite.")
    else:
        print(n, "is prime.")

def main():
    user_num = int(input("Enter an integer greater than 1: "))
    numbers = []

    for i in range(2, user_num+ 1):
        numbers.append(i)
    for num in numbers:
        prime_or_composite(num)
main()


