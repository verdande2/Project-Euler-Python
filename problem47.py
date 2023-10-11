from common import *
import time


start = time.time()
s =[0,0,0,0]
s[0]=set([2])
s[1]=set([5])
s[2]=set([2,3])
s[3]=set([7])
i = 1000
while True:
    s[3] = s[2]
    s[2] = s[1]
    s[1] = s[0]
    s[0] = getPrimeFactors(i)
    
    #print(s[0])
    if len(s[0]) == len(s[1]) == len(s[2]) == len(s[3]) == 4 :
        print(str(i)," and ",str(i-1)," and ",str(i-2)," and ",str(i-3))
        break
        
    # finish here, check for distinct primes

    i += 1
    
end = time.time()
print("found in",str(end-start),"Answer is",str(i-3))
