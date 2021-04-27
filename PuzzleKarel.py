from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper (puzzle piece) and placing it in the right spot.
Karel should end in the same position Karel starts in -- the bottom left corner of the world.
"""


def main():
    """
    pick up the last beeper and place it in the right spot
    """
    picking_beeper()
    complete_puzzle()
    return_back()


def picking_beeper():
    move()
    move()
    pick_beeper()


def complete_puzzle():
    move()
    turn_left()
    move()
    move()
    put_beeper()


def return_back():
    turn_around()
    move()
    move()
    turn_right()
    move()
    move()
    move()
    turn_left()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


def turn_around():
    for i in range(2):
        turn_left()

    # There is no need to edit code beyond this point
if __name__ == "__main__":
    run_karel_program('Puzzle.w')
