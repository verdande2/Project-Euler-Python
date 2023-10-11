import time

start = time.time()


n = 1001
nums_to_generate = (n-1)*2+1

step = 0

cumSum = 0
num = 1
for i in range(-1,nums_to_generate-1):
    step = 2*((i+4)//4)
    #print("i: "+str(i)+" step: "+str(step))
    num = num + step
    cumSum += num
    #print(str(num))

print("Answer is",str(cumSum))
print("Time taken(secs):", time.time() - start)    
