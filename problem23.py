import time, math
from common import *

start = time.time()


cumSum = 0
abundantNums = []
for i in range(1,28124):
    if isAbundantNum(i):
        abundantNums.append(i)

abundantNumSums = set([])

for a in abundantNums:
    for b in abundantNums:
        if a+b<=28123:
            abundantNumSums |= set([a+b])

for x in range(1,28124):
    if x not in abundantNumSums:
        cumSum += x
        
print("Answer is",str(cumSum))
print("Time taken(secs):", time.time() - start)    
