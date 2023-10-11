import time, itertools
from common import *

start = time.time()
cumSum = 0
results = []
for i in range(1,100000):
    string = str(i)
    
    if "0" in string or hasDuplicateDigits(i):
        #print(str(i)+" has dupe digits or a zero")
        continue

    availableDigitsMultiplicand = ""
    for x in range(1,10):
        if not str(x) in string:
            availableDigitsMultiplicand += str(x)

    #print(availableDigitsMultiplicand)
    
    #print("product="+printString)
    for z in range(1,9-len(string)):
        
        for x in itertools.permutations(availableDigitsMultiplicand,z):
            x="".join(x)
            #print(x+" = "+str(z)+" "+str(9-len(string)+1)+" "+str(9-len(string)-z))

            availableDigitsMultiplier = ""
            for y in range(1,10):
                if not str(y) in x and not str(y) in string:
                    availableDigitsMultiplier += str(y)
            #print(x + " * " + availableDigitsMultiplier)
            for y in itertools.permutations(availableDigitsMultiplier,9-len(string)-z):
                y = "".join(y)
                #print("test")

                #print(y)
                #print(str(x)+" * "+str(y)+" = "+str(i))
                if int(x) * int(y) == int(i) and not i in results:
                    print(str(x)+" * "+str(y)+" = "+str(i))
                    cumSum += int(i)
                    results.append(i)
    
                    
print("Sum",str(cumSum),"finished in ",time.time() - start,"seconds.")

    
