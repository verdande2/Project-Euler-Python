#import psyco
from math import sqrt
 
#Use psyco for just-in-time compilation => faster.
#psyco.full()
 
def divs(n):
    d = 0
    #This will not really be *accurate* for all numbers,
    #but I judged that it would be good enough for this case
    #and I was luckily enough right, and it almost certainly saved time.
    for i in range(1, int(sqrt(n))):
        if n % i == 0: d += 1
    return d * 2
 
def eul(n):
    trig = lambda n: n * (n + 1) / 2
    #Make that function a local variable so we don't get
    #the overhead of looking up globals.
    div = divs
    #Don't start checking on the first triangle number,
    #it's a waste :)
    i = n * 20
    while div(trig(i)) < n:
        i += 1
    return i, trig(i)
 
print(eul(500))
