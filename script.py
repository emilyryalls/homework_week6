# The script of the Rock, Paper and Scissors game uses the game_package.
# It calls the functions from the two modules in the game_package
# The game_package.rps module stores the game specific, which could be used for similar games as Rock, Paper and Scissors
# # which involves 3 options
# which include getting the user input, getting randomly generated computer input and determining
# the winner on the basis of the selected inputs

# The game_package.games module stores the general functions which can be replicated from other games or projects
# the functions called from this module are: greeting the user, amending score as per the user and computer input,
# and returning results as well the function the replay or end the game

from game_package.rps import get_user_choice, get_computer_choice, determine_rps_winner
from game_package.games import get_user_greeting, amend_scores, replay, return_results

scores = {"Your score": 0, "Computer score": 0}
end = None
name = None

user_greeting = get_user_greeting(name, 'Rock, Paper, Scissors')
print(user_greeting)
while end != "Thank you for playing":
    # function get user choice retrieves Rock Paper or Scissors,
    human_rps = get_user_choice()
    print(human_rps)
    computer_rps = get_computer_choice()
    print(computer_rps)
    result = determine_rps_winner(human_rps, computer_rps)
    amend_scores(result, scores)
    print(return_results(result, scores))
    end = replay()
    print(end)