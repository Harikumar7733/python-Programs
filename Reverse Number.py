num = int(input("Enter the number:"))
r = 0
reverse = 0
while(num>0):
    r = num % 10
    reverse = reverse * 10+r
    num = num//10
print("The Result is  ",reverse)