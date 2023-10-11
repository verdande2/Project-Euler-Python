import time, math

def isIncreasingNum(n):
    n = str(n)
    val = 0
    IncNum = True
    for char in n:
        if int(char) < val:
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
            DecNum = False
            break
        val = int(char)
    return DecNum

def isBouncyNum(n):
    return (not isIncreasingNum(n)) and (not isDecreasingNum(n))



start = time.time()
bouncyCount = 0
totalCount = 100
n=100
while True:
    if isBouncyNum(n):
        bouncyCount += 1
        if n>10**9:
            print(str(n),": ",str(bouncyCount/totalCount))
        
    totalCount += 1
        
    if bouncyCount/totalCount*100.00 == 99.0:
        break
    n+=1
    

    
end = time.time()
print("found in",str(end-start),"Answer is",str(n))

