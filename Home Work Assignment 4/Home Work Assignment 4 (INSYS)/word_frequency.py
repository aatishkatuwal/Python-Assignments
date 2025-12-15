def main():
    empty_Dic = {}

    file_name = input("Enter the name of the file: ")

    with open(file_name, 'r') as file:
        words = file.read().split()
        for word in set(words):
            empty_Dic[word] = 0

        for word in words:
            empty_Dic[word] += 1

    print("{:<20} {}".format("word", "occurrences"))
    print('----------------------------------------------')

    while len(empty_Dic) > 0:
        word, count = empty_Dic.popitem()
        print("{:<20} {}".format(word, count))

main()
