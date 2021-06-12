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


attempts = 6
display = "_" * len(chosen_word)


while attempts > 0 and "_" in display:
    guess = guessLetter()
    letter_locations = []
    clear()
    correct_display = list(display)
    for letter in chosen_word:
        if letter == guess:
            # print("Right")
            letter_locations.append("right")
        else:
            # print("Wrong")
            letter_locations.append("wrong")
    for position in range(len(letter_locations)):
        if letter_locations[position] == "right":
            correct_display[position] = guess
            display = ''.join(correct_display)
    if "right" not in letter_locations and guess != "ERROR":
        attempts -= 1
        print("Wrong! Attempts left: ", end='')
        print(attempts)
    print(display)
else:
    if attempts == 0:
        print("You Lost, play again? (y/n)")
    else:
        print("You Won")

# TODO: ASCII database
# refactor¿? -> PLAY AGAIN
