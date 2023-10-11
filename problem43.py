import time, itertools

start = time.time()
cumSum = 0
numList = []
for i in itertools.permutations("0123456789"):
    string = "".join(i)
    if int(string[1:4])%2==0 and int(string[2:5])%3==0 and int(string[3:6])%5==0 and int(string[4:7])%7==0 and int(string[5:8])%11==0 and int(string[6:9])%13==0 and int(string[7:10])%17==0:
        cumSum += int(string)
        numList.append(string)
        
end = time.time()
print("found in",str(end-start),"Answer is",str(cumSum))
