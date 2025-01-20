name = str(input("Enter a Name: "))
num = int(input("Enter a Number: "))

if num % 2 == 0:
    if num % 9 == 0 or num % 5 == 0:
        print(f"Hi {name}, the number you enter is EVEN Number, and {num} is divisible by 9 or 5")
    else:
        print(f"Hi {name}, the number you enter is EVEN Number, but {num} is not divisible by 9 or 5")
else:
    if num % 9 == 0 or num % 5 == 0:
        print(f"Hi {name}, the number you enter is ODD Number, and {num} is divisible by 9 or 5")
    else:
        print(f"Hi {name}, the number you enter is ODD Number, but {num} is not divisible by 9 or 5")