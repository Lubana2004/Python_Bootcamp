print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S":
    bill = 15
    if pepperoni == "Y":
        bill =17
        if extra_cheese == "Y":
            bill = 16

elif size == "M":
    bill = 20
    if pepperoni == "Y":
        bill = 22
        if extra_cheese == "Y":
            bill = 21
else:
    bill = 25
    if pepperoni == "Y":
        bill = 27
        if extra_cheese == "Y":
            bill = 26
print("Your bill is $" + str(bill))
