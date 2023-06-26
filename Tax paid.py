price = int(input("Enter the cost of the bike: "))
tax=0
if price > 100000:
    tax = (15/100)*price
    print("The tax to be paid by the Customer:",tax)
elif price > 50000 and price <= 100000:
    tax= (10/100)*price
    print("The tax to be paid by the Customer:",tax )
elif price <= 50000:
    print("The tax to be paid by the Customer:",tax)
else:
    print("You won't Pay any tax to the Company")