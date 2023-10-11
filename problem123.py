import time
from common import genPrimes





start = time.time()
n=1
for p in genPrimes(10**100):
    remainder = ((p-1)**n + (p+1)**n)%(p**2)
    if remainder > 10**10:
        break
    n+=1 

end = time.time()
print("found in",str(end-start),"Answer is",str(n))
