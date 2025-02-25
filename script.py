from game_package.rps import get_user_choice, get_computer_choice, determine_rps_winner
from game_package.games import get_user_greeting, amend_scores, replay, return_results

scores = {"Your score": 0, "Computer score": 0}
end = None

user_greeting = get_user_greeting("Rock, Paper, Scissors")
print(user_greeting)
while end != "\033[92m\u2551 Thank you for playing...\n\u2551 Returning back to game menu...\033[0m":
    # function get user choice retrieves Rock Paper or Scissors,
    human_rps = get_user_choice()
    print(f"\nYou chose: \033[96m{human_rps}\033[96m")
    computer_rps = get_computer_choice()
    print(f"The computer chose: \033[96m{computer_rps}\033[0m\n")
    result = determine_rps_winner(human_rps, computer_rps)
    amend_scores(result, scores)
    print(return_results(result, scores))
    end = replay()
    print(end)

