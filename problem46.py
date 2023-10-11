from common import *
import time


start = time.time()
i = 2

while True:
    if isPrime(i) or i%2==0:
        i += 1
        continue
    foundSolution = False
    for p in genPrimes():
        if p > i: break
        s = 1
        while p + 2 * s**2 < i:
            s += 1
        if p + 2 * s**2 == i:
            #print(str(p),"+","2*"+str(s)+"**2 = ",str(i))
            foundSolution = True
            break
    if not foundSolution:
        break
    i += 1    
            
    
end = time.time()
print("found in",str(end-start),"Answer is",str(i))
