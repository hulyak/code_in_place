"""
File: khansole_extension.py
------------------
randomly generate addition problems until the user has gotten 3 problems correct in a row. (Note: the number of problems the user needs to get correctly in a row to complete the program is just one example of a good place to specify a constant in your program).

"""

import random
MIN_RANDOM = 10
MAX_RANDOM = 99


def main():
    count = 0
    while count < 3:
        rand_1 = random.randint(MIN_RANDOM, MAX_RANDOM)
        rand_2 = random.randint(MIN_RANDOM, MAX_RANDOM)
        print(f"What is {rand_1} + {rand_2} ?")

        total = int(rand_1) + int(rand_2)
        answer = input("Your answer: ")

        if int(answer) == total:
            count += 1
            print(f"Correct! You've gotten {count} correct in a row ")
        else:
            print(f"Incorrect.The expected answer is {total}")
            # Restarting the count in zero
            count = 0

    # If the answer of the user is incorrect, print the value of the expected value
    print("Congratulations! You mastered addition.")

    # This provided line is required at the end of a Python file
    # to call the main() function.
if __name__ == '__main__':
    main()
