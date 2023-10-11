import time


def isReversableNum(n):
    reverseN = int(str(n)[::-1])
    if str(n)[::-1][0:1]=="0": return False
    if allDigitsOdd(n+reverseN):
        return True
    else:
        return False

def allDigitsOdd(n):
    string = str(n)
    for char in string:
        if int(char) in [0,2,4,6,8]:
            return False
    return True

start = time.time()
count = 0
for i in range(1,10**9):
    if isReversableNum(i):
        #print(str(i))
        count+=1
        
end = time.time()
print("found in",str(end-start),"Answer is",str(count))
