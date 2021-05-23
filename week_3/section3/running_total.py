"""
Running Total
Write a program that asks a user to continuously enter numbers and print out the running total, the sum of all the numbers so far. Once you get the program working, see if you can modify it so that the program stops when the user enters a 0. sentinel number 0

Enter a value: 7
Running total is 7

Enter a value: 3
Running total is 10

Enter a value: 5
Running total is 15

Enter a value: 12
Running total is 27

Enter a value: 0

Tip: If your program is looping without stopping, you can press Control + C to quit it.


Extension

If you solve this problem quickly, think about how you might extend the program to also keep track of the minimum and maximum numbers entered so far as well. A sample run of this extended program might look like this:


Enter a value: 42
Running total is 42
Maximum so far is 42
Minimum so far is 42

Enter a value: 3
Running total is 45
Maximum so far is 42
Minimum so far is 3

Enter a value: -6
Running total is 39
Maximum so far is 42
Minimum so far is -6

Enter a value: 0


Prompts the user to enter numbers and prints
the running total until the user enters 0.
"""

SENTINEL = 0


def main():
    # Fill this function out!
    user_number = int(input('Enter a value: '))
    total = user_number
    while user_number != SENTINEL:
        print('Running total is ', str(total))
        print('')
        user_number = int(input('Enter a value: '))
        total = total + user_number


if __name__ == '__main__':
    main()
