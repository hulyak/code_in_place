from karel.stanfordkarel import *

"""
File: Archway.py
------------------------------
Karel will move up and over the archway.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    turn_left()
    move_three_times()
    turn_right()
    move_three_times()
    turn_right()
    move_three_times()
    turn_left()


def move_three_times():
    for i in range(3):
        move()


def turn_right():
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    run_karel_program('Archway.w')
