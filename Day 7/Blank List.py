import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)


guess = input("Guess a letter: ").lower()

eList = [] 
intergerofchosenword = len(chosen_word)
eList += intergerofchosenword * "_"
#Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"]
for pos in range(intergerofchosenword):
    letter = chosen_word[pos]
    if letter == guess:
        eList[pos] = letter
print(eList)

#Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
