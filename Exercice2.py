liste_entier = []
entier = input("Rentrez un nombre entier : ")
while entier != "fin":
    if entier.isnumeric() == False:
        entier = input("Ceci n'est pas un entier, vueillez rentrer un nombre entier ou tapper fin pour mettre fin à la selection : ")
        
    elif entier.isnumeric() == True:
        liste_entier.append(entier)
        print(liste_entier)
        entier = input("Voulez vous rajouter un entier? si oui rentré votre nombre, sinon tapper fin : ")
    
    elif entier == "fin":
        quit

print("Voici votre liste: ",liste_entier)

liste_unique =[]
count = 0
for d in liste_entier:
    if d not in liste_unique:
        liste_unique.append(d)
    elif d in liste_unique:
        count += 1
print(f"Il y avait {count} doublons")
print("Liste sans les doublons : ",liste_unique)