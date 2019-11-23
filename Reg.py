id=int(input("Enter id number:  "))
print("\n")
if(id==100):
    print("Access Successful")
    print("\n")
    name="Welcome to Red Mirchi Company"
    print(name.center(100))
    print(" ")
    print("1.Name\t 2. Location")
    sub=int(input("select the option: "))
    print("\n")
    if(sub==1):
        print("Selected option 1 ")
        Name=input("Enter the name: ")
        print("\n")
        print("Your Name",Name)
        sub=int(input("select the option: "))
        print("\n")
    if(sub==2):
        print("Selected option 2")
        location=input("Enter the location:  ")
        print("\n")
        print("Location: ",location)

        print("Name:",Name)
        print("Location:",location)

else:
    print("Access Denied")
