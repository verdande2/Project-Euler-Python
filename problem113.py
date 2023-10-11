import time
from functools import reduce
import itertools

def isIncreasingNum(n):
    n = str(n)
    val = 0
    IncNum = True
    for char in n:
        if int(char) < val:
            return False
            IncNum = False
            break
        val = int(char)
    return IncNum
    
def isDecreasingNum(n):
    n = str(n)
    val = 10
    DecNum = True
    for char in n:
        if int(char) > val:
            return False
            DecNum = False
            break
        val = int(char)
    return DecNum

def isBouncyNum(n):
    if n<100:
        return False
    else:
        return int(str(n)[0:3]) in threeDigitBouncyNums

def ncr(n,r):
    return reduce(lambda a,b: a*(n-b)/(b+1),range(r),1)

start = time.time()
bouncy_count=0
threeDigitBouncyNums = []
for n in range(100,1000):
    if (not isIncreasingNum(n)) and (not isDecreasingNum(n)):    
        bouncy_count +=1
        threeDigitBouncyNums.append(n)


# find how many bouncy numbers are 3 digit
b_count = 0
for i in range(100,10**101):
    if i in [10**y for y in range(2,100)]:
        print("under",str(i)," has ",str(b_count),"bouncies. = ",str(i-b_count-1),"non bouncies")
    if isBouncyNum(i):
        #print(i)
        b_count +=1
print(str(b_count))

end = time.time()
print("found in",str(end-start),"Answer is",str(not_bouncy_count))
