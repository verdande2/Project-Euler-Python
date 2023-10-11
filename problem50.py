import time, math

start = time.time()


import itertools
def eratosthenes( ):
    '''Yields the sequence of prime numbers via the Sieve of Eratosthenes.'''
    D = {  }  # map each composite integer to its first-found prime factor
    for q in itertools.count(2):     # q gets 2, 3, 4, 5, ... ad infinitum
        p = D.pop(q, None)
        if p is None:
            # q not a key in D, so q is prime, therefore, yield it
            yield q
            # mark q squared as not-prime (with q as first-found prime factor)
            D[q*q] = q
        else:
            # let x <- smallest (N*p)+q which wasn't yet known to be composite
            # we just learned x is composite, with p first-found prime factor,
            # since p is the first-found prime factor of q -- find and mark it
            x = p + q
            while x in D:
                x += p
            D[x] = p

def sieve(limit):
    limit = limit+1
    primes = dict();
    for i in range(2, limit): primes[i] = True

    for i in primes:
        factors = range(i, limit, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]



record_prime_sum = 0
record_prime_start = 0
record_combo = 0

max_num = 10**6

# sieve all primes less than max
p = sieve(max_num)

plen = len(p)

# loop over each prime, starting from smallest to largest
index = 0

while index < plen:
    #print("starting at",p[index])
    combo = 1
    s = p[index]
    print(str(s))
    while s < max_num:
        # increase combo length
        combo = combo + 1

        if index+combo-1 >= plen:
            break
        
        # add next consecutive prime to partial sum
        s = s + p[index + combo - 1]
        
        if s > max_num:
            break
        if s in p and combo > record_combo:
            print(str(s))
            record_combo = combo
            record_prime_sum = s
            record_prime_start = p[index]
            continue
    index = index + 1



end = time.time()
print("found in",str(end-start),"Answer is",str(record_prime_sum))
