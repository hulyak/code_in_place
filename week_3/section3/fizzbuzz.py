"""
Prints the Fizz Buzz sequence up to a given number.
"""

FIZZ_NUM = 3
BUZZ_NUM = 5


def main():
    limit = int(input('Number to count to: '))
    for i in range(1, limit + 1):
        # start at 0 and up to not including upper limit
        if i % BUZZ_NUM == 0 and i % FIZZ_NUM:
            print('fizzbuzz')
        elif i % FIZZ_NUM == 0:
            print('fizz')
        elif i % BUZZ_NUM == 0:
            print('buzz')
        else:
            print(i)


if __name__ == '__main__':
    main()
