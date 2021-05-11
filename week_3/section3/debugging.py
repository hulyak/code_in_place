"""
Debugging and tracing
In lecture, we discussed how to use variables maintain and update information in our program, and how to combine that ability with loops to write sophisticated programs. Using variables appropriately in loops can be tricky, and it's worth making sure you can trace through how they work and how you can resolve bugs in your program.


For example, take a look at the program below, which is supposed to compute the sum of all the numbers from 0 to 99.

Unfortunately, there is a bug in the program that results in the wrong sum being printed out due to an error in variable usage. Trace through the execution of the program to determine what might have gone wrong, and how you might fix it. 
"""


def main():
    total = 0
    for i in range(100):
        # new_total = total + i
        total = total + i
    print("The sum of the first 100 numbers is " + str(total))


if __name__ == "__main__":
    main()

# The sum of the first 100 numbers is 99  new_total
# The sum of the first 100 numbers is 4950   total
