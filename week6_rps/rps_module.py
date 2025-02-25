# from struct import pack_into
#
# from game_package.games import get_user_greeting, amend_scores, return_results, replay
# from game_package.rps import get_user_choice, get_computer_choice, determine_rps_winner
#
# #   Messages
# def user_greeting(name, game_name):
#     """
#     This function takes the player's name and combines it with a predetermined welcome message to introduce the game.
#     This function also adds the game name which the user has chosen based on the integer between 1-3.
#     :param name: str
#     :param game_name: int
#     :return: str
#     """
#     name = input("Please Enter Your Name: ")
#     message = f"Hi {name}!Welcome to Get into Tech Games 2025!\nLet's play a game of {game_name}!\nWill you be able to beat me?\nLet's find out!"
#     return name + message
#
#
#
# #   Menu Page
# def play_solitaire():
#     message = "\033[91mThank you for visiting this page.\nThis game is currently under development.\nPlease return to the main menu.\033[0m\n"
#     return message
#
# def play_rps():
#     scores = {"Your score": 0, "Computer score": 0}
#     end = None
#     name = None
#
#     user_greeting = get_user_greeting('Rock, Paper, Scissors')
#     print(user_greeting)
#     while end != "Thank you for playing":
#         # function get user choice retrieves Rock Paper or Scissors,
#         human_rps = get_user_choice()
#         print(human_rps)
#         computer_rps = get_computer_choice()
#         print(computer_rps)
#         result = determine_rps_winner(human_rps, computer_rps)
#         amend_scores(result, scores)
#         print(return_results(result, scores))
#         end = replay()
#         print(end)
#
# def return_to_menu():
#     return "\033[92mReturning to main menu...\033[0m"
#
# def play_tictactoe():
#     message = "\033[91mThank you for visiting this page.\nThis game is currently under development.\nPlease return to the main menu.\033[0m\n"
#     return message
#
# def display_menu():
#     banner = """
#     \033[97m=== Game Menu ===
#     1. Solitaire (Press S)
#     2. Rock Paper Scissors (Press R)
#     3. Tic-Tac-Toe (Press T)
#     4. Exit (Press Q)\033[0m
#     """  # Explicitly set menu text to white
#     return banner
#
# def choose_game():
#     while True:
#         print(display_menu_2())
#         choice = input("\033[97mEnter your choice (S/R/T/Q): ").upper()  # Keep input white
#
#         if choice == 'S':
#             print(play_solitaire())  # Show message (red), then reset color
#         elif choice == 'R':
#             print(play_rps())
#         elif choice == 'T':
#             print(play_tictactoe())
#         elif choice == 'Q':
#             print("\033[92mThank you for visiting! Goodbye!\033[0m")
#             break
#         else:
#             print("\n\033[91mInvalid input! Try again.\033[0m\n")  # Reset after error message
#
#
# # def create_banner(game):
# #     banner = ' ' * 6 + '\u2554' + '\u2550'*59 + '\u2557\n'
# #     banner += f"\u2551" + " " * 2 + "  ".join([f"\u2666" for _ in range(4)]) + "    " + " ".join(f"LET'S PLAY {game}".upper()) + "    " + "  ".join([f"\u2666" for _ in range(4)]) + " " * 2 + "\u2551\n"
# #     banner += ' ' * 6 + '\u255a' + '\u2550'*59 + '\u255D'
# #     return banner
#
#
# def create_banner(game):
#     text = f"LET'S PLAY {game}".upper()
#     text_length = len(text)
#     line_length = 20 + text_length  # Calculate horizontal line length
#
#     top_line = ' ' * 6 + '\u2554' + '\u2550' * line_length + '\u2557\n'
#     middle_line = (
#             "\u2551"
#             + "  "  # Left spacing
#             + "  ".join("\u2605" for _ in range(4))  # Left diamonds
#             + "    "  # Left padding
#             + text  # Game text
#             + "    "  # Right padding
#             + "  ".join("\u2605" for _ in range(4))  # Right diamonds
#             + "  "  # Right spacing
#             + "\u2551\n"
#     )
#     bottom_line = ' ' * 6 + '\u255a' + '\u2550' * line_length + '\u255d'
#
#     return top_line + middle_line + bottom_line
#
#
# import pyfiglet
#
# def display_menu_2():
#     # Use pyfiglet to create a banner for "Game Menu" with the "block" font
#     title = pyfiglet.figlet_format("Game Menu", font="big")
#
#     # The rest of the menu will be plain text
#     menu_text = f"""
#     1. Solitaire (Press S)
#     2. Rock Paper Scissors (Press R)
#     3. Tic-Tac-Toe (Press T)
#     4. Exit (Press Q)
#     """
#
#     return f"\033[97m{title}\033[0m{menu_text}"
#
#
#
# #   Test
#
# def main():
#     print(create_banner("solitaire"))
#     print(create_banner("rock,paper,scissors"))
#     print(create_banner("tic-tac-toe"))
#     print(display_menu_2())
#     print(choose_game())
#
# if __name__ == "__main__":
#     main()