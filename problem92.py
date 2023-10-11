import time


def sumSquaredDigits(n):
    s = 0
    string = str(n)
    for char in string:
        s += int(char)**2
    return s

start = time.time()
count = 0
for i in range(1,10000000):
    temp = i
    while True:
        if sumSquaredDigits(temp)==1 or sumSquaredDigits(temp)==89:
            if sumSquaredDigits(temp)==89:
                count+=1
            break
        temp = sumSquaredDigits(temp)
        
end = time.time()
print("found in",str(end-start),"Answer is",str(count))
