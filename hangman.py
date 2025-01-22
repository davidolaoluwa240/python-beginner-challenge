# Challenge
# Create a word guessing game

# Import modules
import os
import platform
import time
from random import choice

'''
    Function to clear terminal
'''
def clear_terminal():
    if platform.system() == "Windows": os.system("cls")
    else: os.system("clear")

'''
    Function to get random hidden word
'''
def get_hidden_word():
    # Get words from file
    with open("hangman_words.txt", "r") as file:
        return choice(file.read().split())

'''
    Function to print message to the screen
'''
def print_msg(msg):
    # Pause for 1 seconds
    time.sleep(2)

    # Clear terminal
    clear_terminal()

    print("======================================")
    print(msg)
    print("======================================")



'''
    Function to handle user guess not in hidden guess
'''
def handle_user_guess_fail(user_guess, user_correct_guess_str, attempts_left):
    print_msg(f"{user_correct_guess_str.upper()}\n\n{user_guess.upper()} do not appears in the word!\nYou have {attempts_left} lives remaining.")

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

'''
    Function to handle user guess in hidden guess
'''
def handle_user_guess_correct(hidden_guess, user_guess, user_correct_guess):
    for i in range(len(hidden_guess)):
        guess_char = hidden_guess[i]
        if guess_char == user_guess:
            user_correct_guess[i] = user_guess

'''
    Function for the hangman game
'''
def hangman():
    # States
    hidden_guess = get_hidden_word()
    hidden_guess_length = len(hidden_guess)
    user_correct_guess = ["_"] * hidden_guess_length
    user_correct_guess_str = "".join(user_correct_guess)
    attempts_left = 7

    print_msg(f"Welcome Guest\nYou have {attempts_left} lives.")

    while attempts_left != 0 and user_correct_guess_str != hidden_guess:
        print_msg(f"Here's the word:\n\n{user_correct_guess_str.upper()} ({hidden_guess_length} letters)")

        # Get user guess
        user_guess = input("\nEnter the character you think the word may have: ").lower()

        # Validate user input
        if len(user_guess) > 1:
            print_msg("Error💥💥: You can only enter a single letter")
            continue

        # Check if user_guess is not in hidden guess
        if user_guess not in hidden_guess:
            # Decrement number of attempt
            attempts_left -= 1

            # Handle user guess fail
            handle_user_guess_fail(user_guess, user_correct_guess_str, attempts_left)

        # Check if user_guess is in hidden guess and if user_guess already exist in the user_correct_guess
        if user_guess in hidden_guess and user_guess in user_correct_guess:
            print_msg(f"You've already guessed {user_guess.upper()}!\n\n{user_correct_guess_str.upper()}")

        # Check if user_guess is in hidden guess and if user_guess does not exist in the user_correct_guess
        if user_guess in hidden_guess and user_guess not in user_correct_guess:
            # Handle user guess correct
            handle_user_guess_correct(hidden_guess, user_guess, user_correct_guess)

            # Update user_correct_guess_str
            user_correct_guess_str = "".join(user_correct_guess)

            print_msg(f"{user_correct_guess_str.upper()}\n\n{user_guess.upper()} appears in the word!")
    else:
        # Check if user guessed the hidden word
        if user_correct_guess_str == hidden_guess:
            print_msg(f"YOU WON 🔥🔥: ({hidden_guess})")

        # Check if user could not guessed the hidden word
        if attempts_left == 0:
            print_msg(f"YOU LOSE 😢: ({hidden_guess}) is the hidden word")

# Start Game
hangman()