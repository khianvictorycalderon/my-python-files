
def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        x = number * factorial(number - 1)
        return x
    
def summation(number):
    if number == 1:
        num = 1
    else:
        num = number + summation(number - 1)
    return num
    
print("Factorial: ")
print(factorial(5))
print("------------------------------------\n")


print("Summation: ")
print(summation(5))
print("------------------------------------\n")