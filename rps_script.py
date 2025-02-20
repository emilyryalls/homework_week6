from rps_module import user_greeting, get_user_choice, get_computer_choice, determine_winner, play_again

print('='*20, "🪨📃✂️ Get into Tech Games 2025: Rock Paper Scissors ✂️📃🪨", '='*20)
name = input("Enter your name to begin the game: ")
greeting = user_greeting(name, message='')
print(greeting)

while True:
    user_choice = get_user_choice()
# Retrieves user's choice via prompt, which returns a string.
    computer_choice = get_computer_choice()
# Retrieves computer's choice via randomisation between integers 0-2.

# Using a dictionary, we can map the user input and computer input to their full names.
    choice_names = {
        'R': 'Rock', 'P': 'Paper', 'S': 'Scissors',
        0: 'Rock', 1: 'Paper', 2: 'Scissors'
    }
# User input if they chose Rock (R): choice_names[user_choice] → choice_names['R'] → 'Rock'
# Computer input if they chose Rock (0):choice_names[computer_choice] → choice_names[0] → 'Rock'
    print(f"\nYou chose: {choice_names[user_choice]}\nComputer chose: {choice_names[computer_choice]}")

# Determining and displaying result following the choice that each player made.
    outcome = determine_winner(user_choice, computer_choice)

    if outcome == 'draw':
        print("It's a draw!")
    elif outcome == 'win':
        print("Congratulations! You won!")
    else:
        print("Oops! You lost. Better luck next time!")

    if not play_again():
        print("\nThanks for playing! Goodbye!")
        break  # Exit the loop


# name = input("Enter your name to begin the game: ")
# greeting = user_greeting(name)
# print(greeting)
# introduction_message("Welcome to Get into Tech Games 2025!", "Let's play a game of Rock... Paper... Scissors!", "Will you be able to beat me?", "Let's find out!")
