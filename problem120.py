import time, math

def remainderMax(a,n=10000):
    maxRemainder = 0
    for i in range(1,n+1):
        remainder = ((a-1)**i + (a+1)**i)%(a**2)
        #print(str(a-1)+"**"+str(i)+" + "+str(a+1)+"**"+str(i)+" % "+str(a**2)+" = "+str(remainder))
        
        if remainder > maxRemainder:
            maxRemainder = remainder
    return maxRemainder

start = time.time()
sumMaxRemainders = 0

for i in range(3,1000+1):
    print(str(math.floor(i/10)),"percent done and we are",str(time.time()-start),"seconds in, currently on i="+str(i))
    sumMaxRemainders += remainderMax(i)
    
end = time.time()
print("found in",str(end-start),"Answer is",str(sumMaxRemainders))


