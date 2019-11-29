number=int(input("Enter the number: "))

fact=1

if(number==0):
    print("No Factorial")
elif (number<=0):
    print("No Factorial")
else:
    for i in range(1,number+1):
        fact=fact*i

print("Factorial of",number,"is",fact)
