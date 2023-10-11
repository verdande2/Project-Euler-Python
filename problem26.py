import time
from common import *
import decimal


start = time.time()

cycle = numLongestRecurring = 0
for i in range(1,1000):
    power = lam = 1
    tortoise = 1/i
    tortoiseRem = (1%i) *10
    hare = tortoise / i
    hareRem = (tortoiseRem % i) * 10
    while tortoise != hare or tortoiseRem != hareRem:
        if power == lam:
            tortoise = hare
            tortoiseRem = hareRem
            power *= 2
            lam = 0
        hare = hareRem / i
        hareRem = (hareRem % i) * 10
        lam += 1
    if lam > cycle:
        cycle = lam
        numLongestRecurring = i
    
    #print("1/"+str(i)+" = ")
##    c = findLongestRecurringCycle(frac)
##    if c > longest_cycle:
##        longest_cycle = c
##        answer = i
##    print(str(decimal.Decimal(1)/decimal.Decimal(i)))

        
        
end = time.time()
print("Found in",str(end-start),"seconds.")
print("Answer is",str(numLongestRecurring))            
