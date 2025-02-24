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