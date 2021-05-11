"""
File: hello.py
------------------
Prompts user for their name and then says hello!
"""


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    name = input("What is your name? ")
    print("Hello " + name + "!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
