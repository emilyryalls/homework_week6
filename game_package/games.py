def get_user_greeting(name, game_name):
    """
    This function takes the player's name and combines it with a predetermined welcome message to introduce the game.
    This function also adds the game name which the user has chosen based on the integer between 1-3.
    :param name: str
    :param game_name: str
    :return: str
    """
    name = input("Please Enter Your Name: ").capitalize()
    message = f"Hi {name}! Welcome to Get into Tech Games 2025!\nLet's play a game of {game_name}!\nWill you be able to beat me?\nLet's find out!"
    return message


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
    return f"Result: {result}\n{string}"


def replay():
    while True:
        play_game_again = input("Do you want to play again y/n?").upper()
        if play_game_again == "Y":
            return "Yes"
        elif play_game_again == "N":
            return "Thank you for playing"
        else:
            print("Please try again - only type y or n")