#code to determine who can ride in the rollercoaster
height = int(input("Enter your height in feet: "))
if height >= 3:
    print("you can ride the rollercoaster")
    age = int(input("Enter your age: "))
    if age >=18:
        print("Pay 300 ksh.")
    else :
        print("Pay 200 ksh.")
else:
    print("We are sorry you don't qualify to ride the rollercoaster")