n=input("Enter the number: ");
top=0;
temp=0;
while (n!=0):
    temp=n%10;
    top=top*10+temp;
    n=n/10;
print top;
