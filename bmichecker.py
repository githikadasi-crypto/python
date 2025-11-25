hieght=float(input("Enter your height in centimeter: ") )
weight=float(input("Enter your weight in kilogram: ") ) 
bmi=weight/(hieght/100)**2
print("your bmi is:",bmi)
if bmi<18.4:
    print(("you are underweight"))
elif 18.4<=bmi<=24.9:
    print("you are healthy")
elif 25.0<=bmi<=29.9:
    print("you are severly overweight")
elif 30.0<=bmi<=34.9:
    print("you are obese")
print("you are severly obese")