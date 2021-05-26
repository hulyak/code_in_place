from karel.stanfordkarel import *


"""
File: MoveBeeper.py
------------------------------
Karel will move the beeper up to the top of its column.
Karel starts in the bottom left corner, facing East, in front of the beeper, and Karel will end in the top right corner facing East.
"""


def main():
    # Moves beeper up 2 rows and ends Karel in the top right corner.
    find_beeper()  # Move to beeper and pick it up
    pick_beeper()
    move_to_drop_location()  # Move up 2 rows
    put_beeper()  # Put beeper down
    move()  # End in top right corner


def find_beeper():
    # Karel starts facing East in the bottom left of the world and ends up on the beeper, one spot forwards.
    move()


def move_to_drop_location():
    # Karel starts facing East in row 1 and ends facing East in row 3.
    turn_left()
    move()
    move()
    turn_right()


def turn_right():
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    run_karel_program('MoveBeeper.w')
