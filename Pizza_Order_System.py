isOrdered = False
price = 0
total_price = 0

def printInvalidInput():
    print("Invalid input, try again!\n")

while True:
    isOrdered = input("Would you like to order a pizza? (Yes/No):\n-> ")
    if isOrdered.lower() == "yes":
        isOrdered = True
        break
    elif isOrdered.lower() == "no":
        print("Thank you for not ordering!\n")
        break
    else:
        printInvalidInput()
        
while isOrdered:
    while True:
        pizza_type = input("Which pizza would you like?\n- Hawaiian\n- Bolognese\n- Overload\n-> ")
        if pizza_type.lower() == "hawaiian":
            price += 15
            total_price += 15
            break
        elif pizza_type.lower() == "bolognese":
            price += 11
            total_price += 11
            break
        elif pizza_type.lower() == "overload":
            price += 18
            total_price += 18
            break
        else:
            print(f"Sorry, we don't have {pizza_type} type of pizza, choose another from the menu.\n")

    while True:
        size = input("Which size would you like?\n- Small\n- Medium\n- Large\n-> ")
        if size.lower() == "small":
            price += 5
            total_price += 5
            break
        elif size.lower() == "medium":
            price += 7
            total_price += 7
            break
        elif size.lower() == "large":
            price += 10
            total_price += 10
            break
        else:
            print(f"Sorry, we don't have {size} size of pizza, choose another from the menu.\n")

    addons = input("Would you like to add any add-ons?\n(Separate using comma, enter 'none' if no add-ons)\n-> ")
    addon_list = [addon.strip() for addon in addons.split(",") if addon.strip()]
    print()
    
    # Order Summary
    print("Order Summary: ")
    print(f"Pizza Type: {pizza_type}")
    print(f"Pizza Size: {size}")
    print(f"Cost: ${price}")
    if addons.lower() != "none" and addon_list:
        print(f"Add-ons: ")
        for addon in addon_list:
            print(addon)
    
    while True:
        orderAnother = input("\nWould you like to order another? \n(Yes/No)\n-> ")
        if orderAnother.lower() == "yes":
            price = 0
            print()
            break
        elif orderAnother.lower() == "no":
            print(f"\nThank you, the total cost is ${total_price}\n")
            isOrdered = False
            break
        else:
            printInvalidInput()
