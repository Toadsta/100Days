
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(Message, Shift):
    uM = list(Message)
    eM = []
    for char in range(0, (len(uM))):
        if uM[char] not in alphabet: #if a special character isnt in the alphabet list it will just skip it by adding the unencrypted version
            eM.append(uM[char])
        else:
            iOL = alphabet.index(uM[char])
            iNL = iOL + Shift
            while iNL > 25:
                iNL = -1 + Shift
            eM.append(alphabet[iNL])
    fM = "".join(eM)
    print(f"Your encrypted word is {fM}")

def deencryption(Message, Shift):
    uM = list(Message)
    dM = []
    for char in range(0, (len(uM))):
        if uM[char] not in alphabet:
            dM.append(uM[char])
        else:
            iOL = alphabet.index(uM[char])
            iNL = iOL - Shift
            while iNL > 25:
                iNL = -1 - Shift
            dM.append(alphabet[iNL])
    fM = "".join(dM)
    print(f"Your deencrypted word is {fM}")

keepGoing = True
while keepGoing == True:
    uInputED = input("Would you like to encrypt or decrypt? ").lower()
    if uInputED == "encrypt" or uInputED == "e":
        Message = input("What message would you like to encrypt? ").lower()
        Shift = int(input("How many numbers would you like to shift by? "))
        while Shift > 26:
            Shift = Shift - 26
        encryption(Message, Shift)
        uInput = input("Would you like to keep going? y/n: ").lower()
        print(uInput)
        if uInput == "y":
            keepGoing = True
        elif uInput == "n":
            keepGoing == False
        else:
            print("That is not an option please try again!")
    elif uInputED == "deencrypt" or uInputED == "d":
        Message = input("What message would you like to dencrypt? ").lower()
        Shift = int(input("How many numbers would you like to deshift by? "))
        while Shift > 26:
            Shift = Shift - 26
        deencryption(Message, Shift)
        uInput = input("Would you like to keep going? y/n: ").lower()
        if uInput == "y" or uInput == "yes":
            keepGoing = True
        elif uInput == "n" or uInput == "no":
            keepGoing == False
        else:
            print("That is not an option please try again!")
    else:
        print("Sorry thats not an option. Please try again!")

        #note to self this isnt working it doesnt recognise no
    
