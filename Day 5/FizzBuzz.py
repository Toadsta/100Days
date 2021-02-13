for number in range(1, 101):
    string = "" #this blank string will be added to each time the script is ran if multple of 3 fizz, 5 buzz, both fizzbuzz, if neither just the number
    if number % 3 == 0 and number % 5 == 0: #This one is first as it cannot be skipped
        string += "FizzBuzz"
    elif number % 3 == 0:
        string += "Fizz"
    elif number % 5 == 0:
        string += "Buzz"
    else:
        string += str(number)
    print(string)
