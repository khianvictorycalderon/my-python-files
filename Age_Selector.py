print()
print("Age Selector by Khian Victory D. Calderon")
print()
print("Usage:")
print(" 1.) Enter a name with equal sign to assign their age.")
print("   Example:")
print("    John = 15")
print(" 2.) That will add a name and age variable in the temporary storage.")
print(" 3.) To retrieve the age, simply enter the name you want to find the age.")
print("   Example:")
print("     John")
print("   Output:")
print("     John is 15 years old")
print(" 4.) To retrieve the name with that age, simply enter the age.")
print("   Example:")
print("    15")
print("   Sample Output:")
print("     Here are the names who are 15 years old")
print("     John")
print("     Jake")
print("     Bob")
print("   (This will input all the names with the age of 15)")
print(" 5.) To change the age of that name, simply reassign it.")
print("   Example:")
print("      John = 17")
print(' 6.) Type "Exit" or "Stop" or "Terminate" to stop the program.')
print()


age_data = {}
while True:
    ui = input("--> ").strip()

    if ui.lower() in ["exit", "stop", "terminate"]:
        print("Program terminated.")
        break
    
    if "=" in ui:
        try:
            name, age = ui.split("=")
            name = name.strip().capitalize()
            age = int(age.strip())
            age_data[name] = age
            print(f"Assigned {name} = {age}")
        except ValueError:
            print("Invalid input format. Please use 'Name = Age'.")

    elif ui.isdigit():
        age = int(ui)
        names_with_age = [name for name, person_age in age_data.items() if person_age == age]
        if names_with_age:
            print(f"Here are the names who are {age} years old:")
            for name in names_with_age:
                print(name)
        else:
            print(f"No names found for age {age}.")

    else:
        name = ui.capitalize()
        if name in age_data:
            print(f"{name} is {age_data[name]} years old.")
        else:
            print(f"No age found for {name}.")