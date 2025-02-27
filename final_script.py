from game_package.rps import get_user_choice, get_computer_choice, determine_rps_winner
from game_package.games import get_user_greeting, amend_scores, replay, return_results
from game_package.menu import display_menu, create_banner, choose_game, add_border

#   Opening Title To The Game via create_banner() function:
#   setting the title colour to bright cyan, which is 96 (check games_package.menu module for list of ANSI escape codes for different colours)
title = create_banner("welcome to get into tech games 2025! choose below to play a game!", 96)
print(title)

#   Display The Game Menu:
#   can adjust the title name and list of games to the developer's liking, e.g.:
# games_list = ["snakes & ladders", "pacman", "chess", "monopoly"]
# print(display_menu("main menu", games_list))
menu = display_menu("game menu", ["solitaire", "rock, paper, scissors", "tic-tac-toe"])
print(menu)

#   Select A Game From The Menu Options:
choose_game()
# unfortunately, this function is not flexible: although you can adjust the game names on the display_menu() function, it doesn't change the names or options on this function.
# improvement: to instead create a dictionary or list with keys (numbers) and values (strings) that can be changed.
# limitation: cannot add more loops.

#   Adding Border/Banner: to show each section of the game.
print(add_border("Game Two", 90))
rps_banner = create_banner("rock, paper, scissors!", 96)
print(f"{rps_banner}\n")

#   Introductory greeting for the rock, paper, scissors game.
user_greeting = get_user_greeting("Rock, Paper, Scissors")
print(user_greeting)

#   Begin Rock Paper Scissors Game
scores = {"Your score": 0, "Computer score": 0}
end = None

while end != "\033[92m\u2551 Thank you for playing...\033[0m":
    # function get user choice retrieves Rock Paper or Scissors,
    human_rps = get_user_choice()
    print(f"\nYou chose: \033[94m{human_rps}\033[0m")
    computer_rps = get_computer_choice()
    print(f"The computer chose: \033[94m{computer_rps}\033[0m\n")
    result = determine_rps_winner(human_rps, computer_rps)
    amend_scores(result, scores)
    print(return_results(result, scores))
    end = replay()
    print(end)

print(add_border("End", 90))

