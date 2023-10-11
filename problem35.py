def isPrime(num):
    z = int(pow(num, .5)+1.0)
    for x in range(2,z):
        if num%x == 0:
            return False
    return True

def isCircularPrime(num):
    string = str(num)
    isCircularPrime = True
    
    for x in range(len(string)):
        circ = ""
        for y in range(len(string)-1):
             circ += string[y+1]
        circ += string[0]
        #print(circ)
        string = circ
        if not isPrime(int(string)):
            isCircularPrime = False
            break
    return isCircularPrime

count = 0
for i in range(2,1000000):
    if isCircularPrime(i):
        count += 1
        print(str(i))
print("count : "+str(count))
