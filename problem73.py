import time

def getFactors(n):
    d = []
    for i in range(1,n+1):
        if n%i==0:
            d.append(i)
    return d

def gcf(n1,n2):
    f1 = getFactors(n1)
    f2 = getFactors(n2)
    gcf = 1
    for a in f1:
        for b in f2:
            if a==b:
                if a > gcf:
                    gcf = a
    return gcf    
def reduceFraction(n, d):
    gcd = gcf(n,d)
    return (int(n/gcd), int(d/gcd))
    

start = time.time()
fracs = set([])
count = 0
for d in range(2,12000+1):
    if d%100==0: print(str(d),"after",str(time.time()-start),"seconds","count is: ",str(count))
    for n in range(1,d):
        rN, rD = reduceFraction(n,d)
        if 1/3 < rN/rD < 1/2 and not (rN,rD) in fracs:
            count += 1
        fracs |= set([(rN, rD)])

#sortedFracs = sorted(fracs,key=lambda f: f[2])
#for i in sortedFracs:
##    if 1/3 < i[2] < 1/2:
##        count += 1


print(str(time.time()-start),"seconds")
print("answer is",str(count))
