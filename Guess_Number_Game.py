import random

# Number of tries
guess_try = 1

# Random number
rand = random.randint(1,10)

print("Guess a number between 1 - 10:")
while True:
    guess = int(input("-> "))
    if guess == rand:
        print("Congratulations, your guess is correct! ")
        break
    else:
        if guess_try >= 3:
            print(f"The correct number is {rand}")
            break
        else:    
            print("Sorry, try again")    
            guess_try += 1