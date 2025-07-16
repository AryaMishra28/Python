import random
a=random .randint(1,10)
s=int(input("Enter Number:"))
if a<s:
    print("TOO BIG maybe a little small num")
elif a>s:
    print("TOO LESS maybe a little big num")
else:
    print("correct")
    print("Computer has selected",a)