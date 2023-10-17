import time, math
from common import getDivisors




start = time.time()
count = 0
for i in range(2,25):
    if len(getDivisors(i))==4:
        count += 1
        print(i)

end = time.time()
print("found in",str(end-start),"Answer is",str(count))


