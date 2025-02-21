

from rock_paper_scissors import user_answer, computer_answer, comparison


name = input("Hello, what is your name?:")
print(f" Hello {name.capitalize()}, do you want to play a game of Rock 🪨, Paper 🗞️, Scissors ✂️ ")
us_consent = input("Please press Y for Yes or N for No.").upper()
if us_consent == "Y":
    print("Here we go, lets play a game of Rock 🪨, Paper 🗞️, Scissors ✂️ !!")
else:
    print("Ok, see you next time!")

user = user_answer()
comp = computer_answer()
comparison(user, comp)

repeat = input("Do you want to play again? Please type Y for Yes and N for No?").upper()


while repeat == "Y":
    user = user_answer()
    comp = computer_answer()
    comparison(user, comp)
    repeat = input("Do you want to play again? Please type Y for Yes and N for No?").upper()

else:
    print("It sad to see you go! See you next time, bye!")












