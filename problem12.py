from common import *
import time

# generates triangle numbers, default max is the first 1 million
def triangle(num=1000000):
    s=0
    x=1
    while True:
        s+=x
        yield s
        x+=1

def countDivisors(num):
    count = len(getDivisors(num))
    return count


start = time.time()
#highest_count = 0
for t in triangle():
    #print(str(t))
    c = countDivisors(t)
    if c > 500:
        break
    #elif c > highest_count:
        #print(str(t)+" has new high count "+str(c))
        #highest_count = c
end = time.time()  
print(str(t)+" found in",end-start,"seconds.")
