"""
Zebra Crossing Karel
"""

from karel.stanfordkarel import *


def turn_right():
    for i in range(3):
        turn_left()


def move_to_next_stripe():
    """
    precondition: Karel is at the bottom right of the stripe and is facing East
    postcondition: Karel is at the bottom left of the next stripe
    """
    for i in range(4):  # 3 stripes
        move()


def beeper_column():
    """
    Precondition: Karel is at the start of the column, facing the right direction
    Postcondition: Karel is at the end of the column 
    """
    put_beeper()  # fence post problem
    while front_is_clear():
        move()
        put_beeper()


def draw_stripe():
    """
    Precondition: 
      Karel is at the bottom left corner of a stripe
      Karel starts by facing East
    Postcondition:
      Karel is at the bottom right corner of a stripe
      Karel is facing East
    """
    turn_left()
    beeper_column()
    turn_right()
    move()
    turn_right()
    beeper_column()
    turn_left()


def main():
    draw_stripe()
    while front_is_clear():
        # move across the 3-square gap
        # make a column of two beepers
        move_to_next_stripe()
        draw_stripe()


if __name__ == "__main__":
    run_karel_program('ZebraCrossingKarel1.w')
