
dic = {
    "person1":"Kyle",
    "person2":"John",
    "person3":"Dale"
}

# Printing the dictionary as a whole
print(dic)

# Printing the keys of the dictionary
print(list(dic.keys()))

# Printing the values of keys of the dictionary
print(list(dic.values()))

# For printing every keys and values in a dictionary
for key, value in dic.items():
    print(f"{key}: {value}")