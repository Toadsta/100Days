print("To ride this coaster you must be 120cm!")

height = int(input("How tall are you? (in CM) "))
#below is saying if your height is less than 120 they cant ride, else you can ride
if height < 120:
    print("Sorry, you are to small try again next year!")
else:
    print("Yay, you're tall enough, please enter!")