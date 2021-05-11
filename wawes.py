from karel.stanfordkarel import *


def main():
    # TODO write your solution here
    make_diamond()


def make_diamond():
    put_beeper()
    for i in range(2):
        move()
        put_beeper()
        turn_right()
        move()
        put_beeper()

# There is no need to edit code beyond this point


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()


if __name__ == "__main__":
    run_karel_program()
