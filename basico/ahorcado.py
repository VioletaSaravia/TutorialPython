import random
import os


def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')


word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)


def guessLetter():
    letter = input("Guess a letter: ")
    if len(letter) == 1:
        guess = letter.lower()
        return guess
    else:
        print("not a letter")  # should be an error actually
        return "ERROR"


# attempts = 6


def play(attempts):
    display = "_" * len(chosen_word)
    while attempts > 0 and "_" in display:
        # play(attempts, display) + chosen_word before while
        guess = guessLetter()
        letter_locations = []
        clear()
        for letter in chosen_word:
            # checkGuess(chosen_word, guess)
            if letter == guess:
                # print("Right")
                letter_locations.append("right")
            else:
                # print("Wrong")
                letter_locations.append("wrong")

        def updateDisplay():
            nonlocal display  # WRONG. do display = updateDisplay(display, l_l)
            nonlocal letter_locations
            correct_display = list(display)
            nonlocal guess
            for position in range(len(letter_locations)):
                # updateDisplay(letter_locations, display)
                if letter_locations[position] == "right":
                    correct_display[position] = guess
                    display = ''.join(correct_display)
                    # Immutable strings workaround
            return
        updateDisplay()
        if "right" not in letter_locations and guess != "ERROR":
            attempts -= 1
            print("Wrong! Attempts left: ", end='')
            print(attempts)
        print(display)
    else:  # endScreen(play) -> replay
        if attempts == 0:
            replay = input("You Lost, play again? (y/n) ")
        else:
            replay = input("You Won. Play again? (y/n) ")
        if replay == "y":
            return play(6)
        else:
            print("Goodbye!")
            return


play(6)

# TODO: ASCII database
# refactor¿? -> PLAY AGAIN
# programar en ESPAÑOL
# settings menu
# keypresses en vez de input¿?
