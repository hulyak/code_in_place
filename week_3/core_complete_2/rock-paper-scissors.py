"""
Implements the game of Rock-Paper-Scissors!

History:
This classic game dates back to the Han Dinesty, over 2200 years ago.
The First International Rock-Paper-Scissors Programming Competition
was held in 1999 and was won by a team called "Iocaine Powder"

The Game:
Each player choses a move (simultaneously) from the choices:
rock, paper or scissors.
If they chose the same move the game is a tie. Otherwise:
rock beats scissors
scissors beats paper
paper beats rock.

In this program a human plays against an AI. The AI choses randomly
(we promise). The game is repeated N_GAMES times and the human gets
a total score. Each win is worth +1 points, each loss is worth -1
"""
import random

N_GAMES = 3


def main():
    print_welcome()
    score = 0

    for i in range(N_GAMES):
       # 1. get the moves
        ai_move = get_ai_move()
        human_move = get_human_move()
        outcome = decide_outcome(ai_move, human_move)
        announce_result(ai_move, outcome)
        score += calc_outcome_score(outcome)

    print('your score', score)


def announce_result(ai_move, outcome):
    """
    Lets the user what the AI played and who won
    """
    print('The AI plays: ' + ai_move)
    print('The winner is: ' + outcome)
    print('')


def calc_outcome_score(outcome):
    """
    You get 1 point for winning, and lose 1 point for losing.
    >>> calc_outcome_score('tie')
    0
    >>> calc_outcome_score('human')
    1
    >>> calc_outcome_score('ai')
    -1
    """
    if outcome == 'human':
        return +1
    if outcome == 'ai':
        return -1
    return 0


def decide_outcome(ai_move, human_move):
    """
    >>> decide_outcome('rock','scissors')
    'ai'
    >>> decide_outcome('scissors','scissors')
    'tie'
    """
    # if the two moves are the same, it is a tie
    if ai_move == human_move:
        return 'tie'
    if ai_move == 'rock':
        if human_move == 'scissors':
            return 'ai'
        return 'human'
    if ai_move == 'scissors':
        if human_move == 'paper':
            return 'ai'
        return 'human'
    if ai_move == 'paper':
        if human_move == 'rock':
            return 'ai'
        return 'human'
    print('should not get here!')


def get_human_move():
    """
    make sure the human enters 'rock' 'paper' or 'scissors'
    """
    while True:
        choice = input('what do you play? ')
        if is_valid_choice(choice):
            return choice
        print('invalid choice')


def get_ai_move():
    """
    for now the AI plays randomly. But the optimal strategy is:
    If you lose, switch to the thing that beats the thing your opponent just played. 
    If you win, switch to the thing that would beat the thing that you just played.
    """
    value = random.randint(1, 3)
    if value == 1:
        return 'rock'
    if value == 2:
        return 'paper'
    return 'scissors'


def is_valid_choice(choice):
    """
    >>> is_valid_choice('rock')
    True
    >>> is_valid_choice('paper')
    True
    >>> is_valid_choice('unicorn')
    False
    """
    if choice == 'rock':
        return True
    if choice == 'paper':
        return True
    if choice == 'scissors':
        return True
    return False


def print_welcome():
    print('Welcome to Rock Paper Scissors')
    print('You will play '+str(N_GAMES)+' games against the AI')
    print('rock beats scissors')
    print('scissors beats paper')
    print('paper beats rock')
    print('----------------------------------------------')
    print('')


if __name__ == '__main__':
    main()
