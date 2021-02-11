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

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gameImages = [rock, paper, scissors]

if userChoice == 0:
    if computerChoice == 0:
        print(f"The computer chose:\n{gameImages[computerChoice]}\nIt's a draw!.")
    elif computerChoice == 1:
        print(f"The computer chose:\n{gameImages[computerChoice]}\nYou loose!")
    else:
        print(f"The computer chose:\n{gameImages[computerChoice]}\nYou win!")
elif userChoice == 1:
    if computerChoice == 0:
        print(f"The computer chose:\n{gameImages[computerChoice]}\nYou win!.")
    elif computerChoice == 1:
        print(f"The computer chose:\n{gameImages[computerChoice]}\nIt's a draw!!")
    else:
        print(f"The computer chose:\n {gameImages[computerChoice]}\nYou loose!")
elif userChoice == 2:
    if computerChoice == 0:
        print(f"The computer chose:\n{gameImages[computerChoice]}\nYou loose!.")
    elif computerChoice == 1:
        print(f"The computer chose:\n{gameImages[computerChoice]}\nYou win!")
    else:
        print(f"The computer chose:\n{gameImages[computerChoice]} \nIt's a draw!")
else:
    print("Sorry that is not an option")


