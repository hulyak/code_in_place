import random

# Name of the file to read in!
FILE_NAME = 'cswords.txt'


def main():
    # TODO: your code here
    with open('words.txt') as file:
        for line in file:  # for-each loop gives lines one at a time
            print(line.strip())  # strip removes whitespace at the start or end


chosen_value = random.choice(my_list)  # comes with ‘import random’


if __name__ == '__main__':
    main()
