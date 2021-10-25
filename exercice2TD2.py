codage = list(input("message à codé (en majuscule!) : "))
mot_cle = list(input("rentré votre mot clé:"))

liste_alphall =["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",]*2
liste_alpha = liste_alphall

mot_cle_nmbr = []
for i in mot_cle:
    if i in liste_alpha:
        mot_cle_nmbr.append(liste_alpha.index(i))

match_dico_motc = dict(zip(codage,mot_cle_nmbr))
print(match_dico_motc)
value_mdm =[]
for value in match_dico_motc.values():
    value_mdm.append(value)
print(value_mdm)


crypt = []
crypt2 = []
for i in codage:
    if i in liste_alpha:
        crypt.append(liste_alpha.index(i))

for ind in value_mdm: 
        valeur_ind = ind
        print(valeur_ind)

for ii in crypt:
    for ind in value_mdm: 
        valeur_ind = ind
        print(valeur_ind)
    crypt2.append(liste_alpha[int(ii) + valeur_ind[ii]]) 
    print(ii)
    print(valeur_ind)
    print(crypt2)
string = "".join(crypt2)

print("votre message crypté est :",string) 

print(crypt)
print(crypt2)

