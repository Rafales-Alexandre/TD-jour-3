codage = list(input("message à codé (en majuscule!) : "))
mot_cle = list(input("rentré votre mot clé:"))

dict_mot_cle = {"A" : "1","B" : "2", "C" : "3", "D" : "4", "E" : "5", "F" : "6", "G" : "7", "H" : "8", "I" : "9", "J" : "10", "K" : "11", "L" : "12", "M" : "13", "N" : "14", "O" : "15", "P" : "16", "Q" : "17", "R" : "18", "S" : "19", "T" : "20", "U" : "21", "V" : "22", "W" : "23", "X" : "24", "Y" : "25", "Z" : "26", " "  : "27"}
liste_alpha = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ""]
nmbr = []
nmbr_c = sum(nmbr)
codage_liste =[]
for c in codage:
    if c in liste_alpha:
        codage_liste.append(c)

for d in codage_liste:
    nmbr.append(dict_mot_cle.get(d))
print(nmbr)
print(codage_liste)
liste_alphall =["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ""]*nmbr_c
liste_alphaa = liste_alphall
crypt = []
crypt2 = []

for i in codage:
    if i in liste_alphaa:
        crypt.append(liste_alphaa.index(i))

for ii in crypt:
    crypt2.append(liste_alphaa[int(ii) + nmbr_c])   

string = "".join(crypt2)

print("votre message crypté est :",string) 
