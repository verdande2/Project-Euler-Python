import time, math

def f(frac):
    n = frac[0]
    d = frac[1]
    return (n+2*d,n+d)

def numDigits(i): return len(str(i))

start = time.time()
count = 0
frac = (1,1)
for i in range(1,1000+1):
    frac = f((frac))
    if numDigits(frac[0]) > numDigits(frac[1]):
        count+=1
end = time.time()
print("found in",str(end-start),"Answer is",str(count))


