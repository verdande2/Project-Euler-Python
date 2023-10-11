import time
import itertools
from common import sumDigits

def continued_e():
    yield 2
    n = 1
    while True:
        yield 1
        yield 2*n
        yield 1
        n = n+1
    

start = time.time()

#a = itertools.islice(continued_e, 0, 10)
con_num = 100

a = [];
for i in continued_e():
    a.append(i)
    if len(a) == con_num:
        break

h = [0, 1]
k = [1, 0]

for i in range(2,con_num+2):
    
    h.append(a[i-2]*h[i-1] + h[i-2])
    k.append(a[i-2]*k[i-1] + k[i-2])

end = time.time()
print("found in",str(end-start),"Answer is")
