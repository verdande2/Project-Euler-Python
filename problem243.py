import time, math

start = time.time()

def gcd(n, m):
    while n>0:
        t = n
        n = m % n
        m = t
    return m

def reduceable(n,d):
    g = gcd(n,d)
    return g!=1

def resilience(d):
    c = 0
    for i in range(1,d):
        if gcd(d,i)==1:
            c+=1
    return (c,d-1)

def frac_cmp(a, b):
    l = a[0]*b[1]
    r = a[1]*b[0]
    if l > r:
        return 1
    elif l == r:
        return 0
    elif l < r:
        return -1


import fractions

def phi(n):
    amount = 0

    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1

    return amount

def resil2(d):
    t = phi(d)
    return (t, d-1)

n = 25500
found = False
while not found:
    if frac_cmp(resil2(n), (15499,94744)) == -1:
        found = True
        break
    n += 1
#print("found in",str(time.time()-start),"ans:",str(agg))


