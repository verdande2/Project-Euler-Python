.from __future__ import division

def factor(num):
    """factors a composite number to a permutation of its primes"""
    primeList = {} # for temporary storage of the counts of each prime
    factorList = {} # return array 
    
    for x in range(2,num):
        if isPrime(x)==1:
            
            primeList[x]=0
            
    sortedprimeList = primeList.keys()
    sortedprimeList.sort()
    sortedprimeList.reverse()
    print("after primelist has been compiled")

    temp = num
    while temp!=1:
        
        for x in sortedprimeList:

            if temp%x==0:

                primeList[x]+=1
                temp /= x
                break

    print("after factoring has been complete")
    for x in primeList.keys():
        if primeList[x]!=0:
            factorList[x]=primeList[x]

    print("after factoring sort/clean up, return")
    return factorList
        
def isPrime(num):
    for x in range(2,int(pow(num, .5)+1.0)):
        if num%x == 0:
            return 0
    return 1



print("start")   
x = factor(600851475143)
maximum_prime = 0
for y in x.keys():
    if y>maximum_prime:
        maximum_prime=y
print ("max prime is "+str(maximum_prime))
