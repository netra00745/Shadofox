import random

# Words list
words = ["python", "programming", "hangman", "developer", "internship"]

# Hangman stages
stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ---------
    """
]

def play_game():
    word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    max_attempts = len(stages) - 1

    print("\n🎮 Welcome to Hangman!")

    while wrong_guesses < max_attempts:
        print(stages[wrong_guesses])

        # Display word
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word.strip())

        # Win condition
        if "_" not in display_word:
            print("\n🎉 Congratulations! You won!")
            return

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print("⚠ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            wrong_guesses += 1
            print("❌ Wrong guess!")

    # Lose condition
    print(stages[wrong_guesses])
    print("\n💀 Game Over!")
    print("The word was:", word)

# Play again loop
while True:
    play_game()
    again = input("\nDo you want to play again? (yes/y or no/n): ").lower()
    if again not in ["yes", "y"]:
        print("👋 Thanks for playing Hangman!")
        break
