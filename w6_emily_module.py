from random import randint

def convert_user_input(user_input):
    """
        This function converts the user input into Rock, Paper or Scissors\n
        If the input is not formatted correctly they will be prompted to try again
        :param user_input: str
        :return: str
        """
    while user_input != 'QUIT':
        user_input = input("Input R, P or S, or type QUIT to exit game:").upper()
        if user_input == "QUIT":
            return 'QUIT'
        elif user_input == 'R':
            return 'Rock'
        elif user_input == 'P':
            return 'Paper'
        elif user_input == 'S':
            return 'Scissors'
        else:
            print('Please try again. Make sure there are no spaces.')


def return_computer_move():
    """
    This function generates the computers random move in Rock, Paper, Scissors\n
    :return: str
    """
    computer_move = ['Rock', 'Paper', 'Scissors']
    random_number = randint(0, 2)
    return str(computer_move[random_number])

def determine_rps_winner(human_rps, computer_rps):
    """
    This function compares the human and computer moves in Rock, Paper, Scissors,
    and returns if the human won, lost or drew with the computer.
    :param computer_rps: str
    :param computer_rps: str
    :return: str
    """
    if human_rps == computer_rps:
        return "It's a draw"
    elif human_rps == 'Rock' and computer_rps == 'Paper':
            return 'Computer wins'
    elif human_rps == 'Paper' and computer_rps == 'Scissors':
            return 'Computer wins'
    elif human_rps == 'Scissors' and computer_rps == 'Rock':
            return 'Computer wins'
    else:
        return 'You win!'

def amend_scores(result, scores):
    """
    This function amends scores that are stored in a dictionary, based on the result of a game
    :param result: str
    :param scores: dict
    :return: dict
    """
    if result == "It's a draw":
        return scores
    elif result == "Computer wins":
        scores["Computer score"] += 1
    else:
        scores["Your score"] += 1
    return scores



def return_results(result, scores):
    string = ""
    for k, v in scores.items():
        string = f"{string}{k:<18s} {str(v):<5s}\n"
    return (f"Result: {result}\n{string}")


def main():
    scores = {'Your score': 2, 'Computer score': 1}
    result = 'Computer wins!'
    amend_scores(result, scores)
    print(scores)
    result = 'You Win'
    scores = {'Your score:': 2, 'Computer score:': 1}
    print(return_results(result, scores))


if __name__ == '__main__':
    main()

#
# def return_results(result, scores):
#     string = ""
#     for k, v in scores.items():
#         print(f" {k}\n {v}")
#     return string

    # print(f"{index:<5d} {country_name:<15s} {countries[country_name]:<15,}")

# string = ""
# string = {string} + Your Score: + 1
# string = {Your Score + 1} + Compute Score: + 2

    # return f"Result: {result}\n Your score: {v}\n Computer score: {v} "