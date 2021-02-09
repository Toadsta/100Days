#Randomisation

#Nothing in computing can be truely random, their can be psudeorandom. In python they use Mersenne
#this imports the random module, a module is a peice of code that does a job so in this case the random module is a bit of code that does the math, instead of use doing it
import random
#to get a random number we use randint

#this code prints a random number between 100 and 200
a = random.randint(100, 200)
print(a)

#this prints a random floating number between 0 and 1 but not 1 or 0, if you want the float to go up to any number just times it, i.e below i added *100 which makes it between 0 and 100
b = random.random() * 100
print(b)

#Lists
#You can store mutliple things in a var, it also shows the order they are added
#exampleList = [item1, item2]

CountriesOfUk = ["England", "Scotland", "Woles"]
#above you can see the order of when they where added! The order isnt lost.
print(CountriesOfUk)

#if you wanted to check what the first thing in a list is you would do:
print(CountriesOfUk[0]) #In python 0 is the start of a list not 1
#you can also use a minus index: these both give the same anwser
print(CountriesOfUk[-3])

#swapping them
#as you can see i spelt wales wrong, to fix this i will do:
CountriesOfUk[2] = "Wales"
#I change the index 2 to say wales instead of woles
print(CountriesOfUk)

#To add to the list we do the following
CountriesOfUk.append("Northern Ireland") #this adds the text to the end 
print(CountriesOfUk)

#you can also use other .suffixes such as extend
CountriesOfUk.extend(["Jersey", "Isle of Man", "Gurnsey"])
#the extend adds a list to the list, there is also other suffixes such as .insert .remove .pop https://docs.python.org/3/tutorial/datastructures.html
print(CountriesOfUk)

#Below ask for a list of countires
inputCountries = input("Input the countries of the UK in the this format Country, Country, Country etc:  ")
#this split command turns the string input into a list by removing the ", " from the input string. https://www.askpython.com/python/string/convert-string-to-list-in-python
CountriesOfUk = inputCountries.split(", ")

#Common index errors, index out of range means you are trying to get a piece of infomation that is outside the range of the list i.e you try and get list(50) but there is only 49 

#Nested Lists are used when you have a list but you want sub lists.

Country = ["England", "Scotland", "Wales", "Northern Ireland"]
Counties = ["Too Many To Type", "1", "2", "3"]
UnitedKingdom = [Country, Counties] # this list contains 2 lists
print(UnitedKingdom)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]

#if the 1 was a 0 it would print the 3rd option on line 1, since its a 1 it prints the 3rd option of line 2 
print(dirty_dozen[1][3])