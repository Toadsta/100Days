s_base = 5
m_base = 7
l_base = 9

tomato_sauce = 2
bbq_sauce = 3
garlic_sauce = 2.5

cheese = 1
pepperoni = 2
sausage = 2
bacon = 2

bill = 0

print("Welcome to Toby's Pizzeria!")
baseOption = input("What size pizza would you like? Large/Medium/Small:")

if baseOption == "Large":
    bill += l_base
elif baseOption == "Medium":
    bill += m_base
elif baseOption == "Small":
    bill += s_base
else:
    print("Invalid option please restart program!")
    


sauceOption = input("Excellent, what type of sauce would you like? Tomato/BBQ/Garlic: ")

if sauceOption == "Tomato":
    bill += tomato_sauce
elif sauceOption == "BBQ":
    bill += bbq_sauce
elif sauceOption == "Garlic":
    bill += garlic_sauce
else: 
    print("Invalid option please restart program!")

toppingOption = input("Excellent sauce! What toppings would you like? Cheese/Pepperoni/Sausage/Bacon: " )

if toppingOption == "Cheese":
    bill += cheese
elif toppingOption == "Pepperoni":
    bill += pepperoni
elif toppingOption == "Sausage":
    bill += sausage
elif toppingOption == "Bacon":
    bill += bacon
else:
    print("Invalid option please restart program!")

anotherTopping = input("Would you like another topping? Y/N: ")

if anotherTopping == "Y":
    toppingOption = input("Cheese/Pepperoni/Sausage/Bacon? " )
    if toppingOption == "Cheese":
        bill += cheese
    elif toppingOption == "Pepperoni":
        bill += pepperoni
    elif toppingOption == "Sausage":
        bill += sausage
    elif toppingOption == "Bacon":
        bill += bacon
    else:
        print("Invalid option please restart program!")

    taxPercent = 20
    tax = (bill/100)*taxPercent
    finalBill = tax + bill

    finalBill = "{:.2f}".format(finalBill)
    bill = "{:.2f}".format(bill)
    tax = "{:.2f}".format(tax)

    print(f"Excellent order, your total is ${finalBill}, made up of ${bill} bill and ${tax} tax! ")



