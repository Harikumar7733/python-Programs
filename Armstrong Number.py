num = int(input("Enter the Number:"))
l = len(str(num))
count=0
sum=0
orginal = num
while(num > 0):
  count = num % 10
  sum += count ** l
  num = num//10
if sum == orginal:
  print('The number is Armstrong Number')
else:
  print("The Number is not a Armstorng Number")

