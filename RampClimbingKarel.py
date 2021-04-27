from karel.stanfordkarel import *

"""
File: RampClimbingKarel.py
--------------------
When you finish writing this file, RampClimbingKarel should be
able to draw a line with slope 1/2 in any odd sized world
"""


def main():
    """
    draw a line with slope 1/2 in any odd sized world
    """
    while front_is_clear():
        put_beeper()
        turn_left()
        move()
        turn_right()
        move()
        move()
    put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program('RampKarel1.w')
