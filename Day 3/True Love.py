#Logical operators check for multiple condtions in the same size of code
#A and B # means both need to be true for code to run
#C or D # means only 1 needs to be true for code to run
#not E # means as long as E isnt present the code will run

#lower changes all the string to lower case
name1 = (input("What is your name? "))
name2 = (input("What is their name? " ))

name1 = name1.lower()
name2 = name2.lower()
totalLength = len(name1 + name2)
trueLength = (name1.count("t" or "r" or "u" or "e" ) + name2.count("t" or "r" or "u" or "e" ))
loveLength = (name1.count("l" or "o" or" v" or "e") + name2.count("l" or "o" or "v" or "e"))

TrueLove = str(trueLength)+str(loveLength)
TrueLove = int(TrueLove)

if TrueLove < 10 or TrueLove > 90 :
    print(f"Uh oh, its only a score of {TrueLove}, you go together aswell and diet coke and mentons ")
elif TrueLove >= 10 and TrueLove <= 30:
    print(f"You're amazing together, you are amazeballs, the score is {TrueLove} ")
elif TrueLove >= 30 and  TrueLove <= 60:
    print(f"Wow!, your love score is {TrueLove}, you are meant to be")
else:
    print(f"Your score is off the charts!, it's at {TrueLove}")