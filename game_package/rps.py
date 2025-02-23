import random

def get_user_choice():
    # CHANGE TO NEW INPUT
    choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    player_choice = input('Please choose Rock (R), Paper (P), or Scissors (S): ').upper()
    while player_choice not in choices:
        # ALSO CHANGE
        player_choice = input('Invalid choice! Please enter R, P, or S: ').upper()
    return choices[player_choice]

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

def determine_rps_winner(human_rps, computer_rps):
    """
    This function compares the human and computer moves in Rock, Paper, Scissors,
    and returns if the human won, lost or drew with the computer.
    :param computer_rps: str
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