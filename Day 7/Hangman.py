#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#Randomly choose a word from the word_list and assign it to a variable called ChosenWord.
import random
ChosenWord = random.choice(word_list)

#Combine a list into a seperate characters
def listToText(text): 
    # initialize an empty string
    text1 = " " 
    # return string  
    return (text1.join(text))

#create a list with same amount of blank spaces as the word
correctanwserlist = [] 
lengthChosenWord = len(ChosenWord)
correctanwserlist += lengthChosenWord * "_"

#Checking if the anwser is correct and if it is, it will add it to the correct place 
lives = 7
display = 0
HANGMANPICS = ['''
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
while "_" in correctanwserlist and lives > 0:

    posofletter = -1 #its -1 as lists start at 0 not 1
    guess = input(f"{HANGMANPICS[display]} \nSo far you have '{listToText(correctanwserlist)}'\nYou have {lives} lives remaining, what is your guess? ").lower()
    if guess in ChosenWord:
        for letter in ChosenWord:
            if letter == guess:
                posofletter += 1
                correctanwserlist[posofletter] = guess
            else: 
                posofletter += 1
    else:
        print("That was wrong, you lose a life!")
        lives -= 1
        display += 1

if lives > 0:
    print(f"{HANGMANPICS[display]}\nWelldone, you won with {lives} lives remaining, the correct anwser was {ChosenWord} ")
else:
    print(f"{HANGMANPICS[display]}\nOh no, you ran out of lives, the correct anwser was {ChosenWord} ")