def replay():
    play_game_again = input("Do you want to play again y/n?")
    if not replay():
        return print("Thank you for playing")
    if play_game_again.lower() == "y":
        return True
    if play_game_again.lower() == "n":
        return False


for True in replay()
# initiate the game