from karel.stanfordkarel import *

"""
File: Mountain.py
----------------------------
Karel climbs a mountain of any size and plants a beeper at the top.
"""


def main():
    # Milestone 1: climb the mountain and put a beeper!!
    ascend_mountain()
    put_beeper()
    # Milestone 2: bring it on home!!!
    descend_mountain()


def descend_mountain():
    while front_is_clear():
        step_down()


def step_down():
    # Pre: Karel is on a edge (right side of mountain) facing east
    # Post: Karel is on a lower ledge. facing east
    move()
    turn_right()
    move()
    # This means karel is an eastwardly facing robot
    turn_left()


def ascend_mountain():
    while front_is_blocked():
        step_up()


def step_up():
    turn_left()
    move()
    turn_right()
    move()


def turn_right():
    # Makes karel turn in the clockwise direction.
    # Works in any pre-condition state!
    for i in range(3):
        turn_left()


if __name__ == '__main__':
    run_karel_program('Mountain2.w')
