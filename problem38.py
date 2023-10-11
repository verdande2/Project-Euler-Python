from common import *
import time

start = time.time()
max_pandigital = 0
for i in range(1,1000001):
    string = ""
    n = 1
    while len(string) < 9:
        string += str(i * n)
        n+=1
    if len(string) != 9 or not isPandigital(string):
        continue
    else:
        if int(string) > max_pandigital:
            max_pandigital = int(string)
end = time.time()
print("found in",str(end-start),"Answer is",str(max_pandigital))
