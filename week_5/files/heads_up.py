import random

"""
Our next goal is to learn how to read data from files. Loading data from a file can be useful for many final projects. Write a program that runs a console version of the phone game Heads Up!

Milestone #1: First, load all of the words from the file cswords.txt into a list.

Milestone #2: Then, show a randomly chosen word from the list

Milestone #3: Repeat: wait for the user to hit enter, then show another word.

"""


# Name of the file to read in!
FILE_NAME = 'cswords.txt'


def main():
    # TODO: your code here
    cs_words_list = []
    with open('cswords.txt') as file:
        for line in file:  # for-each loop gives lines one at a time
           # print(line.strip()) # strip removes whitespace at the start or end
            cs_words_list.append(line.strip())

    # print(cs_words_list)
    while(True):
        index = random.randint(0, len(cs_words_list))
        input(cs_words_list[index])


if __name__ == '__main__':
    main()
