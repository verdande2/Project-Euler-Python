import time, math

start_t = time.time()

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

def find_consec_square_chain(n, debug=False):
    start = 1
    debug and print("finding consecutive square chain for",str(n))
    while True:

        chain = []
        c = start
        s = 0
        debug and print("trying new chain starting at",str(c))
        if c**2 > n:
            debug and print("c^2 is greater than n!")
            return 0
        while s < n:
            debug and print("s =",str(s),"< n =",str(n))
            chain.append(c)
            debug and print('adding',str(c),'^2')
            s += c**2
            c += 1
        if s==n:
            debug and print('sum s=',str(s),' n = ',str(n))
            return chain
        start += 1
    
max_digits = 8

ans = []
for digits in range(1,max_digits+1):
    #print("digits:",str(digits))
    div = digits/2
    f = math.ceil(div)
    # for digits = 1
    # f = 0
    # n loops from 10^0 =1 to 10^1 = 10 (strictly less than)
    # for digits = 2
    # f = 1
    # n loops from 10^1 to 10^2 ie. 10-99

    #print("looping from",str(int(10**(f-1))),"to",str(int(10**(f))))
    for n in range(int(10**(f-1)), int(10**(f))):
        if div == f:
            #even
            # generate f digits and mirror them
            #print("even")
            s = str(n)+str(n)[::-1]
        else:
            #odd
            # generate f digits and mirror
            #print("odd")
            s = str(n)+str(n)[:-1][::-1]
        #print("n",str(n),"generated:",s)
        a = find_consec_square_chain(int(s))
        if a!=0:
            if a not in ans:
                print("found:",s)
                ans.append(a)

agg = 0
for t in ans:
    if len(t) < 2:
        continue
    n = sum([int(a**2) for a in t])
    agg += n
    print('[%s]' % ', '.join(map(str, t)))
    print("number:",str(n))
    

#find_consec_square_chain(595)

end = time.time()
print("found in",str(end-start_t),"Answer is",str(agg))

