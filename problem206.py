import time, math, re

start = time.time()
regPattern = re.compile("1\d2\d\3\d4\d5\d6\d7\d8\d9\d0")

for n in range(100000000,1000000000):
    if regPattern.match(str(n**2)):
        answer = n
        break

    
end = time.time()
print("found in",str(end-start),"Answer is",str(answer))


