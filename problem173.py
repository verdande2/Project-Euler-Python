import time, math

start = time.time()

def squares_needed(o,i):
    # outer side length
    # inner side length
    if (o%2 != i%2):
        raise Exception('odd/even do not match!')
    return o**2-i**2

o = 3
c = 0
while True:
    i = o%2 # start at 1 for odd, 0 for even outer side lengths
    ran = False
    for i in range(o-2, 0, -2):
        s = squares_needed(o,i)
        if s > 1000000:
            break
        else:
            ran = True
            #print("found:",str(o),str(i), str(s))

        c += 1
    o += 1
    if not ran:
        break

print("found in",str(time.time()-start),"ans:",str(c))


