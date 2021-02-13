#for loops

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits: #this creates a new variable called fruit and it runs until the list ends, the final var mem will be pear in this case. For is a loop
    print(fruit) #1
    print(fruit + " Pie") #2 then will go back to 1 until its finished
print(fruit) #not indented so not part of for loop, will be executed after for loop

#range

for number in range(1, 101): #range counts up to but not including last number
    print(number)

#range steps
for number in range(1, 101, 2): #range counts every 2nd number so 1,3
    print(number)