import time
from common import getDivisors

def isRelativelyPrime(a,b):
    _a = getDivisors(a)
    _b = getDivisors(b)
    return _a&_b == set([1])

def phi(n):
    count = 0
    for a in range(1,n):
        if isRelativelyPrime(a,n):
            count += 1
    return count


start = time.time()
maxnphi = (0,0)
for n in range(1000000,2300,-1):
    phi_val = phi(n)
    ratio = n/phi_val
    if ratio > maxnphi[1]:
        maxnphi=(n,ratio)
        print("A new max n/phi(n) has been found:",str(ratio)," from n =",str(n))

end = time.time()
print("found in",str(end-start),"Answer is",str(maxnphi[0]))
