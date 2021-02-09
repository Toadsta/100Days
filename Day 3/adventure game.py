print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("You have washed up on an island looking for the treasure of Toadsta, will you find it?.")
LorR = input("You're at a fork in the road, where do you want to go? Left/Right: ").lower()
if LorR == ("left") or LorR == "l":
    SorB = input("You walk down the left hand path, you see a river, do you swim across it or find a bridge? Swim/Bridge: ").lower()
    if SorB == "bridge" or SorB == "b":
        door = input("You follow the river to the nearest bridge and find a house with 3 doors. Which door do you enter? Red/Green/Blue: ").lower()
        if door == "red" or door == "r":
            print("You open the red door, and see nothing. You step inside and the door closes behind you! You are trapped!")
            print("Game Over - Unlocked Trapped Ending")
        elif door == "blue" or door == "b":
            print("The blue door intially refuses to open, you decide to kick it open. As you're about to kick it the door opens and you fall inside. There is no floor....")
            print("Game Over - You Unlocked The Limbo Ending")
        else:
            print("You open the green door, and see the most amazing treasure before you! A real life lightsaber!")
            print("You unlocked the best ending!")
    else:
        print("You begin to swim across the river, and just as you're about to reach the otherside you are pulled under by a alligator! ")
        print("Game Over! - You Unlocked, 'The Forbidden River' ending.")
else:
    print("You, walk down the right hand path, and the ground collapses under you!")
    print("Game Over! You Unlocked, The 'Underground Exploreer' Ending")
