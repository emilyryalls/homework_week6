# This is a generalized module which has functions which can be reused for:
# 1. Greeting the user and getting the "name" of the user
# 2. Capturing the result (as draw, user won or computer won) and adding scores for user or computer
# 3. Print the results of scores of user and computer after each round
# 4. Asking the user if the want to replay the game or end the game.


# get_user_greeting function returns "message" as a f-string
def get_user_greeting(game_name):
    """
    This function takes the player's name and combines it with a predetermined welcome message to introduce the game.
    This function also adds the game name via string input.
    :param game_name: str
    :return: str
    """
    name = input("Please Enter Your Name: ").capitalize()
    message = f"Hi {name}! Welcome to Get into Tech Games 2025!\nLet's play a game of {game_name}!\nWill you be able to beat me?\nLet's find out!"
    return message


# function amend_scores returns the scores as per the result, after the user
# input and the computer input is compared
def amend_scores(result, scores):
    """
    This function amends scores that are stored in a dictionary, based on the result of a game, which is either a draw or computer /user wins
    :param result: str
    :param scores: 'dictionary'
    :return: 'dictionary'
    """
    if result == "It's a draw":
        return scores
    elif result == "Computer wins":
        scores["Computer score"] += 1
    else:
        scores["Your score"] += 1
    return scores

# The function return_results take two parameters, result=string and scores=dictionary
# and return a string which is key value pairs from the dictionary using the formatted strings
def return_results(result, scores):
    """
    This function returns the result of the game along with the User score and Computer Score using the string formatting
    :param result: str
    :param scores: dictionary
    :return: str
    """
    string = ""
    for k, v in scores.items():
        string = f"{string}{k:<18s} {str(v):<5s}\n"
    return f"Result: {result}\n{string}"

# function replay takes user input to replay or end the game
def replay():
    """
    This function returns the user input as Y or N for yes or No respectively to replay or end the game.
    :return: str
    """
    while True:
        play_game_again = input("Do you want to play again y/n?").upper()
        if play_game_again == "Y":
            return "Yes"
        elif play_game_again == "N":
            return "Thank you for playing"
        else:
            print("Please try again - only type y or n")