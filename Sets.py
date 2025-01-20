def printLongLine():
    print("\n----------------------------------------")

fruits = {
    "apple",
    "banana",
    "cheer"
}
printLongLine()

print(fruits)
# Test if apple is in the fruit set
print("Apple in the sets" if ("Apple").lower() in fruits else "Apple not in set")
printLongLine()

# Union of two sets (Combining 2 sets)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2) # Removes duplicate
set4 = set2.intersection(set1) # Returns the duplicate
print("Union sets are the following: ") 
print(set3)
print("Duplicate sets are the following: ") 
print(set4)