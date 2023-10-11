import time

start = time.time()

def R(L,W):
    r=0
    for l in range(1, L+1):
        for w in range(1, W+1):
            r += (W+1-w)*(L+1-l)
    return r
            
n = 2 * 10**6
record_del = 10000
record_area = 0

for l in range(1,100):
    for w in range(1,100):
        r = R(l,w)
        if abs(r-n) < record_del:
            record_del = abs(r-n)
            record_area = l*w
            print("new record del: ",str(record_del),"area:",str(record_area))

end = time.time()
print("found in",str(end-start),"Answer is")
