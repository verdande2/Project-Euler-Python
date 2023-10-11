import math, time
from common import *

debug = False

# function returns sum of divisors
def d(n):
    return sum(getProperDivisors(n))

def findAmicablePair(a):
    if d(d(a)) == a and a != d(a):
        ret = (a,d(a))
        if debug: print("amicable pair: ",ret)
    else:
        ret = (0,0)
        
    return ret

start = time.time()
amicableSet = set()

#note for future reference, 1 is not an amicable number.
for x in range(2,10000):
    aPair = findAmicablePair(x)
    #print(aPair)
    if aPair[0]<10000 and not aPair[0] in amicableSet:
        amicableSet |= set([aPair[0]])
    if aPair[1]<10000 and not aPair[1] in amicableSet:
        amicableSet |= set([aPair[1]])
##for i in amicableSet:
##    print(str(i))
cumSum = sum(amicableSet)
end = time.time()  
print(str(cumSum)+" found in",end-start,"seconds.")

