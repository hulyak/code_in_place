"""
Prints the Fizz Buzz sequence up to a given number.
"""

FIZZ_NUM = 3
BUZZ_NUM = 5


def main():
    limit = int(input('Number to count to: '))

    num_fizzed = 0
    num_buzzed = 0
    num_fizzbuzzed = 0

    for i in range(1, limit + 1):
        # start at 0 and up to not including upper limit
        if i % BUZZ_NUM == 0 and i % FIZZ_NUM == 0:
            print('fizzbuzz')
            num_fizzbuzzed += 1
        elif i % FIZZ_NUM == 0:
            print('fizz')
            num_fizzed += 1
        elif i % BUZZ_NUM == 0:
            print('buzz')
            num_buzzed += 1
        else:
            print(i)

    print('Num fizzed: ' + str(num_fizzed))
    print('Num buzzed: ' + str(num_buzzed))
    print('Num fizzbuzzed: ' + str(num_fizzbuzzed))


def main2():
    limit = int(input("Enter a limit: "))
    number = 0

    while(number < limit):
        number = number + 1
        # if the number is divisble by 3 and 5
        if(number % 3 == 0 and number % 5 == 0):
            print("fizzbuzz")
        elif(number % 3 == 0):  # if the number is divisible by 3
            print("fizz")
        elif(number % 5 == 0):  # if the number is divisible by 5
            print("buzz")
        else:
            print(number)


if __name__ == '__main__':
    main()
