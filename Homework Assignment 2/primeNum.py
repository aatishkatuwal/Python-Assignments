def main():
    start_num = 1
    end_num = 10

    print("number is prime")
    print("------------------------")

    for num in range(start_num, end_num + 1):
        if is_prime(num):
            print(num, "prime")
        else:
            print(num, "not prime")

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

main()
