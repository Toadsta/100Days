height = input("Enter your heigh in M: ")
weight = input("Enter your weight in Kg: ")

#Inputs are in str so i convert them into floats
bmi = (float(weight) / (float(height) ** 2) )
bmi = round(bmi)

#Converts BMI from float to str so it can print it
print("Your BMI is " + str(bmi))