# This is a custom function

def isEven(number):
    return True if number % 2 == 0 else False

ui = input("Enter a number: ")
print("Number is even" if isEven(int(ui)) else "Number is odd")