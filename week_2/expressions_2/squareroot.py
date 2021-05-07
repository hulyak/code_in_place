"""
This program asks the user for a number
and prints its square root.
"""

import math


def main():
    num = float(input("Enter number: "))
    root = math.sqrt(num)
    print("Square root of", num, "is", root)


if __name__ == '__main__':
    main()
