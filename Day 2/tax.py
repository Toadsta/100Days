#Also  i changed all int to float just incase of decimals
print("Welcome to the tip calculator")
bill = input("What was the total bill? ")
people = input("How many people to split the bill? ")
tip = input("What percentage tip would you like to give? ")

#this calcuates the tax needed to be added to the bill
tax =  ( ( float(bill) / 100 ) * float(tip) )
#billtax is bill + tax
billtax =  float(tax) + float(bill) 
#this is now going to divide billtax by number of people
finalpayment = float(billtax) / float(people)

#I added this round function as the bill sometimes came out as a really long string the 2 means to a decial point of 2
finalpayment = round(finalpayment, 2)
#This is formating it so the finall amount is always to 2dp and never 0 or 1
finalpayment = "{:.2f}".format(finalpayment)

#The str changes the number into a string so I can add the text to the front. If youre unsure of type use print(type("thing"))
print(f"Each person should pay ${finalpayment}" )