
"""
The fix to this bug has two parts. You need to add a return to divide_and_round and you need to use the returned value when calling divide_and_round in main.
"""


def divide_and_round(n):
    """
    Divides an integer n by 2 and rounds 
    up to the nearest whole number
    """
    if n % 2 == 0:
        n = n / 2
    else:
        n = (n + 1) / 2


def main():
    n = 10
    divide_and_round(n)
    print(n)  # should print 5


"""
Part A: The program prints 10. 
The divide_and_round function correctly divides n by 2 and rounds up 
to the nearest whole number, but does not return or print n. Therefore, the  value of n in main’s print statement is still 10, and so 10 gets printed.
"""

"""
Part B: Here is the fixed program
"""


def divide_and_round(n):
    """
    Divides an integer n by 2 and rounds 
    up to the nearest whole number
    """
    if n % 2 == 0:
        n = n / 2
    else:
        n = (n + 1) / 2
    # this function should return n
    return n


def main():
    n = 10
    # use the x = change(x) paradigm to make sure main's n is changed
    n = divide_and_round(n)
    print(n)
