ui = int(input("Enter a number: "))

if ui % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")
    
print("The sequence of numbers are: ")
for number in range(ui-2, 0, -2):
    print(number)