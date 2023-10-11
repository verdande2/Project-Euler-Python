import time
from common import isPrime

start = time.time()


n_max = 100000
nums_to_generate = (n_max-1)*2+1

step = 0

total_primes = 0
total_nums = 0


num = 1
for i in range(-1,nums_to_generate-1):
    step = 2*((i+4)//4)
    #print("i: "+str(i)+" step: "+str(step))
    num = num + step
    total_nums += 1
    n = (total_nums-1)/2+1
    if isPrime(num) and num!=1:
        total_primes += 1
    if total_primes/total_nums < .1 and total_primes>0 and total_nums>0:
        answer = n
        break
    
    #print(str(num))

print("Answer is",str(answer))
print("Time taken(secs):", time.time() - start)    
