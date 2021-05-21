"""
Print out each of the numbers 1 through 100 and whether that number is even or odd. 100 is specified using a constant MAX_NUMBER
"""
# Example Solution 1
MAX_NUMBER = 100


def main():
    # if you don't go until MAX_NUMBER+1, range will stop short
    for i in range(1, MAX_NUMBER+1):
        # you can use the variable i in the body of the loop
        if i % 2 == 0:
            # be careful printing. You can't add an int to a string
            print(i, 'is even')
        else:
            print(i, 'is odd')


# Example Solution 2
def main():
    # this variable recreate the "i" in a for loop
    curr = 1
    # this problem is probably better suited to a for loop
    while curr <= MAX_NUMBER:
        if curr % 2 == 0:
            print(curr, 'is even')
        else:
            print(curr, 'is odd')
        # in a while loop you must increment curr. In the for loop
        # i is incremented for you!
        curr += 1
