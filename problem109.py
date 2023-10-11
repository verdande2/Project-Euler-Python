import itertools
import time

start = time.time()

def evaluate(g):
    hits = g.split(' ')
    s = 0
    for hit in hits:
        if hit[0]=='S':
            mult = 1
        elif hit[0]=='D':
            mult = 2
        elif hit[0]=='T':
            mult = 3
        value = int(hit[1:])
        s += value * mult
    return s

ways = 0

spots = []
for d in ['S','D','T']:
    for i in range(1,21):
        spots.append(d+str(i))
spots.append('D25')
spots.append('S25')
        
games = []
for i in itertools.combinations_with_replacement(spots, 2):
    c = " ".join(i)
    for n in range(1,21):
        d = c+" D"+str(n)
        
        games.append(d)
    d = c+" D25"
    games.append(d)
    
for i in itertools.combinations_with_replacement(spots, 1):
    c = " ".join(i)
    for n in range(1,21):
        d = c+" D"+str(n)
        
        games.append(d)
    d = c+" D25"
    games.append(d)
    
for n in range(1,21):
    d = "D"+str(n)
    
    games.append(d)
d = c+" D25"
games.append(d)


ways = 0
for g in games:
    if evaluate(g) < 100:
        ways += 1

        

print("Time taken(secs):", time.time() - start)
