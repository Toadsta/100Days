programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}
#Retrieving Items
print(programming_dictionary["Function"])

#Adding new pieces of info to a list.
programming_dictionary["Loop"] = "The action of doing something over and over again"

#Empty dic
empty_dictionary = {}

#Wipe a dic
#programming_dictionary = {}

#Edit an item in a dic
programming_dictionary["Bug"] = "XYZ"

#Loop through a dic
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


#Nesting

dic = {"Key": "Value"} #Basic dic

list = ["Something"] #Basic list 

#Here you can put these 2 things into another dic or list
nesting = {
    "Key": list,
    "Key2": dic
}

#Heres a real world example
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#But if we wanted more than 1 city 

travelLog = {
    "Frace": ["Paris", "Bordeaux", "Lyon"],
    "Germany": ["Berlin", "Warmunde", "Kiel"]
}