from karel.stanfordkarel import *

"""
diagnostic problem
Write a program that has Karel draw four small "waves". Each wave is a triangle made up of three beepers. There is a gap between each wave. 

This problem reviews basic control flow with Karel. It was much easier to solve if you defined a make_wave() function. It also introduces a fence-post problem where you need to move between waves three times, but you need to draw four waves. 
"""


def main():
    # make the first three waves
    for i in range(3):
        build_wave()
        # you need to move twice to go between waves
        move()
        move()
    # because of the fencepost bug, we need a fourth wave
    build_wave()


def build_wave():
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    turn_around()
    move()
    turn_left()


def turn_around():
    turn_left()
    turn_left()

# Example Solution 2
# def main():
#     # you can also solve this problem with a while loop
#     while front_is_clear():
#         build_wave()
#         # you might be facing a wall at this point!
#         if front_is_clear():
#             move()
#             move()


# def build_wave():
    # same as in solution 1

if __name__ == "__main__":
    run_karel_program('Roomba2.w')
