print()
over = False

def getInput():
    num = int(input(" Enter a positive number: "))
    fac = 1
    if num > 0:
        print(f" {num}! = {num} ",end="")
        fac *= num
        for x in range(num-1,0,-1):
            fac *= x
            print(f"* {x} ",end="")
        print()    
        print(f" {num}! = {fac}")   
        print()        
        ask = input(" Continue? Type 'yes'\n ")
        print()
        if ask.lower() == "yes":
            getInput()
        else:
            print(" Thank you for using.")
    else:
        print(" Input must be a positive.")
        
getInput()