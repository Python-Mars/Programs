n=input("Enter the number: ");
test=n;
top=0;
temp=0;
while (n!=0):
    temp=n%10;
    top=top*10+temp;
    n=n/10;
print top;

if(test==top):
    print "Palindrome";
else:
    print "Not Palindrome";
