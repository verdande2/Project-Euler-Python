def isPrime(num):
    z = int(pow(num, .5)+1.0)
    for x in range(2,z):
        if num%x == 0:
            return False
    return True

i=1
count=2
found = False
while not found:
    if isPrime(count):
        if i==10001:
            answer = count
            found = True
        i+=1
    count+=1
print("The 10,001st prime is "+str(answer))
