t="Bookmyshow"
print "\n"
print(t.center(100))

print("1. Book \t 2. Remaining \t 3. Cancel \t 3. Exit")
print "\n"
option=input("Enter the choice: ")
print option

if(option==1):
    book=input("Enter how many tickets you want: ")
    print ("Successfully book the tickets",book)
    print("1. Book \t 2. Remaining \t 3. Cancel \t 3. Exit")
    sub = input("Enter the choice: ")
    if(sub==2):
        total=100
        rem=total-book
        print "Remaing Tickets"
        print rem
        print("1. Book \t 2. Remaining \t 3. Cancel \t 3. Exit")
        sub = input("Enter the choice: ")
    if(sub==3):
        can=input("How many tickets cancel: ")
        print can
        print "Sucessfully canceled"
        print "Total tickets"
        num=can+rem
        print num
    sub = input("Enter the choice: ")
    if (sub == 4):
        print "Exit"

