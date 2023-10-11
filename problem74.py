import time
import math

    
def sum_of_fac_of_digits(n):
    s = 0
    while n != 0:
        r = n%10
        n = math.floor(n/10)
        s += math.factorial(r)
    return s

def determine_length(n):
    history = [n]

    while True:
        m = sum_of_fac_of_digits(n)
        if m not in history:
            history.append(m)
            n = m
        else:
            return len(history)

    
start = time.time()

count = 0

for n in range(1,10**6):
    if determine_length(n)==60:
        count += 1
        print("length 60:",str(n),"found! count:",str(count))

print(str(time.time()-start),"seconds")
print("answer is", str(count))
