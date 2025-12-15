def main():
    boy_file = open('BoyNames.txt', 'r')
    popular_boys = [line.rstrip() for line in boy_file.readlines()]
    boy_file.close()

    girl_file = open('GirlNames.txt', 'r')
    popular_girls = [line.rstrip() for line in girl_file.readlines()]
    girl_file.close()

    boy = input("Enter a boy's name, or N if you do not wish to enter a boy's name: ")
    girl = input("Enter a girl's name, or N if you do not wish to enter a girl's name: ")

    if boy == 'N':
        print("You chose not to enter a boy's name.")
    elif boy in popular_boys:
        print(boy + " " + "is one of the most popular boy's names.")
    else:
        print(boy + " " + "is not a popular boy's name.")

    if girl == 'N':
        print("You chose not to enter a girl's name.")
    elif girl in popular_girls:
        print(girl + " " + "is one of the most popular girl's names.")
    else:
        print(girl + " " + "is not a popular girl's name.")

main()
