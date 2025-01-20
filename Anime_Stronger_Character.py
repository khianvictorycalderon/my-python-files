Naruto = int(input(" Enter Naruto strength: "))
Luffy = int(input(" Enter Luffy strength: "))
Saitama = int(input(" Enter Saitama strength: "))

if Naruto > Luffy and Naruto > Saitama:
    print(" Naruto is strongest")
elif Luffy > Naruto and Luffy > Saitama:
    print(" Luffy is the strongest")    
elif Saitama > Naruto and Saitama > Luffy:
    print(" Saitama is the strongest")
else:
    print(" There is a tie")    