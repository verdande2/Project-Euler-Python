import time, math

start = time.time()


i = 3
cumSum = 0
while True:
    string = str(i)
    facSum = 0
    for char in string:
        facSum += math.factorial(int(char))
    if facSum == i:
        cumSum += i
        print(str(cumSum))
    i+=1

print("Answer is",str(cumSum))
print("Time taken(secs):", time.time() - start)    
