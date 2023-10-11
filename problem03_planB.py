x = 600851475143
largest_prime_factor = 0

def isPrime(num):
    z = int(pow(num, .5)+1.0)
    for x in range(2,z):
        if num%x == 0:
            return False
    return True


z=pow(x,.5)
for i in range(2,int(z)):
    if isPrime(i) and x%i==0 and i>largest_prime_factor:
        largest_prime_factor = i

print(largest_prime_factor)
