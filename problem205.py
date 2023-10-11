import time, math, re

start = time.time()

import itertools



cr = itertools.combinations_with_replacement(range(1,7), 6)

##for i in pr:
##    s = sum(i)
##    print(str(i[0]), str(i[1]), str(s))
##    

total = 0
win = 0 
for c in cr:
    sum_to_beat = sum(c)
    for p in itertools.combinations_with_replacement(range(1,5), 9):
        s = sum(p)
        if s > sum_to_beat:
            win += 1
        total += 1

print(str(win), str(total))
##ans = 0
##total = 0
##for p in pr:
##    for c in cr:
##        if sum(p)>sum(c):
##            ans += 1
##        total += 1
##ans /= total
##    
##end = time.time()
##print("found in",str(end-start),"Answer is",str(ans))
##

