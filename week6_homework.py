import random

choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

def get_user_choice():
    # CHANGE TO NEW INPUT
    player_choice = input('Please choose Rock (R), Paper (P), or Scissors (S): ').upper()

    while player_choice not in choices:
        # ALSO CHANGE
        player_choice = input('Invalid choice! Please enter R, P, or S: ').upper()

    return player_choice


def get_computer_choice():
    choices = ['R', 'P', 'S']
    return random.choice(choices)


def determine_winner(player_choice, computer_choice):
    # choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}

    if player_choice == computer_choice:
        return "It's a tie!"

    elif (player_choice == 'P' and computer_choice == 'R') or \
            (player_choice == 'S' and computer_choice == 'P') or \
            (player_choice == 'R' and computer_choice == 'S'):
        return f"You win! {choices[player_choice]} beats {choices[computer_choice]}!"

    else:
        return f"You lose! {choices[computer_choice]} beats {choices[player_choice]}!"


# game variables
player_choice = get_user_choice()
computer_choice = get_computer_choice()
result = determine_winner(player_choice, computer_choice)

print(f'You chose: {player_choice} ({choices[player_choice]})')
print(f'The computer chose: {computer_choice} ({choices[computer_choice]})')
print(result)
