

ui = float(input("Enter a temperature, regardless of units: "))
fahrenheit = (ui * (9 / 5)) + 32
celsius = (ui - 32) / (9 / 5)

print(f"{ui} celsius to fahrenheit is {fahrenheit}")
print(f"{ui} fahrenheit to celsius is {celsius}")