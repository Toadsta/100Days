aprice = 20
cprice = 5
tprice = 10
sprice = 15
pprice = 5

print("To ride this coaster you must be 120cm!")
print(f"The adult price is ${aprice}, the senior adult is ${sprice}, the child price is ${cprice}, and the teen price is ${tprice}\nIf you want a photo it's an extra ${pprice}")

height = int(input("How tall are you in cm? "))

#Below is a nested if else statement, the program validates the heigh first then tells them the price it will be, 
#if age is greater than 17 you pay aprice if younger than 12 you pay cprice if youre a teen yoy pay tprice

if height >= 120:
    age = int(input("Also, how old are you? "))
    #this first one checks if you're under 13
    if age <= 12:
        #print(f"Yay, you're tall enough to ride, please pay ${cprice} ") -removed to condense code
        TicketPrice = cprice
    #this elif means else if you can have as many in a row as you want in a row instead of nesting and making the code very long horizontally
    elif age >= 65:
        #print(f"Yay, you're tall enough to ride, please pay ${sprice}")
        TicketPrice = sprice
    elif age >= 18:
        #print(f"Yay, you're tall enough to ride, please pay ${aprice}")
        TicketPrice = aprice
    #this final else means if you met non of the above condtions you will have that price in this case teens.
    else:
        #print(f"Yay, you're tall enough to ride, please pay ${tprice}")
        TicketPrice = tprice

    wantsPhoto = input("Would you like a photo while you're on the ride? Y/N ")
    if wantsPhoto == "Y":
        finalPrice = TicketPrice + pprice
        print(f"Great, your total cost is ${finalPrice} ")
    else:
        finalPrice = TicketPrice
        print(f"Great, your totalcost is ${TicketPrice} ")




#below is saying if your height is less than 120 they cant ride, else you can ride.
else:
    howShort = 120 - height
    print(f"Sorry, you are {howShort}cm to small try again when you grow!")
