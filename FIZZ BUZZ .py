u=int(input("Enter your staring range"))
a=int(input("Enter your ending range"))
for s in range(u,a+1):
    if s%3==0 and s%5==0:
        print("fizzbuzz")   
    elif s%3==0:
        print("fizz")
    elif s%5==0:
        print("buzz")
    else:
        print(s)



