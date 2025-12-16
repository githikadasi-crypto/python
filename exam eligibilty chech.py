medical=input("Do you have any medical issues? (yes/no): ")   
atten=int(input("Is your attendance above 75%? (yes/no): "))
if medical == 'yes':
    print("You are eligible to sit for the exam.")
else :
    if atten>=75:
        print("You are eligible to sit for the exam.")
    else:
        print("You are not eligible to sit for the exam.")
