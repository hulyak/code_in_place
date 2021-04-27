from karel.stanfordkarel import *


def main():
    for i in range(4):
        cover_one_side()
        turn_left()


def cover_one_side():
    while front_is_clear():
        put_beeper()
        move()


if __name__ == '__main__':
    run_karel_program()
