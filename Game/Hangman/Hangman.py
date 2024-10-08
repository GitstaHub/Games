
from random import randint
from HangmanDB import words
import argparse

dbg = 0
def get_random_word():
    index = randint(0,len(words)-1)
    return words[index]

def is_letter_in_word(letter, word):
    return letter.lower() in word

def check_valid_input(letter):
    return len(letter) == 1 and letter.isalpha()

def main():
    word = get_random_word()
    allowed_errors = 7

    guesses = []

    done = False

    while not done:
        for letter in word:
            if is_letter_in_word(letter, guesses) :
                print(letter, end=" ")
            else:
                print("_", end=" ")
        while True:
            if dbg:
                guess = input(f"\nAllowed Errors Left {allowed_errors}, Next Guess: ({word.lower()})")
            else :
                guess = input(f"\nAllowed Errors Left {allowed_errors}, Next Guess: ")

            if check_valid_input(guess):
                break
        guesses.append(guess.lower())
        if not is_letter_in_word(guess, word):
            allowed_errors -= 1
            if allowed_errors == 0:
                break

        done = True
        for letter in word:
            if not is_letter_in_word(letter, guesses):
                done = False

    if done:
        print(f"You found the word! It was {word}!")
    else:
        print(f"Game Over! The word was {word}!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--arg', type=str, help='An optional argument')

    args = parser.parse_args()
    result =  args.arg if args.arg is not None else "Default Value"
    dbg = result.lower() in ["dbg","d","debug"]
    main()
