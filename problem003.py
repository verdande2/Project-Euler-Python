##Problem 3
##The prime factors of 13195 are 5, 7, 13 and 29.
##
##What is the largest prime factor of the number 600851475143 ?

## Notes:
## 

from timeit import default_timer as timer
from math import sqrt



# start timer
start = timer()

primes = set([2])
value = 3
number = 600851475143
factors = []
while value < sqrt(number):
    isPrime = True
    for k in primes:
        if value % k == 0:
            isPrime = False
            value += 2
    if isPrime:
        primes.add(value)
        if number % value == 0:
            #print(str(value))
            factors.append(value)
            number = int(number/value)
factors.append(number) # final number is also factor

print(max(factors))

end = timer()
print("Runtime: ",str(end-start)," s",sep="")
