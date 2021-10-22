import random
value = random.randint(1,100)
count = 0
print('Proposer un nombre entre 1 et 100!')
guess = input("Votre valeur: ")

while guess != value:
    count += 1
    if guess.isnumeric():
        guess = int(guess)
    else:
        print("Ce n'est pas un nombre entier, veuillez entrer un nombre entier entre 1 et 100")
        guess = input()
        
    if int(guess) > int(value):
        print('Votre proposition est trop grande, retentez votre chance!')
        guess = input()

    elif int(guess) < int(value):
        print('Votre proposition est trop petite, retentez votre chance!')
        guess = input()
    continue

print(f'Bien joué {guess} était la valeur à trouver et vous l\'avez trouvé en {count} tentatives!')