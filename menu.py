import pyfiglet
from game_package.rps import get_user_choice, get_computer_choice, determine_rps_winner
from game_package.games import get_user_greeting, amend_scores, replay, return_results


def create_banner(message):
    """
    This function generates and formats a custom decorative banner, given a string message.
    :param message: str
    :return: banner
    """
    text = message.title()
    line_length = 20 + len(text)  # Calculate horizontal line length

    top_line = " " * 6 + '\u2554' + '\u2550' * line_length + '\u2557\n'
    middle_line = ("\u2551" + "  " + "  ".join("\u2605"*4) + "    " + text + "    " + "  ".join("\u2605"*4) + "  " + "\u2551\n")
    bottom_line = ' ' * 6 + '\u255a' + '\u2550' * line_length + '\u255d'

    return top_line + middle_line + bottom_line


def display_menu(title, games):
    """
    This function generates and formats a custom game-style menu displaying a title and an indexed list of game names.
    :param title: str
    :param games: list (string)
    :return: list
    """
    menu_title = pyfiglet.figlet_format(title, font="alligator", width=103)
    border = "\n" + "\u2605" * 103 + "\n"
    game_names = ""
    for index, name in enumerate(games, start =1):
        game_names += f"\n\u2551\033[1;97m{index: 10d} \u2605 {name.title()}\033[0m\n"
    return border + menu_title + border + game_names + border


def play_solitaire():
    """
    Function to call a game of Solitaire.
    :return: str
    """
    banner = create_banner("welcome to solitaire")
    message = "\n\n\u2551\033[91m Thank you for choosing Solitaire.\n\033[0m\u2551 \033[91mUnfortunately this game is currently under development.\n\033[0m\u2551 \033[91mAutomatically returning you back to the game menu.\033[0m\n"
    return banner + message


def play_rps():
    """
    Function to call a game of Rock, Paper, Scissors.
    :return: str
    """
    scores = {"Your score": 0, "Computer score": 0}
    end = None

    user_greeting = get_user_greeting("Rock, Paper, Scissors")
    print(user_greeting)
    while end != "\033[92m\u2551 Thank you for playing...\n\u2551 Returning back to game menu...\033[0m":
        # function get user choice retrieves Rock Paper or Scissors,
        human_rps = get_user_choice()
        print(f"\nYou chose: \033[96m{human_rps}\033[0m")
        computer_rps = get_computer_choice()
        print(f"The computer chose: \033[96m{computer_rps}\033[0m\n")
        result = determine_rps_winner(human_rps, computer_rps)
        amend_scores(result, scores)
        print(return_results(result, scores))
        end = replay()
        print(end)


def play_tictactoe():
    """
    Function to call a game of Tic=Tac-Toe.
    :return: str
    """
    banner = create_banner("welcome to tic-tac-toe")
    message = "\n\n\u2551\033[91m Thank you for choosing Tic-Tac-Toe.\n\033[0m\u2551 \033[91mUnfortunately this game is currently under development.\n\033[0m\u2551 \033[91mAutomatically returning you back to the game menu.\033[0m\n"
    return banner + message


def choose_game():
    """
    Function that chooses the game.
    :return: ???
    """
    while True:
        print(display_menu("game menu", ["solitaire", "rock, paper, scissors", "tic-tac-toe"]))
        choice = input("\033[97mEnter your choice (1/2/3 or Q for QUIT): \033[0m").upper()

        if choice == '1':
            print(play_solitaire())
        elif choice == '2':
            print(create_banner("welcome to a game of rock, paper, scissors!"))
            print(play_rps())
        elif choice == '3':
            print(play_tictactoe())
        elif choice == 'Q':
            print("\033[92mThank you for visiting! Goodbye!\033[0m")
            break
        else:
            print("\n\033[91mInvalid input! Try again.\033[0m\n")




def main():
    print(create_banner("welcome to get into tech games 2025! choose a game from the menu below!"))
    print(display_menu("game menu", ["solitaire", "rock paper scissors", "tic-tac-toe", "pacman"]))
    print(create_banner("solitaire"))
    print(create_banner("rock, paper, scissors"))
    print(create_banner("tic-tac-toe"))


if __name__ == "__main__":
    main()

