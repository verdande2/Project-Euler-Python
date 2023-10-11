import time
from common import genPrimes

start = time.time()
temp = start
c=0
nums = set([])
n_max = 50000000 # 50 mil
for a in genPrimes():
    if a**4 > n_max: break
    for b in genPrimes():
        if a**4 + b**3 > n_max: break
        for c in genPrimes():
            
            val = a**4 + b**3 + c**2
            if time.time()-temp > 10:
                print(str(time.time()-start),a,b,c,val)
                temp = time.time()
            if val < n_max:
                nums |= set([val])
            else:
                break
    
c=len(nums)


end = time.time()
print("found in",str(end-start),"Answer is",str(c))
