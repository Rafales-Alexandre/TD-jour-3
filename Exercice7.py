def anagrammes(mot):
    liste = [mot]
    for i in range(1, len(mot)):
        liste.append(mot[i] + mot[1:i] + mot[0] + mot[i + 1:])
 
    if len(mot) > 2:
        for mot in list(liste):
            liste += [mot[0] + x for x in anagrammes(mot[1:])][1:]  
    return liste
 
print(anagrammes(str(input())))