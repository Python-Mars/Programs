n=input("Enter the number: ");
test=n;
top=0;
temp=0;
while (n!=0):
    temp=n%10;
    top=top+temp*temp*temp;
    n=n/10;

if (test==top):
    print "Armstrong";
else:
    print "Not Armstrong"
