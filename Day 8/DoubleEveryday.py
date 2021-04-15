money = float(input("How much money would you like to double each day? £"))
daystodouble = int(input("How many days would you like to double this money for? "))
for x in range(1, daystodouble):
    double = money*2
    previousmoney = 0 + money
    money = double

totalmoney = money + previousmoney    
moneycomma = "{:,}".format(totalmoney)

    
print(f"£{moneycomma}")
