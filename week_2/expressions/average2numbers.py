"""
This program asks the user for two numbers and prints their average.
This program is BUGGY because it doesn't compute average correctly.
You need to modify the line: average = num1 + num2 / 2
to make the program work correctly. Try to make that modification
here and then you can check the solution.
"""


def main():
    print("This program averages two numbers.")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    average = (num1 + num2) / 2        # buggy!
    print("The average is", average)


if __name__ == '__main__':
    main()
