import math

# The constant K in the half life formula
K = -8266.64258429376

"""
Write a program to calculate how old something is.

Input: what percent of c14 is remaining in the sample?
"""


def main():
    calculate_age_single_sample()


def calculate_age_single_sample():
    # ask the user to enter the percent c14 left in their sample
    pct_left = float(input("% of natural c14: "))
    # calc the age: https://en.wikipedia.org/wiki/Radiocarbon_dating
    age = K * math.log(pct_left / 100)
    # print the result
    print("Sample is " + str(age) + " years old.")


# tells python to call main when the program starts
if __name__ == '__main__':
    main()
