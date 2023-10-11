import time
from math import floor

def numGen(startingNum=1):
    num = startingNum
    while True:
        yield num
        num += 1

def fiftyfifty(t):
    d = t*(t-1)
    #print()
    a = (2+(4 + 8*t**2 + -8*t)**(1/2))/4
    #b = (2+(4 + 8*a)**(1/2))/4
    for n in range(floor(a),t**2):
        #print("n:",str(n),"2*n*(n-1)",str(2*n*(n-1)),"d:",str(d),"(2*n*(n-1))/d",str((2*n*(n-1))/d))
        if 2*n*(n-1)== d:
            return a
        elif 2*n*(n-1)> d:
            break
    return 0
start = time.time()

#for n in numGen():
for n in numGen(10**12):
    #break
    #if n%10**9==0: print(str(n))
    x = fiftyfifty(n)
    if x!=0:
        answer = x
        print("found in",str(time.time()-start),"Answer is",str(answer))
        #break

answer=fiftyfifty(21)
end = time.time()
print("found in",str(end-start),"Answer is",str(answer))


