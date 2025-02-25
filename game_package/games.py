# This is a generalized module which has functions which can be reused for:
# 1. Greeting the user and getting the "name" of the user
# 2. Capturing the result (as draw, user won or computer won) and adding scores for user or computer
# 3. Print the results of scores of user and computer after each round
# 4. Asking the user if the want to replay the game or end the game.

# get_user_greeting function returns "message" as a f-string
def get_user_greeting(game_name):
    """
    This function takes the player's name and combines it with a predetermined welcome message to introduce the game.
    This function also adds the game name which the user has chosen.
    :param game_name: str
    :return: str
    """
    name = input("\u2605 Please Enter Your Name: ").capitalize()
    message = f"\n\u2551 Hi \033[95m{name}\033[0m! Welcome to Get into Tech Games 2025!\n\u2551 Let's play a game of \033[95m{game_name}\033[0m!\n\u2551 Will you be able to beat me?\n\u2551 Let's find out!"
    return message


# function amend_scores returns the scores as per the result, after the user
# input and the computer input is compared
def amend_scores(result, scores):
    """
    This function amends scores that are stored in a dictionary, based on the result of a game
    :param result: str
    :param scores: dict
    :return: dict
    """
    if result == "It's a draw!":
        return scores
    elif result == "\033[93mComputer wins! You lose! Better luck next time\033[0m!":
        scores["Computer score"] += 1
    else:
        scores["Your score"] += 1
    return scores


# The function return_results take two parameters, result=string and scores=dictionary
# and return a string which is key value pairs from the dictionary using the formatted strings
def return_results(result, scores):
    string = ""
    for k, v in scores.items():
        string = f"{string}{k:<18s} {str(v):<5s}\n"
    return f"Result: {result}\n{string}"


# function replay takes user input to replay or end the game
def replay():
    while True:
        play_game_again = input("\u2551 Do you want to play again? (y/n): ").upper()
        if play_game_again == "Y":
            return "\u2551 \033[92mPlaying again!\033[0m"
        elif play_game_again == "N":
            return "\033[92m\u2551 Thank you for playing...\033[0m"
        else:
            print("\u2551 \033[91mInvalid input! Please try again (only type y or n).\033[0m")
