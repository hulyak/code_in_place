from karel.stanfordkarel import *

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """

    """
    put_beeper()
    while front_is_clear():
        move()
    turn_around()
    put_beeper()
    if front_is_blocked():
        pick_beeper()
    else:
        move()
    clean_beepers()
    if beepers_present():
        turn_around()
    else:
        put_beeper()


def turn_around():
    turn_left()
    turn_left()


def clean_beepers():
    while no_beepers_present():
        move()
        if beepers_present():
            pick_beeper()
            turn_around()
            move()
            put_beeper()
            move()
    if beepers_present():
        turn_around()
        pick_beeper()
        if front_is_blocked():
            turn_around()
        else:
            move()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program('Midpoint.w')
