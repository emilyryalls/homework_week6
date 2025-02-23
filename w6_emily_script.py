from w6_emily_module import convert_user_input, return_computer_move, determine_rps_winner, amend_scores, return_results

# human_move = "Rock"
# computer_move = "Scissors"
scores = {'Your score': 0, 'Computer score': 0}
user_input = None

while user_input != 'QUIT':
    human_move = (convert_user_input(user_input))
    print(human_move)
    if human_move == 'QUIT':
        break
    else:
        computer_move = (return_computer_move())
        print(computer_move)
        result = determine_rps_winner(human_move, computer_move)
        scores = amend_scores(result, scores)
        final_result = return_results(result, scores)
        print(final_result)




