total = 300
nmbr_fléchette = 10
fléchette = [0,20,50] #a,b,c

for a in range(0,nmbr_fléchette+1):
    for b in range(0,nmbr_fléchette+1):
        for c in range(0,nmbr_fléchette+1):
            if a + b + c == 10 and 0*a + 20*b + 50*c == total:
                print(a,b,c)