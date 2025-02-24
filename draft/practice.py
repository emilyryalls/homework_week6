# def print_info(**info):
# 	for key, value in info.items():
# 		print(f"{key}: {value}")
#
# print_info(name="Alice", age=30, city="New York")


# def display_menu(*args):
#     return "=== Game Menu ==="
#
#     # Loop through each argument and display it as a menu option
#     for index, options in enumerate(args, 1):
#         return f"{index}. {game}"
#
#     return input("\nPlease select a game by entering the corresponding number (1-3):")
#
#
# # Call the function with a list of game options
# def main():
#     choose = display_menu("Solitaire", "Rock Paper Scissors", "Tic-Tac-Toe")
#     print(choose)
# main()


# def display_menu(*args):
#     # Display the banner
#     return "=== Game Menu ==="
#
#     # Loop through each argument and display it as a menu option
#     for index, game in enumerate(args, 1):
#         return f"{index}. {game}"
#
#     print("\nPlease select a game by entering the corresponding number (1-3):")
#
#
# # Call the function with a list of game options
# display_menu("Solitaire", "Rock Paper Scissors", "Tic-Tac-Toe")

def user_greeting(name, game_name):
    """
    Creates a personalized welcome message with the user's name and chosen game.
    :param name: str - player's name
    :param game_name: str - name of the selected game
    :return: str - formatted greeting message
    """
    greeting = f"Hi {name}!"
    message = f"Welcome to Get into Tech Games 2025!\nLet's play a game of {game_name}!\nWill you be able to beat me?\nLet's find out!"
    return f"{greeting}\n{message}"


def play_solitaire():
    """Returns maintenance message for Solitaire"""
    return "Thank you for visiting this page.\nThis game is currently under development.\nPlease return to the main menu.\n"


def play_rps():
    """Returns maintenance message for Rock Paper Scissors"""
    return "Thank you for visiting this page.\nThis game is currently under development.\nPlease return to the main menu.\n"


def play_tictactoe():
    """Returns maintenance message for Tic-Tac-Toe"""
    return "Thank you for visiting this page.\nThis game is currently under development.\nPlease return to the main menu.\n"


def display_menu():
    """Displays game menu and returns valid user choice"""
    while True:
        print("""
=== Game Menu ===
1. Solitaire
2. Rock Paper Scissors
3. Tic-Tac-Toe
""")
        choice = input("Enter the number 1, 2, or 3 to choose the game: ")
        if choice in {'1', '2', '3'}:
            return choice
        print("\nInvalid choice! Please enter a number between 1-3.\n")


def get_game_name(choice):
    """Maps menu choice to game name"""
    return {
        '1': 'Solitaire',
        '2': 'Rock Paper Scissors',
        '3': 'Tic-Tac-Toe'
    }[choice]


def execute_game(choice):
    """Executes the selected game based on menu choice"""
    return {
        '1': play_solitaire,
        '2': play_rps,
        '3': play_tictactoe
    }[choice]()


def main():
    """Main game flow controller"""
    name = input("Please Enter Your Name: ").strip()
    game_choice = display_menu()
    game_name = get_game_name(game_choice)

    print(user_greeting(name, game_name))
    print(execute_game(game_choice))


if __name__ == "__main__":
    main()