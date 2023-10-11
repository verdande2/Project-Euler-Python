import time, math
from common import *

start = time.time()

string = ""
i = 1
d=[]
while len(string) < 1000001:
    string += str(i)
    i += 1
d.append(int(string[0]))
d.append(int(string[9]))
d.append(int(string[99]))
d.append(int(string[999]))
d.append(int(string[9999]))
d.append(int(string[99999]))
d.append(int(string[999999]))


product = 1
for a in d:
    product *= a

    

        
print("Answer is",str(product))
print("Time taken(secs):", time.time() - start)    
