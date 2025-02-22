# importing random module to generate computer choice
import random


def get_user_choice():
    # global choices, player_choice
    # using a dictionary for RPS to associate the letter to the word
    choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    # starting the game
    # this variable will prompt the user to enter their choice
    player_choice = input('Please choose Rock (R), Paper (P) or Scissors (S): ')
    # This will prompt the user to enter their choice again if wrong
    while player_choice not in choices:
        player_choice = input('Please enter R, P or S: ')
    return player_choice
    computer_choice = random.choice(list(choices.keys()))


# this will be how the computer generates its choice
# this variable is using .choice() method to select a choice from the dictionary
# the dictionary needed to be converted to a list
choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
computer_choice = random.choice(list(choices.keys()))
# IF USING A NUMBER .randint() range between 0-2
# variables for the numbers i.e r = 0

# FUNCTION
def determine_winner(player_choice, computer_choice):
    choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    computer_choice = random.choice(list(choices.keys()))
    # different playing scenarios:
    if player_choice == computer_choice:
        return "You have tied with the Computer!"

    elif player_choice == 'P':
        if computer_choice == 'S':
            return "You lose! Scissors cut Paper!"
        else:
            return "You win! Paper wraps Rock!"

    elif player_choice == 'S':
        if computer_choice == 'R':
            return "You lose! Rock smashes Scissors!"

    elif player_choice == 'R':
        if computer_choice == 'S':
            return "You win! Rock smashes Scissors!"
        else:
            return "You lose! Scissors cut Paper."


player_choice = get_user_choice()
result = determine_winner(player_choice, computer_choice)
print(f'You chose: {player_choice}')
print(f'The computer chose: {computer_choice}')
print(result)
