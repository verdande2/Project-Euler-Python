def find_factor(n) :
    for i in range(2, int(n**0.5 + 1)+1) :
        if n % i == 0 :
            return i
    return n
 
def find_factors(n) :
    factors = []
    while n != 1 :
        fac = find_factor(n)
        if fac not in factors :
            factors.append(fac)
        n /= fac
    return factors
 
maximum = 0.0
for n in range(2, 1000000+1) :
    factors = find_factors(n)
    dividend = n
    divisor = 1
    for factor in factors :
        dividend *= factor - 1
        divisor  *= factor
 
    totient = dividend / divisor
    ratio = float(n) / float(totient)
    if  maximum < ratio :
        maximum = ratio
        print(n, ratio, factors)
