import random

YorN = input("Do you want to flip a coin? Y/N: ").lower()
if YorN == "yes" or YorN == "y":
    coinFlip = random.randint(1, 2)
    if coinFlip == 1:
        print("Heads!")
    else:
        print("Tails!")
else:
    print("Oh, ok :(")