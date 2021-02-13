import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Toad's password generator!")
letterAmount= int(input("How many letters would you like in your password?\n")) 
symbolAmount = int(input(f"How many symbols would you like?\n"))
numberAmount = int(input(f"How many numbers would you like?\n"))

finalList = []
for letter in range(0, letterAmount):
    finalList.append(random.choice(letters))

for symbol in range(0, symbolAmount):
    finalList.append(random.choice(symbols))

for number in range(0, numberAmount):
    finalList.append(random.choice(numbers))

#password = ""
#for listPicker in range(0, (letterAmount + symbolAmount + numberAmount)):
    #password += random.choice(finalList)

#Simpler way of doing above
password = ""
random.shuffle(finalList)
for listPicker in finalList:
    password += listPicker

print(f"Your new password should be {password}")
    

