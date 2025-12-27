# -------------------------------------------------
# INTERMEDIATE HANGMAN GAME
# Features:
# - Visual hangman stages
# - Hint system
# - Input validation
# - Clean game flow
# -------------------------------------------------

import random  # Used to randomly select a word

# List of words and their hints
word_list = {
    "python": "A popular programming language",
    "developer": "A person who writes code",
    "algorithm": "Step-by-step problem solving process",
    "function": "Reusable block of code",
    "variable": "Stores a value in a program"
}

# Visual stages of the hangman (from empty to full)
hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]

# Randomly choose a word and its hint
word, hint = random.choice(list(word_list.items()))

# Create a set to store guessed letters
guessed_letters = set()

# Number of wrong guesses allowed
max_attempts = len(hangman_stages) - 1
wrong_attempts = 0

print("🎮 Welcome to Hangman!")
print("Hint:", hint)

# Game loop runs until win or loss
while wrong_attempts < max_attempts:

    # Display current hangman stage
    print(hangman_stages[wrong_attempts])

    # Display word progress
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word.strip())

    # Check if player has guessed the full word
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # Ask user for a guess
    guess = input("\nEnter a letter: ").lower()

    # Input validation
    if not guess.isalpha() or len(guess) != 1:
        print("⚠ Please enter a single valid letter.")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("⚠ You already guessed that letter.")
        continue

    # Add guess to guessed letters
    guessed_letters.add(guess)

    # Check if guess is wrong
    if guess not in word:
        wrong_attempts += 1
        print("❌ Wrong guess!")

# If player loses
if wrong_attempts == max_attempts:
    print(hangman_stages[wrong_attempts])
    print("\n💀 Game Over! The word was:", word)
