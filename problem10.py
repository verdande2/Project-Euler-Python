def isPrime(num):
    z = int(pow(num, .5)+1.0)
    for x in range(2,z):
        if num%x == 0:
            return False
    return True

sum_of_primes = 0
for i in range(2,2000000):
    if isPrime(i):
        sum_of_primes+=i
print("The sum of all primes under 2000000 is "+str(sum_of_primes))
