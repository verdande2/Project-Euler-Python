import time, math, itertools
from common import *

def isConcatablePrimeSet(s):
    ConcatPrimeSet = True
    for perm in itertools.permutations(s,2):
        n1 = str(perm[0])
        n2 = str(perm[1])
        if not isPrime(int(n1+n2)):
            ConcatPrimeSet = False
            break
    return ConcatPrimeSet
        
        
        
start = time.time()
found = False
testSet=[0,0,0,0,0]
n = 10000
for n1 in genPrimes(n):
    if found: break
    print("n1 changing: "+str(n1)+" after",str(time.time()-start),"seconds.")
    for n2 in genPrimes(n):
        if found: break
        print("n2 changing: "+str(n2)+" after",str(time.time()-start),"seconds.")
        for n3 in genPrimes(n):
            if found: break
            print("n3 changing: "+str(n3)+" after",str(time.time()-start),"seconds.")
            for n4 in genPrimes(n):
                if found: break
                for n5 in genPrimes(n):
                    if found: break
                    testSet = [n1,n2,n3,n4,n5]
                    if isConcatablePrimeSet(testSet):
                        found = True
                        break

end = time.time()
print("found in",str(end-start),"Answer is",str(testSet))

