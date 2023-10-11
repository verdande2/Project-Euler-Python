import itertools
import math, time
ti = time.time()

def hunt(m):
    
    return [digits for digits, count in m.items() if count == 5]

f = open('prob62.txt', 'w')

# set up a dict with key being sorted string of digits of each cube
d = dict()

n = 1
while True:

    n3 = n**3
    s = str(n3)
    s = ''.join(sorted(s))
    
    f.write("trying "+str(n)+"^3 = "+str(n3)+' digits: '+s)
    f.write("\n")
    print("trying",str(n),"^3 =",str(n3), 'digits: ',s)


    if s in d:
        d[s] = d[s] + 1
    else:
        d[s] = 1

    n = n+1

    a = hunt(d)
    if len(a)>0:
        break

f.close()
  
print(str(a))
print("Time taken(secs):", time.time() - ti)
