import time
from math import floor

colors = {"red":2,"green":3,"blue":4}
letters = {"red":"R","green":"G","blue":"B"}
def possiblePositions(color, length):
    unit = colors[color]
    char = letters[color]
    blank = "_"
    pp = []
    if length == unit:
        pp.append(char*5)
    if unit > length:
        return 0
    max_blocks = floor(length/unit)
    for number_of_blocks in range(0,max_blocks):
        # fail right here
        for i in range(0,length-unit+1):
            pp.append(blank*i+char*unit+blank*(length-unit-i))
            
    return pp
        


start = time.time()
count = 0 
length = 5

##count += possiblePositions("red",length)
##print(str(count))
##count += possiblePositions("green",length)
##print(str(count))
##count += possiblePositions("blue",length)
##print(str(count))

end = time.time()
print("found in",str(end-start),"Answer is",str(count))

r = possiblePositions("red",5)
g = possiblePositions("green",5)
b = possiblePositions("blue",5)
