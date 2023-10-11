import time, math
from common import sumDigits




start = time.time()
count = 0
for i in range(0,10**18+1):
    if i%(10**6)==0:
        print (i,count,str(time.time()-start))
    if sumDigits(i) == sumDigits(137*i):
        count += 1 
    
end = time.time()
print("found in",str(end-start),"Answer is",str(count))


