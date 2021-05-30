"""
File: word_guess.py
-------------------
Fill in this comment.
"""

import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


# def play_game(secret_word):
#     """
#     Add your code (remember to delete the "pass" below)
#     """
#     word_completion = "-" * len(secret_word)
#     guessed = False
#     guessed_letters = []
#     guessed_words = []
#     remaining_guesses = 8
#     while not guessed and tries > 0:
#         # random_word = random.choice(words_list)
#         # create dashes as long as the word's length
#         print('The word now looks like this: ', word_completion)
#         print(f"You have {remaining_guesses} guesses left")
#         guess = input("Type a single letter here, then press enter: ").upper()
#         if len(guess) == 1 and guess.isalpha():
#             if guess in guessed_letters:
#                 print("")

#         elif len(guess) == len(secret_word) and guess.isalpha():

#         else:
#             print(f"There are no {guess}'s in the word")

#         word_completion = ("-" * len(secret_word)) - 1
#         remaining_guesses -= 1
#         print(f"The word now looks like this: {word_completion}")
#         print(f"You have {remaining_guesses} guesses left")


#         remaining_guesses += 1


# def get_word():
#     """
#     This function returns a secret word that the player is trying
#     to guess in the game.  This function initially has a very small
#     list of words that it can select from to make it easier for you
#     to write and debug the main game playing program.  In Part II of
#     writing this program, you will re-implement this function to
#     select a word from a much larger list by reading a list of words
#     from the file specified by the constant LEXICON_FILE.
#     """
#     words_list = []
#     with open(LEXICON_FILE) as file:
#         for line in file: # for-each loop gives lines one at a time
#             words_list.append(line.strip()) # strip removes whitespace at the start or end

#     index = random.randrange(3)
#     # word = random.choice(words_list)
#     return word.upper()
#     if index == 0:
#         return 'HAPPY'
#     elif index == 1:
#         return 'PYTHON'
#     else:
#         return 'COMPUTER'


def get_word():
    word_list = []
    with open(LEXICON_FILE) as file:
        for line in file:  # for-each loop gives lines one at a time
            # strip removes whitespace at the start or end
            word_list.append(line.strip())

    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(
                    word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " +
              word + ". Maybe next time!")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    # secret_word = get_word()
    # play_game(secret_word)

    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
