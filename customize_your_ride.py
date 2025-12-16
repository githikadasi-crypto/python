print("select your ride:")
print("1.bike")
print("2.car")
choice=int(input("Enter your choice:"))
if choice==1:
    print("you have seleccted bike")
    print("select your bike type:")
    print("1.sport bike")
    print("2.cruiser bike")
    choice2 = int(input("Enter your choice:"))
    if choice2==1:
        print("you have selected sport bike")
    elif choice2==2:
        print("you have selected cruiser bike")
    else:
        print("invalid choice")
elif choice==2:
    print("you have selected car")
    print("select your car type:")
    print("1.sedan")
    print("2.suv")
    choice3 = int(input("Enter your choice:"))
    if choice3==1:
        print("you have selected sedan")
    elif choice3==2:
        print("you have selected suv")
    else:
        print("invalid choice")
else:
    print("invalid choice")