Cars = ["Toyota", "BMW", "Mercedes-Benz", "Ford", "Honda", "Tesla", "Audi", "Chevrolet"]
C_Prices = [1000, 2000, 1500, 1200, 3000, 1200, 4000, 3500]
C_Colors = ["Red", "Red", "Blue", "Yellow", "Black", "Blue", "Green", "Black"]

def getInput():
    for item in range(8):
        ui = input("\nCar List:\nToyota\nBMW\nMercedes-Benz\nFord\nHonda\nTesla\nAudi\nChevrolet\n\nChoose a Car from the above list:\n")
        
        if ui in Cars:
            index = Cars.index(ui)
            print(f"\nCar Found! Here are the details:")
            print(f"Car Name  : {Cars[index]}")
            print(f"Car Price : ${C_Prices[index]}")
            print(f"Car Color : {C_Colors[index]}\n")
            print("Thank you for exploring our car series!")
            print(f"At {Cars[index]}, we drive innovation and excellence!")
            break
        else:
            print("Car not found. Please choose from the list.")

getInput()