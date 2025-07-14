import random
a=random .randint(1,10)
s=int(input("Enter Number:"))
if a==s:
    print("Correct")
else:
    print("Incorrect")
    print("Computer has selected",a)