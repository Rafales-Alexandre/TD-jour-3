import random

bombe = random.randint(0,100)
print(bombe)
tentative = input("Tentez votre chance! Proposez un entier de 0 à 100 : ")
count=1
i = int(tentative)-int(bombe)
print(i)

while i > 10 or i < -10:
    while count < 5:
        count += 1
        test = 6 - count
        tentative = input(f"Raté retentez votre chance! Attention il ne vous reste plus que {test} tentatives : ")
        i = int(tentative)-int(bombe)
        if i <= 10 and i >= -10:
            break
    if count == 5:
        print("Game Over!")
        break
    
        
if i <= 10 and i >= -10:
    print(f"Bravo vous avez trouvé la bombre en {count} tentatives")
