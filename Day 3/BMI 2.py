#some code from bmi.py
height = input("Enter your heigh in M: ")
weight = input("Enter your weight in Kg: ")

#Inputs are in str so i convert them into floats
bmi = (float(weight) / (float(height) ** 2) )
bmi = round(bmi)

#The reason i made bmiMeaning if this was intergrated into an app it could be stored
if bmi < 18.5:
    bmiMeaning = "underweight"
    print(f"Your BMI is {bmi}, this means you are {bmiMeaning}!")
elif bmi <= 25:
    bmiMeaning = "normal weight"
    print(f"Your BMI is {bmi}, this means you are a {bmiMeaning} :) ")
elif bmi <= 30:
    bmiMeaning = "overweight"
    print(f"Your BMI is {bmi}, this means you are {bmiMeaning}!")
elif bmi <=35:
    bmiMeaning = "obese"
    print(f"Your BMI is {bmi}, this means you are {bmiMeaning}! ")
else:
    bmiMeaning = "clinically obese"
    print(f"Your BMI is {bmi}, this means you are {bmiMeaning}! ")