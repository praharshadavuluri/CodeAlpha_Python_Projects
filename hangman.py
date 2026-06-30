import random

# List of words
words = ["apple", "python", "computer", "keyboard", "flower"]

# Randomly choose one word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
attempts = 6

print("===================================")
print("      WELCOME TO HANGMAN GAME")
print("===================================")

while attempts > 0:

    display_word = ""

    # Display guessed letters
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if word is completed
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct Guess!")
    else:
        attempts -= 1
        print("Wrong Guess!")
        print("Remaining Attempts:", attempts)

if attempts == 0:
    print("\nGame Over!")
    print("The word was:", word)