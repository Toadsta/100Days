number = int(input("Welcome to the number checker, input a number to see if its odd or even: "))

#this % is called modulo, it calculates the remiander of any number, if its even its 0 if its odd its 1
remainder = number % 2

if remainder == 1:
    print("Thats an odd number!")
else:
    print("Thats an even number!")