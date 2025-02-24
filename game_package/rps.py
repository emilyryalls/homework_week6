import random


# the function get_user_choice get user input and stores it as a dictionary with key of "R/P/S" with
# assigned values of rock, paper and scissors respectively
def get_user_choice():
    """
    This function returns the user choice from the options provided by choosing teh first alphabet of the option.
    The while loop prompts the user to pick one of the option which is mentioned in the preset message.
    :return: dictionary
    """
    choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    player_choice = input('Please choose Rock (R), Paper (P), or Scissors (S): ').upper()
    while player_choice not in choices:
        player_choice = input('Invalid choice! Please enter R, P, or S: ').upper()
    return choices[player_choice]


# The function get_computer_choice captures computer input as a dictionary which is decided randomly
# between number 0-2 and taken but the index position corresponding to that number
def get_computer_choice():
    """
    This function generates the computers random move in Rock, Paper, Scissors\n
    :return: str
    """
    computer_move = {0:'Rock', 1:'Paper', 2:'Scissors'}
    random_number = random.randint(0, 2)
    return str(computer_move[random_number])

# def get_computer_choice():
#     choices = ['Rock', 'Paper', 'Scissors']
#     return random.choice(choices)


# This function compares the user and computer
def determine_rps_winner(human_rps, computer_rps):
    """
    This function compares the human and computer moves in Rock, Paper, Scissors,
    and returns if the human won, lost or drew with the computer.
    :param human_rps: str
    :param computer_rps: str
    :return: str
    """
    if human_rps == computer_rps:
        return "It's a draw"
    elif human_rps == 'Rock' and computer_rps == 'Paper':
            return 'Computer wins'
    elif human_rps == 'Paper' and computer_rps == 'Scissors':
            return 'Computer wins'
    elif human_rps == 'Scissors' and computer_rps == 'Rock':
            return 'Computer wins'
    else:
        return 'You win!'


def main():
    print(get_computer_choice())
    print(get_user_choice())

if __name__ == '__main__':
    main()