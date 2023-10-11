import time
from common import *
from itertools import permutations

def isRelativelyPrime(a,b):
    if isPrime(a) and isPrime(b): return True
    _a = getDivisors(a)
    _b = getDivisors(b)
    return _a&_b == set([1])

def phi(n):
    count = 0
    for a in range(1,n):
        if isRelativelyPrime(a,n):
            count += 1
    return count

def isPermutation(a,b):
    a = str(a)
    b = str(b)
    if len(a) != len(b): return False
    for perm in permutations(a):
        perm = "".join(perm)
        if perm == b: return True
    return False
    

start = time.time()
lowest_np=10**100
for n in range(10**7-1,1,-1):
#for n in range(1,10**7):
    #if isPrime(n): continue
    p = phi(n)
    np = n/p
    print(str(n),str(p),str(np))
    if np<lowest_np:
        if isPermutation(n,p):
            print("after",str(time.time()-start),"new lowest n/phi from n =",str(n),str(p),str(n/p))
            lowest_np = n/p


print(str(time.time()-start),"seconds")
print("answer is",str(n))

isPermutation(12345,54321)
