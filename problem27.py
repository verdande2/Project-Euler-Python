import time
from common import *

start = time.time()

max_consecutive_primes = [0, 0, 0]
for a in range(-999,1001):
    for b in range(-999,1001):
        n = 0
        while isPrime(n**2 + a * n + b):
            if n > max_consecutive_primes[2]:
                max_consecutive_primes = [a, b, n]
            n+=1
        
        
        
end = time.time()
print("n**2 + "+str(max_consecutive_primes[0])+"*n + "+str(max_consecutive_primes[1])+" generates primes for n =[0,"+str(max_consecutive_primes[2])+"]. Found in",str(end-start),"seconds.")
print("Answer is",str(max_consecutive_primes[0]*max_consecutive_primes[1]))            
