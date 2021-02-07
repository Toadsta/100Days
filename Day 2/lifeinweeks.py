print("Wanna see how long you have left?")
age = input("Whats your age? ")

numberOfYearsLeft = 90 - int(age)
numberOfMonthsLeft = numberOfYearsLeft * 12
numberOfWeeksLeft = numberOfYearsLeft * 52
numberOfDaysLeft = numberOfYearsLeft * 365

print(f"You have {numberOfYearsLeft} years, {numberOfMonthsLeft} months, {numberOfWeeksLeft} weeks, {numberOfDaysLeft} days ")