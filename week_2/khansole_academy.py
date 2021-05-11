"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    rand_1 = random.randint(10, 99)
    rand_2 = random.randint(10, 99)
    total = rand_1 + rand_2
    print("What is " + str(rand_1) + " + " + str(rand_2) + " ?")
    answer = int(input("Your answer: "))
    if int(answer) != (int(total)):
        print("Incorrect. The expected answer is " + str(total))
    else:
        print("Correct!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
