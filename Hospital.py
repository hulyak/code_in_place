from karel.stanfordkarel import *

# File: HospitalKarel.py
# -----------------------------
# Here is a place to program your Section problem


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while front_is_clear():
        if beepers_present():
            pick_beeper()
            build_hospital()
        if front_is_clear():
            move()


def build_hospital():
    """
    pre: karel is facing east, karel is at the base of the first column of the hospital
    post: karel is facing east at the bottom of the second column of the hospital 
    """
    turn_left()
    make_column()
    turn_right()
    move()
    turn_right()
    make_column()
    turn_left()


def make_column():
    """
    pre: karel begins at the start of a column
    post: karel ends at the end of the column
    """
    put_beeper()
    for i in range(2):
        move()
        put_beeper()


def turn_right():
    for i in range(3):
        turn_left()


if __name__ == '__main__':
    run_karel_program('Hospital1.w')
