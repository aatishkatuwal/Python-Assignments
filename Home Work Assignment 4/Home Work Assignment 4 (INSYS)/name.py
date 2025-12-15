def main():
    full_name = input("Enter full name: ")
    name_list = full_name.split()

    for i in range(len(name_list)):
        print(name_list[i][0]+".", end="")

main()
