#I will be using % which is known as a modulo, if a number is divisble output is 0, if it isnt output is any other number

year = int(input("What is the current year? "))

#this does if year is divisible by 4
Conditon1 = year%4
#if the year is divsible by 4 it moves on if not its failed and is moved to the else part straight away.
if Conditon1 == 0:
    #this code checks to see if the year is divisble by 100 if it is its moved to next stage, if not it moves straight to else
    Conditon2 = year%100
    if Conditon2 == 0:
        #this checks if its divisible by 400 the final conditon, if it is divisible it passes, if its not it moves to else.
        Conditon3 = year%400
        if Conditon3 == 0:
            print("It's a leap year")
        else:
            print("It's not a leap year")
    else:
        print("It's a leap year!")
    
else:
    print("It's not a leap year")

#side notes, this took quite a while because im stupid and forgot how dividing works, modulo (%) checks to see if a number is divisible
#if it is the output is 0 if it isnt its any other number.