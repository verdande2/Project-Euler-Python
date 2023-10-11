import time, itertools
from common import *

start = time.time()
answer_set = {}
for a in genPrimes(10000):
    if a<=999:
        continue
    perm_list = []
    
    for perm in itertools.permutations(str(a)):
        perm = "".join(perm)
        perm = int(perm)
        if not perm in perm_list:
            perm_list.append(perm)
    perm_list.sort()

    for x in range(0,len(perm_list)):
        for y in range(x,len(perm_list)):
            if isPrime(perm_list[x]) and isPrime(perm_list[y]) and x!=y:
                diff = perm_list[y] - perm_list[x]
                if perm_list[y] + diff in perm_list and isPrime(perm_list[y] + diff) and perm_list[y]+diff>perm_list[y]>perm_list[x]>=1000:
                    print(str(perm_list[x])+" "+str(perm_list[y])+" "+str(perm_list[y]+diff)+" increasing by "+str(diff))
                    answer_set[perm_list[x]] = (perm_list[x], perm_list[y], perm_list[y] + diff)

print("done.")
