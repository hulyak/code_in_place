def main():
    print("Welcome to the CodeInPlace Game Show")
    print("Pick a door and win a prize")
    print("------------------------------------")

    # Part 1: get the door number form the user
    door = int(input("Door: "))
    # while the input is invalid
    while door < 1 or door > 3:
        # tell the user the input was invalid
        print("Invalid door!")
        # ask for a new input
        door = int(input("Door: "))

    # Part 2: compute the prize
    prize = 4
    if door == 1:
        prize = 2 + 9 // 10 * 100
    elif door == 2:
        locked = prize % 2 != 0
        if not locked:
            prize += 6
    elif door == 3:
        for i in range(door):
            prize += i

    # Part 3: report the prize
    print('You win ' + str(prize) + ' treats')


if __name__ == '__main__':
    main()
