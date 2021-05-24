"""
Number Guesser Prograam

This is an example of how to use variables to
keep track of information in a program that
also makes use of loops
"""
import random

MIN_NUMBER = 0
MAX_NUMBER = 100


def main():
    """
    make a random guess - random.randint
    while loop:
      get input from user
      higher
      lower
      correct
    display the number of guesses used
    """

    num_guesses = 0
    lower_limit = MIN_NUMBER
    upper_limit = MAX_NUMBER

    while True:
        num_guesses += 1
        guess = random.randint(lower_limit, upper_limit)

        user_response = input("Is your number " + str(guess) + "? ")

        if user_response == 'higher':
            lower_limit = guess + 1
        if user_response == 'lower':
            upper_limit = guess - 1
        if user_response == 'correct':
            break

    print("I win! It took me " + str(num_guesses) + " guesses")


if __name__ == "__main__":
    main()
