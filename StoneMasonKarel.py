

from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
When you finish writing code in this file, StoneMasonKarel should be
able to solve the "repair the quad" problem from Assignment 1.
You should make sure that your program works for all of the
sample worlds supplied in the starter folder.
"""


def main():
    """
    repair each column and move to next one until you reach the wall
    """

    while front_is_clear():
        column_repair()
        move_to_next_column()
    column_repair()


def move_to_next_column():
    for i in range(4):
        move()


def column_repair():
    turn_left()
    put_line_of_beepers()
    turn_around()
    move_to_wall()
    turn_left()


def put_line_of_beepers():
    while front_is_clear():
        fn_put_beeper()
        move()
    fn_put_beeper()


def fn_put_beeper():
    if no_beepers_present():
        put_beeper()


def turn_around():
    turn_left()
    turn_left()


def move_to_wall():
    while front_is_clear():
        move()


if __name__ == '__main__':
    run_karel_program('SampleQuad1.w')
