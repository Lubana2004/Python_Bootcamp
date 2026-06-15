print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
        photo = bool(input("Would you like to see the picture? "))
        if photo == True:
            print("you have to pay $6")
    elif age <= 18:
        print("Please pay $7.")
        if photo == True:
            print("you have to pay $8")
    else:
        print("Please pay $12.")
        if photo == True:
            print("you have to pay $10")
        else:
            print("no photo")



else:
    print("Sorry you have to grow taller before you can ride.")
