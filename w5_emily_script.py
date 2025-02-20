# Create a game of rock paper scissors
# The user will play against the computer
# You should design a program that does the following:
# Prompt the user to enter a value: R, P or S
# The programme should convert this value into Rock, Paper or Scissors respectively
# Asks the computer to generate a random value between 0 and 2
# Convert the computer's choice. 0 becomes Rock; 1 becomes Paper; 2 becomes Scissors
# Compare the user's choices with the computer's choice to display a message indicating whether the user won, lost or drew against the computer
# Showcase what you have learned about conditional statements and create your own functions

# human_input = input("Input R, P or S:")
# human_rps = (convert_user(human_input))
# print(human_rps)
# computer_rps = computer()
# print(computer_rps)

from w5_emily_module import convert_user, computer, play_rps

# having game as a function
human_input=None
score = 0

while human_input != 'QUIT':
    human_input = input("Input R, P or S, or type QUIT to exit game:")
    if human_input == "QUIT":
        break
    elif human_input != 'R' and human_input != 'P' and human_input != 'S':
        print('Please try again. Make sure letter is capitalised and has no spaces.')
    else:
        # Rock, Paper or Scissors assigned to human_rps
        human_rps = (convert_user(human_input))
        print(f" You: {human_rps}")
        # Rock, Paper or Scissor assigned to computer_rps
        computer_rps = computer()
        print(f" Computer: {computer_rps}")
        score = play_rps(human_rps, computer_rps, score)
        # assign score to a variable within the loop so the value is fed back into the loop
        # function play_rps returns the value of score