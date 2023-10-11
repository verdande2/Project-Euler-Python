import math, itertools

# number tests
def isPalindrome(num):
    temp = str(num)
    if temp[::-1] == temp:
        return True
    else:
        return False

def isPrime(num):
    if num==1 or num==0 or num<0: return False
    z = int(pow(num, .5)+1.0)
    for x in range(2,z):
        if num%x == 0:
            return False
    return True

def isTriangleNum(num):
    i=1
    while True:
        t = int(i*(i+1)/2)
        if num == t:
            return True
        elif t>num:
            return False
        i+=1

def isPentagonalNum(num):
    i=1
    while True:
        p = int(i*(3*i-1)/2)
        if num == p:
            return True
        elif p>num:
            return False
        i+=1

def isHexagonalNum(num):
    i=1
    while True:
        h = int(i*(2*i-1))
        if num == h:
            return True
        elif h>num:
            return False
        i+=1

def isPandigital(num):
    a=list(str(num))
    a.sort()
    if a==list("123456789"):
        return True
    return False 

def hasDuplicateDigits(num):
    digitCount = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    hasDuplicateDigits = False
    string = str(num)
    for char in string:
        char = int(char)
        digitCount[char]+=1
    
    for k in digitCount.keys():
        if digitCount[k]>1:
            hasDuplicateDigits = True
            break
    return hasDuplicateDigits
    

def sumDigits(num):
    string = str(num)
    s = 0
    for digit in string:
        s += int(digit)
    return s

def countDigits(num):
    string = str(num)
    return len(string)


def getDivisors(n):
    d = set([1])
    for i in range(1, math.ceil(n ** 0.5)+1):
        if n % i == 0:
            d.add(i)
            d.add(int(n/i))
    return d

def getProperDivisors(n):
    d = set([1])
    for i in range(1, math.ceil(n ** 0.5)+1):
        if n % i == 0:
            d.add(i)
            d.add(int(n/i))
    d-=set([n])
    return d

def getPrimeFactors(n):
    d = getProperDivisors(n)
    r = getProperDivisors(n)
    for num in d:
        if not isPrime(num):
            r -= set([num])
    return r

# generators section
def genTri(yield_index=False):
    i=1
    while True:
        t = int(1/2*i*(i+1))
        if yield_index:
            yield i,t
        else:
            yield t
        i+=1
        
def genPent(yield_index=False):
    i=1
    while True:
        p = int(i*(3*i-1)/2)
        if yield_index:
            yield i,p
        else:
            yield p
        i+=1
        
def genHex(yield_index=False):
    i=1
    while True:
        h = int(i*(2*i-1))
        if yield_index:
            yield i,h
        else:
            yield h
        i+=1
        
def genPrimes(n=1000000000000000): # 1,000 trillion
    yield 2
    primes = []
    for m in range(3,n,2):
        if all(m%p for p in primes):
            primes.append(m)
            yield m





def isDeficientNum(n):
    d = getProperDivisors(n)
    s = sum(d)
    return s<n
def isPerfectNum(n):
    d = getProperDivisors(n)
    s = sum(d)
    return s==n
def isAbundantNum(n):
    d = getProperDivisors(n)
    s = sum(d)
    return s>n


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
