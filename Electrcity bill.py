units=int(input("Enter the Number of Units:"))
Amount=0
if units <= 100:
    print("you will not pay a single Rupee")
elif units > 100 and units <= 200:
    Amount = (units - 100)*5
    print("The Amount is to pay by user is : ",Amount)
elif units >= 200:
    Amount =500+ (units - 200)*10
    print("The Amount pay by User is :",Amount)
else:
    print("The user is out of limit")
