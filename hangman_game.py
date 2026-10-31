
import random

# List of words
words = ["python", "computer", "programming", "developer", "keyboard"]

# Select a random word
secret_word = random.choice(words)

guessed_letters = []
wrong_attempts = 0
max_attempts = 6

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")

# Main game loop
while wrong_attempts < max_attempts:

    # Display current word
    display_word = ""

    for letter in secret_word:

        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong Attempts:", wrong_attempts)
    print("Remaining Chances:", max_attempts - wrong_attempts)

    # Check winning condition
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You Won!")
        print("The word was:", secret_word)
        break

    # Take user input
    guess = input("\nGuess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet!")
        continue

    elif guess in guessed_letters:
        print("You already guessed this letter!")

    elif guess in secret_word:
        print("Correct Guess!")
        guessed_letters.append(guess)

    else:
        print("Wrong Guess!")
        guessed_letters.append(guess)
        wrong_attempts += 1

# Losing condition
if wrong_attempts == max_attempts:
    print("\nGAME OVER!")
    print("The correct word was:", secret_word)

print("\nThank you for playing Hangman!")
