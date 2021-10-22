import random

bombe = random.randint(0,100)
tentative = input("tentez votre chance! Proposez un entier de 0 à 100 : ")
count=0
i = int(tentative)-int(bombe)

while i > 10 or i < -10:
    if count < 4:
        count += 1
        test = 5 - count
        tentative = input(f"Raté retentez votre chance! Attention il ne vous reste plus que {test} tentatives : ")
    elif count == 4:
        print("Game Over!")
        break
if i <= 10 and i >= -10:
    print(f"Bravo vous avez trouvé la bombre en {count} tentatives")
