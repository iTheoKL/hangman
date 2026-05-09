import random
import string

from words import words
from hangman_visual import live_dict


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 8

    while len(word_letters) > 0 and lives > 0:
        print("You have", lives, "lives left and have used these letters: ", " ".join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(live_dict[lives])
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in (alphabet - used_letters):
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1
                print("The letter", user_letter, "is not in the word.")

        elif user_letter in used_letters:
            print("You've already guessed this letter.")
        else:
            print("Invalid input.")

    if lives == 0:
        print(live_dict[lives])
        print("You've died. The word was", word)
    else:
        print("You've guessed it right! The word was", word)


if __name__ == "__main__":
    while True:
        hangman()

        choice = input("Do you wanna play again? (Yes/no): ")

        if choice[0].upper() == 'N':
            break
