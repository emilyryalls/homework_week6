import pyfiglet
from setuptools.command.egg_info import manifest_maker


#   Create a banner for title texts.
#   Banner dynamically adjusts based on the length of the text input.
#   Text color can be changed by inputting an integer via ANSI escape code format.
def create_banner(message: str, textcolor: int) -> str:
    """
    This function generates and formats a custom decorative banner, enclosed by a box-line border.\n
    The banner size adjusts based on the length of the input message.
    The color of the text can be changed by inputting ANSI escape code number.
    :param message: str
    :param textcolor: int
    :return: str
    """
    text = message.title()
    line_length = 20 + len(text)

    top = " " * 6 + "\u2554" + "\u2550" * line_length + "\u2557\n"
    middle = (
            "\u2551" + "  "
            + "  ".join("\u2605" * 4)
    # "  ".join(...) is used to join two spaces between each star i.e. "★  ★  ★  ★"
            + "    "
            + f"\033[1;{textcolor}m{text}\033[0m"
    # Here the textcolor parameter is embedded between \033[1;...m] because the standard format for changing the colour of output text
    # in ANSI escape code is \033[{integer}m (see list of escape codes below). The "1;" makes the text bold.
    # So for example, if I wanted the text to be blue (94) and bold (1) then I would write \033[1;94m.
    #   The ";" is used to separate the integer for text style (1) from text colour (94).
    # I added a parameter 'textcolor' instead of setting a predetermined colour so that the developer can choose which colour they want the text to be.
    # On the script, all they'd need to do is add a string , integer e.g.: print(create_banner("Hello", 94))
            + "    "
            + "  ".join("\u2605" * 4)
            + "  "
            + "\u2551\n"
    )
    bottom = " " * 6 + "\u255a" + "\u2550" * line_length + "\u255d"

    # Positioning the banner at the center:
    #   100 here is what I have set the width to be.
    # width minus the length of the top line divided by 2.
    # multiply one space " " by that length and add that onto each banner layer (top, middle bottom).
    padding = (100 - len(top)) // 2
    centered_banner = " "* padding + top
    centered_banner += " "* padding + middle
    centered_banner += " " * padding + bottom
    return centered_banner


#   Add a border to separate sections of the game.
#   Color of border decorations can be changed by inputting an integer via ANSI escape code format.
def add_border(txt: str, bordercolor: int) -> str:
    """
    This function adds a custom border with text that adjusts based on the length of the text inputted by the user.
    The text color can be modified by inputting an integer via ANSI escape code format.
    :param txt: str
    :param bordercolor: int
    :return: str
    """
    top = f"\033[{bordercolor}m" + "\u2605" * 103 + "\033[0m\n"
    middle = " " * ((103 - len(txt)) // 2) + txt + "\n"
    bottom = f"\033[{bordercolor}m" + "\u2605" * 103 + "\033[0m\n"
    return top + middle + bottom


#   Displays a game-style menu with a built-in title and list.
#   User can input a list stored in a variable or string list to 'games' parameter to add as many game options as they want.
def display_menu(title: str, games: list):
    """
    This function generates and formats a custom game-style menu displaying a title and an indexed list of game names.
    The user can input a string list to 'games' parameter to input the game options they want.
    :param title: str
    :param games: list
    :return: None
    """
    menu_title = pyfiglet.figlet_format(title, font="alligator", width=150)
    # Uses the pyfiglet module to create a stylised ASCII art title.
    # title is added as a parameter so that developers can decide what to put as the title.
    border = "\n" + "\u2605" * 103 + "\n"
    game_names = ""
    for index, name in enumerate(games, start =1):
        game_names += f"\n\u2551\033[1;97m{index: 10d} \u2605 {name.title()}\033[0m\n"
    return border + menu_title + border + game_names + border


#   Play function to take us to Solitaire.
#   Is incorporated in the menu and can be used within a loop to access the game.
#   For now, only returns a predetermined message as game is not developed.
def play_solitaire():
    """
    This function calls a game of Solitaire.\n
    The display is a predetermined message to inform the user of current game development.
    :return: str
    """
    banner = create_banner("welcome to solitaire", 96)
    message = "\n\n\u2551\033[91m Thank you for choosing Solitaire.\n\033[0m\u2551 \033[91mUnfortunately this game is currently under development.\n\033[0m\u2551 \033[91mPlease choose another option.\033[0m\n"
    return banner + message


#   Play function to take us to Tic-Tac-Toe.
#   Is incorporated in the menu and can be used within a loop to access the game.
#   For now, only returns a predetermined message as game is not developed.
def play_tictactoe():
    """
    This function calls a game of Tic=Tac-Toe.\n
    The display is a predetermined message to inform the user of current game development.
    :return: str
    """
    banner = create_banner("welcome to tic-tac-toe", 96)
    message = "\n\n\u2551\033[91m Thank you for choosing Tic-Tac-Toe.\n\033[0m\u2551 \033[91mUnfortunately this game is currently under development.\n\033[0m\u2551 \033[91mPlease choose another option.\033[0m\n"
    return banner + message


# Function to select a game based on the integer the user inputs.
def choose_game():
    """
    This function displays a game menu and prompts the user to select a game to play based on the displayed list.
    The options are:\n
    "1" for Game 1\n
    "2" for Game 2\n
    "3" for Game 3\n
    "Q" for Quit to exit the game.\n
    The function continues until a valid input is entered or the user quits.
    :return: ???
    """
    while True:
        choice = input("\033[97mEnter your choice to play a game from the options above (1/2/3): \033[0m").upper()
        # Asks the user to input a choice between game 1-3 from the menu page

        if choice == '1':
        # If they chose Solitaire.
            print(add_border("Game One", 90))
            print(play_solitaire())
        elif choice == '2':
        # If they chose RPS, then break out of the loop and run what's on the final_script.
            break
        elif choice == '3':
        # If they chose Tic-tac-toe.
            print(add_border("Game Three", 90))
            print(play_tictactoe())
        else:
            print("\n\033[91mInvalid input! Try again.\033[0m\n")

"""
* the following are just comments:

    ANSI Escape Code:
    
        \u2605                  star
        \033[{colour}m          standard format
        colour:
            90                  bright black (gray)
            91                  bright red
            92                  bright green
            93                  bright yellow
            94                  bright blue
            95                  bright magenta
            96                  bright cyan
            97                  bright white
        
        \033[{text style}m      standard format
        text style:
            0                   reset all styles (including colours)
            1                   bold
            2                   faint text
            4                   underline
            9                   strikethrough
        
        \u2554                  ╔
        \u2550                  ═
        \u2551                  ║
        \u2557                  ╗
        \u255a                  ╚
        \u255d                  ╝

"""

def main():
    print(display_menu("game menu", ["solitaire", "rock paper scissors", "tic-tac-toe"]))


if __name__ == "__main__":
    main()