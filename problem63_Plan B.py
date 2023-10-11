import time, math

start = time.time()
count = 0
for b in range(1,100):
    for e in range(1,100):
        digits = len(str(b**e))
        if e==digits:
            count += 1
            print(str(time.time()-start),"seconds in.",str(count),": ",str(b**e)," = ",str(b)+"**"+str(e))
    
end = time.time()
print("found in",str(end-start),"Answer is",str(count))


