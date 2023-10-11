import time



start = time.time()
count = 0
temp = start
for i in range(1,16**16):
    if i%10000000==0: print(time.time()-start,i,100*i/16**16)
    h = hex(i)[2:]
    if not "f" in h:
        continue
    if not "0" in h:
        continue
    if not "1" in h:
        continue
    count += 1
    

end = time.time()
print("found in",str(end-start),"Answer is",str(count))

