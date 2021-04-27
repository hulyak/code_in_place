from karel.stanfordkarel import *

"""
File: Roomba.py
----------------------------
Karel picks up all the beepers in the world.
"""


def main():
    while left_is_clear():
        # pre: karel is facing east at the start of a row
        clear_row()
        next_row()
        # post: karel is facing east at the start of the next row
    # fence post
    clear_row()

# Removes all beepers from one row


def clear_row():
    while front_is_clear():
        safe_pick()
        move()
    safe_pick()

# Picks up a beeper... if there is one!


def safe_pick():
    if beepers_present():
        pick_beeper()

# Karel moves up one row. Facing east pre + post


def next_row():
    turn_around()
    move_to_wall()
    turn_right()
    move()
    turn_right()

# Move until Karel hits a wall


def move_to_wall():
    while front_is_clear():
        move()

# If only Karel knew by default


def turn_around():
    turn_left()
    turn_left()

# Recall, not an ambi turner


def turn_right():
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    run_karel_program('Roomba2.w')
