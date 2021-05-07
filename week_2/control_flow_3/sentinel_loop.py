"""
Asks the user for a number until they enter -1
Reports the total value of all the numbers at the end
"""

SENTINEL = -1


def main():
    score = int(input("Type a number: "))
    total = 0
    scoreCounter = 0
    while score != SENTINEL:
        total += score
        scoreCounter = scoreCounter + 1
        score = int(input("Type a number, use -1 to stop: "))
    print("The average for the test is ", str(total/scoreCounter))


# 2nd solution
total = 0
while True:
    num = int(input("Enter a number: "))
    if num == -1:
        break  # immediately exits loop
    total += num
print("total is ", total)


if __name__ == '__main__':
    main()
