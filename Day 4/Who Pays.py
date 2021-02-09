import random
#this code will create a list and pull out at random a name
inputNames = input("Input the names of those who are playing in the format name, name, name etc: ")
names = inputNames.split(", ") #this splits the input at the comma and adds each name individually to the list.
#    whoPays = random.randint(1, (len(names)-1) ) #The -1 here is because it starts at the index - old code
#The whoPays var can be shorted by using the random.choice(names) see below
whoPays = random.choice(names)
#    print(f"{names[whoPays]}, is the person who pays today!") - old code
print(f"{whoPays}, is the person who pays today!") 