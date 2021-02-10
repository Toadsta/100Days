import random
import sys

userInput = input("Lets play rock, paper, scissors, what do you choose: ").lower()
if userInput == "rock":
    userChoice = 0
elif userInput == "paper":
    userChoice = 1
elif userInput == "scissors":
    userChoice = 2
else:
    sys.exit("Sorry that is not an input please re run the program")
choiceSelection = [0, 1, 2]
computerChoice = random.choice(choiceSelection)

if userChoice == 0:
    if computerChoice == 0:
        print("The computer chose rock, it's a draw!.")
    elif computerChoice == 1:
        print("The computer chose paper, you loose!")
    else:
        print("The computer chose scissors, you win!")
elif userChoice == 1:
    if computerChoice == 0:
        print("The computer chose rock, you win!.")
    elif computerChoice == 1:
        print("The computer chose paper, it's a draw!!")
    else:
        print("The computer chose scissors, you loose!")
elif userChoice == 2:
    if computerChoice == 0:
        print("The computer chose rock, you loose!.")
    elif computerChoice == 1:
        print("The computer chose paper, you win!!")
    else:
        print("The computer chose scissors, it's a draw!")
else:
    print("Sorry that is not an option")


