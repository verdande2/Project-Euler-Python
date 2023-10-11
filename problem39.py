import time, math
from common import *

start = time.time()

solutionDict = {}
for p in range(1,1001):
    solutions = []
    for a in range(1,p+1):
        for b in range(1,p-a+1):
            c = p - a - b
            if a**2 + b**2 == c**2 and not [b,a,c] in solutions:
                solutions.append([a,b,c])
    solutionDict[p] = [len(solutions), solutions]
m = 0
for k in solutionDict.keys():
    if solutionDict[k][0] > m:
        m = solutionDict[k][0]
        finalSolution = k
print("Answer is",str(finalSolution))
print("Time taken(secs):", time.time() - start)    
