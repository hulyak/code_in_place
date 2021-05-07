# Constant – visible to all functions
MAX_NUM = 9


def main():
    # repeat for several values!
    for i in range(MAX_NUM+1):
        print(i, factorial(i))


def factorial(n):
    """
    This function returns the factorial of n 
    Input: n (number to compute the factorial of)
    Returns: value of n factorial
    Calculates n factorial.
    5 factorial is 5 * 4 * 3 * 2 * 1
    Doctests:
    >>> factorial(5)
    120
    >>> factorial(4)
    24
    >>> factorial(3)
    6
    >>> factorial(1)
    1
    >>> factorial(0)
    1
    """
    result = 1
    for i in range(1, n+1):
        # [1, 2, 3]
        result *= i
    return result


if __name__ == '__main__':
    main()
