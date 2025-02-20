#   Rock Paper Scissors

# Objective:
#   1) To practice creating functions
#   2) To revisit conditional structures
#   3) To use built-in functions

# Task A: Create a Game of Rock, Paper Scissors
# Design a program that does the following:
#   > Prompts the user to enter the value: R, P or S
#   > Converts this value into Rock, Paper or Scissors.
#   > Asks the computer to generate a random value between 0 and 2.
#   > Convert the computer's choice: 0 (Rock), 1 (Paper), 2 (Scissors).
#   > Compare the user's choice with the computer's choice to display a message indicating whether the user won, lost or drew vs computer.
#   > Create your own functions + incorporate conditional statements.

# Note: Scissors > Paper, Paper > Rock, Rock > Scissors

import random

#   Create: greeting and game introductory message to the user.
def user_greeting(name, message):
    """
    This function takes the player's name and combines it with a predetermined welcome message to introduce the game.
    :param name: str
    :param message: str
    :return: str
    """
    greeting = f"Hi {name}!"
    message = "Welcome to Get into Tech Games 2025!\nLet's play a game of Rock... Paper... Scissors!\nWill you be able to beat me?\nLet's find out!"
    return f"{greeting}\n{message}"


#   Retrieve: user choice by including a prompt for the user to submit choice (R, P, S)
# Using a while True loop enables the loop to repeat iterations until user inputs the correct values + to restart the game.
def get_user_choice():
    """
    This function prompts the user to input their choice of (case-sensitive) Rock (R), Paper (P) or Scissors (S).
    This function verifies the input until a valid input is provided.
    :return: str
    """
    while True:
        user_input = input("Enter R (Rock), P (Paper), or S (Scissors): ")
        if user_input in ['R', 'P', 'S']:
            return user_input
        return ("Invalid input! Try again.")


#   Retrieve: randomly-generated value between 0-2.
def get_computer_choice():
    """
    This function generates a random choice for the computer, whereby a random integer is selected between 0 and 2:\n
    > 0 : Rock\n
    > 1 : Paper\n
    > 2 : Scissors

    :return: int
    """
    return random.randint(0, 2)

#   User vs Computer: Determining the Winner.
# Via rules of Rock, Paper, Scissors, Scissors > Paper, Paper > Rock, and Rock > Scissors.
# Since we have assigned numerical values to each choice, mathematically, a win is achieved if == 1 or -2
# The modulus arithmetic (% 3) ensures that all the wins are translated into 1, losses are translated into 2.
def determine_winner(user, computer):
    choices = {'R': 0, 'P': 1, 'S': 2}
    user_num = choices[user]

    if user_num == computer:
        return "draw"
    elif (user_num - computer) % 3 == 1:
        return "win"
    else:
        return 'lose'

#   Repeat Game Option
def play_again():
    """
    This function provides a 'Yes' or 'No' (case-sensitive) option for the user to repeat the game.\n
    > Y : Yes\n
    > N : No

    :return: str
    """
    while True:
        repeat = input("\nWould you like to play again? (Y/N): ")
        if repeat == 'Y':
            return True
        elif repeat == 'N':
            return False
        else:
            return ("Invalid input! Please enter Y or N.")


# def user_greeting(name):
#     greeting = f"Hi {name}!"
#
# def introduction_message(*argv):
#     for arg in argv:
#         print(arg)


# Task B: Compare Programs
#   1) Have you achieved this differently?
#   2) Does anyone's solution stand out?
#   3) Would you consider changing the names of your variables or functions?