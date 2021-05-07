"""
An example program with constants. 
Converts feet to total number of inches.
"""

# Number of inches in a foot
INCHES_IN_FOOT = 12


def main():
    feet = float(input("Enter number of feet: "))
    inches = feet * INCHES_IN_FOOT
    print("That is", inches, "inches!")


if __name__ == '__main__':
    main()
