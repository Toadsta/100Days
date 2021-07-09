#You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. 
#Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
import math

def paintAmount(Length, Width, paintPerMeter):
    areaWall = Length * Width
    paintNeeded = areaWall/paintPerMeter
    canNeeded = math.ceil(paintNeeded)
    print(f"The number of cans needed is {canNeeded}")

paintAmount(Length=float(input("What is the length of the wall in meters: ")), Width=float(input("What is the width of the wall in meters: ")), paintPerMeter=float(input("How much paint can one can cover in meters: ")))