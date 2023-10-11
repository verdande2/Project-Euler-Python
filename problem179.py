import time, math
from common import getDivisors




start = time.time()
count = 0
for i in range(2,10**7):
    if i%10**5==0: print(i)
    a = len(getDivisors(i))
    b = len(getDivisors(i+1))
    if a == b:
        count += 1
    
end = time.time()
print("found in",str(end-start),"Answer is",str(count))


