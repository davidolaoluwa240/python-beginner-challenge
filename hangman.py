# Challenge
#

# Import modules
from random import randint

def hangman():
    # States
    words = []
    user_correct_guess = []
    attempts_left = 7

    # 1. Get words from file
    with open("hangman_words.txt", "r") as file:
        # 1a. Update words list
        words.extend(file.read().split())

    # 2. Get hidden guess and length of hidden guess
    hidden_guess = words[randint(0, len(words) - 1)]
    hidden_guess_length = len(hidden_guess)
    print("Your hidden word: ", hidden_guess)

    user_correct_guess = ["_"] * hidden_guess_length

    # 3. While user still have attempts live and user correct guess is not equal to hidden guess keep playing game
    while attempts_left != 0 and "".join(user_correct_guess) != hidden_guess:
        # 3a. Print message
        print(f"""Here's the word:
{"".join(user_correct_guess)}({hidden_guess_length} letters)
You have {attempts_left} lives remaining.
""")

        # 3b. Get user guess
        user_guess = input("Enter the character you think the word may have: ").lower()

        # 3c. validate user input
        if len(user_guess) > 1:
            print("===================\n===================")
            print("Error💥💥: You can only enter a single letter")
            print("===================\n===================")
            continue

        #
        if user_guess not in hidden_guess:
            attempts_left -= 1

            print(f"""
Good choice! Let's see if {user_guess.upper()} is in the word...
{"".join(user_correct_guess)}
{user_guess.upper()} do not appears in the word!
You have {attempts_left} lives remaining.
            """)

            match attempts_left:
                case 0:
                    print("----------")
                    print("   ( )-|  ")
                    print("  - | -    ")
                    print(r"   / \     ")

                case 1:
                    print("----------")
                    print("   ( )-   ")
                    print("  - | -    ")
                    print(r"   / \     ")

                case 2:
                    print("----------")
                    print("   ( )    ")
                    print("  - | -    ")
                    print(r"   / \     ")

                case 3:
                    print("----------")
                    print("   ( )    ")
                    print("  - | -    ")
                    print("   /       ")

                case 4:
                    print("----------")
                    print("   ( )    ")
                    print("  - | -    ")
                    print("           ")

                case 5:
                    print("----------")
                    print("   ( )    ")
                    print("    |      ")
                    print("           ")

                case 6:
                    print("----------")
                    print("   ( )    ")
                    print("           ")
                    print("           ")

        if user_guess in hidden_guess and user_guess in user_correct_guess:
                    print(f"""
You've already guessed {user_guess.upper()}!
{"".join(user_correct_guess)}
You have {attempts_left} lives remaining.
                    """)

        if user_guess in hidden_guess and user_guess not in user_correct_guess:
            for i in range(len(hidden_guess)):
                guess_char = hidden_guess[i]
                if guess_char == user_guess:
                    user_correct_guess[i] = user_guess

            print(f"""
Good choice! Let's see if {user_guess.upper()} is in the word...
{"".join(user_correct_guess)}
{user_guess.upper()} appears in the word!
You have {attempts_left} lives remaining.
            """)
            print("===================\n===================")


# Start Game
hangman()