choice = int(input("How many pairs of socks do you own?"))
if choice <5:
    print("You need to buy more socks")
elif choice >=5:
    print("That's a good amount of socks")
elif choice >10:
    print("Those are too many socks")
    
print()
    
choice = input("Do you like black or red?")
choice2 = input("Do you like mountains or midwest?")
if choice == "black":
    if choice2 == "mountains":
        print("You should go to CU Boulder")
    elif choice2 == "midwest":
        print("You should go Iowa")
elif choice == "red":
    if choice2 == "mountains":
        print("You should go to New Mexico")
    elif choice2 == "midwest":
        print("You should go to UW Madison")
