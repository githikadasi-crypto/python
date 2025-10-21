£ Taking total amount as input from User
Amount =int(input("Please Enter Amount for Withdraw :"))
£ Calculating the number of notes of differentrr demonominations
note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10
print("")
