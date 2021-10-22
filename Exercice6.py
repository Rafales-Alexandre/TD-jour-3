cost = 2
dé_tétra = [1,2,3,4]
mise = 2
point = 0

for i in dé_tétra:
    for ii in dé_tétra:
        if i == ii:
            mise = mise - cost
            point = i + ii
        else:
            mise = mise + cost

print(mise)
print(point)

#Je ne jouerais pas à ce jeu car on ne recupère jamais d'argents, dans le meilleur des cas on ne perd rien et cela avec une probabilité tres faible!