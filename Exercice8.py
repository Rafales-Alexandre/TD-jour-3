import random

nmbr_vote = 20
participants = ["Ashe", "Morty", "Squall", "Neo", "Lara"]
vote = ["Pas bien", "Assez bien", "Bien", "Tres bien", "Excelent"]
liste = []

for part in participants:
    for vot in vote:
        if vot != "Pas bien" and vot != "Assez bien":
            liste.append(f"{part} {vot}")

scrutin = []

while len(scrutin) < int(nmbr_vote):
    select = random.choice(liste)
    scrutin.append(select)

result = {}
result["Morty"] = 0
for m in scrutin:
    if m == "Morty Excelent" or m =="Morty Tres bien" or m =="Morty Bien":
        result["Morty"] += 1
result["Ashe"] = 0
for m in scrutin:
    if m == "Ashe Excelent" or m =="Ashe Tres bien" or m =="Ashe Bien":
        result["Ashe"] += 1
result["Squall"] = 0
for m in scrutin:
    if m == "Squall Excelent" or m =="Squall Tres bien" or m =="Squall Bien":
        result["Squall"] += 1
result["Neo"] = 0
for m in scrutin:
    if m == "Neo Excelent" or m =="Neo Tres bien" or m =="Neo Bien":
        result["Neo"] += 1
result["Lara"] = 0
for m in scrutin:
    if m == "Lara Excelent" or m =="Lara Tres bien" or m =="Lara Bien":
        result["Lara"] += 1

dict = {}
 
for value in result.values():
       dict[value] = []
 
for (key,value) in result.items():
        dict[value].append(key)

maxVote = sorted(dict.keys(),reverse=True)[0]
new_dict = {}

for k, v in result.items():
    if v == maxVote:
      new_dict[k] = v  

result2 = {}
key1 = list(new_dict.keys())[0]
if len(new_dict) > 1:
    key2 = list(new_dict.keys())[1]
elif len(new_dict) > 2:
    key3 = list(new_dict.keys())[2]
elif len(new_dict) > 3:
    key4 = list(new_dict.keys())[3]
elif len(new_dict) > 4:
    key5 = list(new_dict.keys())[4]

if len(new_dict) >1 :
    result2[key1] = 0
    for m in scrutin:
        if m == key1+" Excelent": 
            result2[key1] += 1
    result2[key2] = 0
    for m in scrutin:
        if m == key2+" Excelent":
            result2[key2] += 1

elif len(new_dict) >2:  
    result2[key1] = 0
    for m in scrutin:
        if m == key1+" Excelent": 
            result2[key1] += 1
    result2[key2] = 0
    for m in scrutin:
        if m == key2+" Excelent":
            result2[key2] += 1 
    result2[key3] = 0
    for m in scrutin:
        if m == key3+" Excelent":
            result2[key3] += 1

elif len(new_dict) >3:  
    result2[key1] = 0
    for m in scrutin:
        if m == key1+" Excelent": 
            result2[key1] += 1
    result2[key2] = 0
    for m in scrutin:
        if m == key2+" Excelent":
            result2[key2] += 1 
    result2[key3] = 0
    for m in scrutin:
        if m == key3+" Excelent":
            result2[key3] += 1
    for m in scrutin:
        if m == key4+" Excelent":
            result2[key4] += 1

elif len(new_dict) >4:  
    result2[key1] = 0
    for m in scrutin:
        if m == key1+" Excelent": 
            result2[key1] += 1
    result2[key2] = 0
    for m in scrutin:
        if m == key2+" Excelent":
            result2[key2] += 1 
    result2[key3] = 0
    for m in scrutin:
        if m == key3+" Excelent":
            result2[key3] += 1
    for m in scrutin:
        if m == key4+" Excelent":
            result2[key4] += 1
    for m in scrutin:
        if m == key5+" Excelent":
            result2[key5] += 1
else:
    print(key1, "à gagné les élections!")

res=0
for k,v in result2.items():
    if v > res:
        res = v
        key = k
        print (f"{key} à gagné les élections avec une égalité!")
