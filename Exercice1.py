#1
liste_entier = []
entier = input("Rentrez un nombre entier : ")

while entier != "fin":
    if entier.isnumeric() == False:
        entier = input("Ceci n'est pas un entier, vueillez rentrer un nombre entier ou tapper fin pour mettre fin à la selection : ")
        
    elif entier.isnumeric() == True:
        liste_entier.append(entier)
        entier = input("Voulez vous rajouter un entier? si oui rentré votre nombre, sinon tapper fin : ")
    
    elif entier == "fin":
        quit

print("Voici votre liste: ",liste_entier)
#2

for ind in liste_entier:
    index = liste_entier.index(ind) 
    valeur_ind = ind
    print(f"Pour l'index {index} on à valeur {valeur_ind}")
    


#3
somme = 0
for i in liste_entier:
    somme = somme + int(i)
print("L'addition des entiers que vous venez de rentrer est égal à : ",somme)

#4
liste_x3 = []
for m in liste_entier:
    m3 = int(m) * 3
    liste_x3.append(m3)

print("La multiplication par 3 de chacun des entiers que vous venez de donner donne la liste suivante : ",liste_x3)

#5
max = 0
for maximum in liste_entier:
    if int(maximum) >= int(max):
        max = maximum
print("Votre valeur maximum est égal à : ",max)

#6
min = 0
for minimum in liste_entier:
    if int(minimum) <= int(min):
        min = minimum
print("Votre valeur minimum est égal à : ",min)

#7
nmbr_pair = 0
for pair in liste_entier:
    if int(pair)%2 == 0:
        nmbr_pair = nmbr_pair + 1
print(f"Vous avez {nmbr_pair} pairs dans votre liste")

#8
somme_impair = 0
for impair in liste_entier:
    if int(impair)%2 == 1:
        somme_impair = somme_impair + int(impair)
print("La somme de tous les nombres impairs est égal à : ",somme_impair)