import time, math


start = time.time()
count = 0
i = 1
while True:
    digits = len(str(i))
    if math.floor(i**(1/digits)) == i**(1/digits):
        count += 1
        print(str(time.time()-start),"seconds in.",str(count),": ",str(i)," = ",str(i**(1/digits))+"**"+str(digits))
    
    i+=1
end = time.time()
print("found in",str(end-start),"Answer is",str(count))


