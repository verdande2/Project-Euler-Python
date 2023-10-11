import time
from common import *

debug = False

def isTruncatablePrime(num):
    isTruncatablePrime = True
    num = str(num)
    
    #check from left first
    for i in range(0,len(num)):
        if debug: print("Checking primality of "+num[i:])
        if not isPrime(int(num[i:])):
            isTruncatablePrime = False
            break
        if debug: print("Checking primality of "+num[:i+1])
        if not isPrime(int(num[:i+1])):
            isTruncatablePrime = False
            break
    return isTruncatablePrime

start = time.time()
cumSum = 0
count = 0
x = 8
while True:
    if isTruncatablePrime(x):
        count += 1
        cumSum += x
        print(str(x)+" is a truncatable prime.")
        debug=False
        isTruncatablePrime(x)
        debug=False
    if count == 11:
        break
    x += 1
print(str(cumSum))
print("Time taken(secs):", time.time() - start)
