codage = list(input("message à codé (en majuscule!) : "))
nmbr_c = int(input("rentré une valeur de clé de codage"))

if nmbr_c <0:
    nmbr_c = -(nmbr_c)
    #just in case
liste_alphall =["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ""]*nmbr_c
liste_alpha = liste_alphall

crypt = []
crypt2 = []
for i in codage:
    if i in liste_alpha:
        crypt.append(liste_alpha.index(i))

for ii in crypt:
    crypt2.append(liste_alpha[int(ii) + nmbr_c])   

string = "".join(crypt2)

print("votre message crypté est :",string) 
