from common import *
import time

start = time.time()

max_pentagonal_number = 10000000


lowest_d=1000000000000
for a in genPent():
    for b in genPent():
        #print("a: "+str(a)+" b: "+str(b)+" sum: "+str(a+b)+" diff: "+str(max(a,b)-min(a,b)),"sum is pentagonal:",str(isPentagonalNum(a+b)),"diff is pentagonal:",str(isPentagonalNum(max(a,b)-min(a,b))))
        if isPentagonalNum(a+b) and isPentagonalNum(max(a,b)-min(a,b)):


            
            d = abs(a-b)
            print("a: "+str(a)+" b: "+str(b)+" d: "+str(d))
            if d<lowest_d:
                lowest_d = d
                
        if b > max_pentagonal_number:
            break;
    
    if a > max_pentagonal_number:
        break;
end = time.time()
print("found in",str(end-start),"Answer is",str(lowest_d))
