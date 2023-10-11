import time
from common import isPrime
from itertools import permutations


def numInPrimeFamily(n):
    if not "*" in n:
        if isPrime(int(n)):
            return 1
        else:
            return 0
    prime_count = 0
    for i in range(0,10):
        test = n.replace("*",str(i))
        if isPrime(int(test)) and test[0]!="0": prime_count += 1

    return prime_count


start = time.time()
answer = ""
for digits in range(2,13):
    wildcards = digits-1
    print("digits:",digits,"wildcards:",wildcards,time.time()-start)
    for i in permutations("1234567890"+wildcards*"*",digits):
        i = "".join(i)
        #print(i,numInPrimeFamily(i))
        if numInPrimeFamily(i) == 8 :
            print(i)
            answer = i
            break


    
    if answer!="": break


end = time.time()
print("found in",str(end-start),"Answer is",str(answer))
