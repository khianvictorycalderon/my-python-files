# I learn these objects method in JavaScript, but i might as well apply it in python
# These are the 3 functions we will use:
# values() = Similar to Object.values() in JavaScript
# keys() = Similar to Object.keys() in JavaScript
# items() = Similar to Object.entries() in JavaScript
# and some advanced object methods

Name_Age = {
    "jake":15,
    "john":16
}

# To access the age of jake:
print(f"Jake's age is {Name_Age["jake"]}")

# To access the age of john:
print(f"John's age is {Name_Age["john"]}")

# To add value, simply add using equal sign
# This will also work on update, if you want to change the existing value of the dictionary
Name_Age["bob"] = 20
print(f"Bob's age is {Name_Age["bob"]}")
Name_Age["john"] = 21
print(f"John's new age is {Name_Age["john"]}")


#--------------------------------------------------------
# These are the 3 methods
Names = {
     # Keys     Values
    "person1": "Blake",
    "person2": "Afhina",
    "person3": "Suke",
    "person4": "Caine",
    "person5": "Michael"
}

# Accessing the keys
print()
NameKeys = Names.keys()
print("These are the keys: ")
for key in NameKeys: # iterate over the keys
    print(key)
    
# Accessing the values
print()
NameValues = Names.values()
print("These are the values of the keys: ")
for value in NameValues: # iterate over the values
    print(value)
    
# Accessing both the keys and the values
print()
NamePairs = Names.items()
print("These are the items (or entries in JavaScript):")
for key, value in NamePairs:
    print(f"{key} = {value}")