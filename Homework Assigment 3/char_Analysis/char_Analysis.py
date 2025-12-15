def main():

    upper_case = 0
    lower_case = 0
    digits = 0
    spaces = 0

    text_txt = open('text.txt', 'r')
    for line in text_txt:
        for char in line:
            if char.isupper():
                upper_case += 1
            elif char.islower():
                lower_case += 1
            elif char.isdigit():
                digits += 1
            elif char.isspace():
                spaces += 1

    text_txt.close()

    print("Uppercase letters:", upper_case)
    print("Lowercase letters:", lower_case)
    print("Digits:", digits)
    print("\nSpaces:", spaces)

main()
