#Here we are making a function, anytime i type greet() it will run the code in the function
def greet():
    print("Hello")
    print("How are you!")
    print("Lovely weather today?")

#Here we are calling the greet function from above
greet()

#Now we are going to give it inputs

def greetWithName(name): #Here it is creating a varible named name. This is known as a Parameter
    print(f"Hello {name}")
    print(f"How are you today {name}")

greetWithName(input("What is your name? ")) #Here we giving the var name data. This is known as an Argument

#Argument is the data ran through the code, whereas the Parameter is the name of the data. You use the parameter in the function to refer to the data stored within it.

#Functions with more than one input

def greetWith(Location, Name): #To add more than one Parameter just use , to seperate each parameter
    print(f"Hello {Name}")
    print(f"What is it like in {Location}")

greetWith(input("Where are you from? "), input("Whats your name? ")) #Much like above to to get the input for each parameter you just need to use , to seperate the inputs
#The code above is positional arguments as it defines an argument by the order it is typed in

#We dont have to put them in the corret order but it makes it easier. We could do this 
greetWith(Name=input("Whats your name? "), Location=input("Where are you from? "))
#This is a keyword arugmment as we use the parameter to define the argument not the position