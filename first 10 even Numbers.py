names = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
num = int(input("Enter the Number:"))
if num<=100:
   if num in names:
    k = names.get(num)
    print("yes we have Series")
   else:
    b=num%10
    b=names.get(b)
    c=num//10
    c=names.get(c)
    results=c+b
    print(num,"in words is", results)
else:
   print("error:enter a valid Number")
