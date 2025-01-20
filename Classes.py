
def PrintLongLine():
    print("------------------------------------")

class NewLaptop:
    def __init__(this, ThisID, ThisModel, ThisColor, ThisFunctional):
        this.id = ThisID # This is an identifier for the laptop
        this.model = ThisModel # Model of the laptop
        this.color = ThisColor # Color of the laptop
        this.functional = ThisFunctional # Is the laptop usable?
        
    # Methods Here: -------------------------------------------
    def PrintProperties(this):
        print(f"Laptop {this.id} model is: {this.model}")
        print(f"Laptop {this.id} color is: {this.color}")
        print(f"Is Laptop {this.id} functional? --> {'Yes' if this.functional else 'No'}")
        
    def TurnOn(this):
        return (f"{f'Laptop {this.id} turned on' if this.functional else f'Cannot turn on laptop {this.id}, it is not operational'}")
    
    def TurnOff(this):
        return (f"{f'Laptop {this.id} turned off' if this.functional else f'Does nothing, laptop {this.id} not operational'}")
        
PrintLongLine()

# Laptop 1 Properties
Laptop1 = NewLaptop(1, "Acer", "Gray", True)
Laptop1.PrintProperties()
PrintLongLine()

# Laptop 2 Properties
Laptop2 = NewLaptop(2, "Lenovo", "Black", False)
Laptop2.PrintProperties()
PrintLongLine()

# Laptop 3 Properties
Laptop3 = NewLaptop(3, "Toshiba", "Blue", True)
Laptop3.PrintProperties()
PrintLongLine()

# Laptop 4 Properties
Laptop4 = NewLaptop(4, "HP", "Red", True)
Laptop4.PrintProperties()
PrintLongLine()

# Let's turn on all the laptops
print(Laptop1.TurnOn())
print(Laptop2.TurnOn())
print(Laptop3.TurnOn())
print(Laptop4.TurnOn())
PrintLongLine()

# Let's turn off all the laptops
print(Laptop1.TurnOff())
print(Laptop2.TurnOff())
print(Laptop3.TurnOff())
print(Laptop4.TurnOff())
PrintLongLine()