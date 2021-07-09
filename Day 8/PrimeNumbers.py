def Checker(Number):
    flag = False
    for primechecker in range(2, Number): #here we are running a program to find wether Number is devisble by 2 to Number, if it gives a remainer of 0 we know it has another more than 1 and itself as divisible.
        if Number % primechecker == 0:
            flag = True
            break
    if flag == True or Number == 1: #Ive placed this or = 1 as with this method 1 is classed as prime but it is not as its only devisible by one number.
        print(f"{Number} is not prime!")
    else:
        print(f"{Number} is prime!")

Checker(int(input("What number do you want to check? ")))
