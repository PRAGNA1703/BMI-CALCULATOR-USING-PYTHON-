#Enter your name 
name = input("Enter your name :")
#enter your weight in kilograms
weight = float(input("Enter your weight:"))
#enter your height in meters 
height = float(input("Enter your height :"))

bmi = weight / (height * height)
print(bmi)
if (bmi < 16 ):
    print(name +",You are under weight.")
elif ( bmi <= 24.9):
    print(name +",You are normal  weight.")
elif ( bmi <= 29.9):
    print(name +",You are overweight.")
elif ( bmi <= 34.9 ):
    print(name +",You are obese.")
elif ( bmi <= 39.9):
    print(name +",You are severely obese.")
else:
    print("Enter valid inputs .")