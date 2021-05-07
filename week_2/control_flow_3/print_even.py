"""
Example of using the index variable of a for loop
"""


def main():
    for i in range(100):
        # in a for loop, you have access to
        # a variable which knows how many times the loop
        # has completed
        print(i * 2)


if __name__ == '__main__':
    main()
