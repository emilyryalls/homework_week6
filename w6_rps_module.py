#   Greeting and Layout Function

#   Menu Page
def play_solitaire():
    message = (
        "\033[91mThank you for visiting this page.\n"
        "\033[91mThis game is currently under development.\n"
        "\033[91mPlease return to the main menu.\033[0m\n"  # Reset color at the end
    )
    return message

def play_rps():
    message = (
        "\033[91mThank you for visiting this page.\n"
        "\033[91mThis game is currently under development.\n"
        "\033[91mPlease return to the main menu.\033[0m\n"
    )
    return message

def play_tictactoe():
    message = (
        "\033[91mThank you for visiting this page.\n"
        "\033[91mThis game is currently under development.\n"
        "\033[91mPlease return to the main menu.\033[0m\n"
    )
    return message

def display_menu():
    banner = """
    \033[97m=== Game Menu ===
    1. Solitaire (Press S)
    2. Rock Paper Scissors (Press R)
    3. Tic-Tac-Toe (Press T)
    4. Exit (Press Q)\033[0m
    """  # Explicitly set menu text to white
    return banner

def choose_game():
    while True:
        print(display_menu())  # Display the menu in white
        choice = input("\033[97mEnter your choice (S/R/T/Q): ").upper()  # Keep input white

        if choice == 'S':
            print(play_solitaire())  # Show message (red), then reset color
        elif choice == 'R':
            print(play_rps())
        elif choice == 'T':
            print(play_tictactoe())
        elif choice == 'Q':
            print("\033[92mThank you for visiting! Goodbye!\033[0m")
            break
        else:
            print("\n\033[91mInvalid input! Try again.\033[0m\n")  # Reset after error message


#   Messages
def user_greeting(name, game_name):
    """
    This function takes the player's name and combines it with a predetermined welcome message to introduce the game.
    This function also adds the game name which the user has chosen based on the integer between 1-3.
    :param name: str
    :param game_name: int
    :return: str
    """
    name = input("Please Enter Your Name: ")
    message = f"Hi {name}!Welcome to Get into Tech Games 2025!\nLet's play a game of {game_name}!\nWill you be able to beat me?\nLet's find out!"
    return name + message

def solitaire_banner():
    banner = f"""
          ╔═════════════════════════════════════╗
    ║  ♠  ♥  ♦  ♣    S O L I T A I R E    ♣  ♦  ♥  ♠  ║
          ╚═════════════════════════════════════╝
    """
    return banner


def solitaire_banner_2():
    banner = "\u2554"+"\u2550"*37+"\u2557"
    return banner

print(solitaire_banner_2())


# Start the game menu
def main():
    # display_menu()
    # choose_game()
    # greeting = user_greeting()
    # print(greeting)
    print(solitaire_banner())


main()

# if __name__ == "__main__":
#     display_menu()

border = "\u250C\u2500\u2510\n\u2514\u2500\u2518"
print(border)