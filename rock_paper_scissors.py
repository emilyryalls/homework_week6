
import random
# imported random which is pseudo-random number generator function


# created a function called user-answer which captures user input as a "String"
# DOC strings are used to describe the function
def user_answer():
    """
    captures User's input
    :return: String
    """
    answer = input("Choose one- R, P or S:").upper()
    # the input function would allow user to provide input
    # .upper method is to capture the user input and put in the upper case to enable the loop continuation
    if answer == "R":
        print("Your choice is Rock")
    #     conditional statements are use to assign the value as per the user choice
    #     strings are assigned value corresponding to it as per the game rules
    elif answer == "P":
        # conditional statements are use to assign the value as per the user choice
        print("Your choice is Paper")
    elif answer == "S":
        # conditional statements are use to assign the value as per the user choice
        print("Your choice is Scissors")
    return answer


# # created a function called computer_answer which captures user input as an "Integer"
# # DOC strings are used to describe the function
def computer_answer():
    """
    capture the computer choices
    :return: integer
    """
    comp_answer = random.randint(0, 2)
    # .randint method is used to chose random number from the given range by the random function
    # the random number is assigned to a variable which is comp_answer
    # print(f"Computer choice is {comp_answer}")
    if comp_answer == 0:
        # using conditional statement to assign the response corresponding to the integer which is equivalent to computer's choice
        print("Computer choice is Rock")
    elif comp_answer == 1:
        # # using conditional statement to assign the response corresponding to the integer which is equivalent to computer's choice
        print("Computer choice is Paper")
    elif comp_answer == 2:
        # # using conditional statement to assign the response corresponding to the integer which is equivalent to computer's choice
        print("Computer choice is Scissors")
    return comp_answer

def comparison(user_input, comp_input):
    # a function is defined and described to run comparison of each response from user and computer inputs
    # it compares the string value from user input and integer value from computer input
    """
    compare the user input and computer input
    :param user_input: string
    :param comp_input: integer
    :return: String
    """
    if user_input == "R" and comp_input == 0:
        # a response is generated from the comparison of input values from user and computer and printed to declare the winner
        print("Its a tie!")
    elif user_input == "R" and comp_input == 1:
        #  # a response is generated from the comparison of input values from user and computer and printed to declare the winner
        print("You lose, Computer Wins!")
    #      # a response is generated from the comparison of input values from user and computer and printed to declare the winner
    elif user_input == "R" and comp_input == 2:
        #  # a response is generated from the comparison of input values from user and computer and printed to declare the winner
        print("You WIN, Computer lose!")
    elif user_input == "P" and comp_input == 0:
        print("You WIN, Computer lose!")
    elif user_input == "P" and comp_input == 1:
        print("Its a tie!")
    elif user_input == "P" and comp_input == 2:
        print("You lose, Computer Wins!")
    elif user_input == "S" and comp_input == 0:
            print("You lose, Computer Wins!")
    elif user_input == "S" and comp_input == 1:
         print("You WIN, Computer lose!")
    elif user_input == "S" and comp_input == 2:
         print("Its a tie!")
#          # a response is generated from the comparison of input values from user and computer and printed to declare the winner

def main():
    user = user_answer()
    comp= computer_answer()
    comparison(user,comp)
    print("print if the file is", __name__)

if __name__ == "__main__" :
    main()









