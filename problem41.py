import time, itertools
from common import *

start = time.time()
string = "123456789"
max_pandigital_prime = 0
for i in range(0,10):
    for perm in itertools.permutations(string[:i+1]):
        perm = "".join(perm)
        num = int(perm)
        if isPrime(num) and num>max_pandigital_prime:
            max_pandigital_prime = num
            
            
end = time.time()
print("max pandigital prime is "+str(max_pandigital_prime)+"solved in",str(end-start),"seconds.")
