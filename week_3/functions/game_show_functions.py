def main():
    print("Welcome to the CodeInPlace Game Show")
    print("Pick a door and win a prize")
    print("------------------------------------")

    # Part 1: get the door number form the user
    door = get_door_choice()

    # Part 2: compute the prize
    prize = calculate_prize(door)

    # Part 3: report the prize
    print('You win ' + str(prize) + ' treats')


def get_door_choice():
    """
    Asks the user for a door. Keeps reprompting until they enter a valid input (door 1, 2 or 3)
    """
    door = int(input("Door: "))
    # while the input is invalid
    while door < 1 or door > 3:
        # tell the user the input was invalid
        print("Invalid door!")
        # ask for a new input
        door = int(input("Door: "))


def calculate_prize(door):
    """
    Based on the door choice, returns the prize.
    Assumes that the door value is an integer which 
    must be 1, 2 or 3. Returns a number.
    """
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
    return prize


if __name__ == '__main__':
    main()
