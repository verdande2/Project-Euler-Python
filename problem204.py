import time, math

start_t = time.time()

import common
from itertools import islice
 
def hamming100():
    '''\
    This version is based on a snippet from:
        http://dobbscodetalk.com/index.php?option=com_content&task=view&id=913&Itemid=85
 
        When expressed in some imaginary pseudo-C with automatic
        unlimited storage allocation and BIGNUM arithmetics, it can be
        expressed as:
            hamming = h where
              array h;
              n=0; h[0]=1; i=0; j=0; k=0;
              x2=2*h[ i ]; x3=3*h[j]; x5=5*h[k];
              repeat:
                h[++n] = min(x2,x3,x5);
                if (x2==h[n]) { x2=2*h[++i]; }
                if (x3==h[n]) { x3=3*h[++j]; }
                if (x5==h[n]) { x5=5*h[++k]; } 
    '''
    h = 1
    _h=[h]    # memoized
    multipliers  = (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97)
    multindeces  = [0 for i in multipliers] # index into _h for multipliers
    multvalues   = [x * _h[i] for x,i in zip(multipliers, multindeces)]
    yield h
    while True:
        h = min(multvalues)
        _h.append(h)
        for (n,(v,x,i)) in enumerate(zip(multvalues, multipliers, multindeces)):
            if v == h:
                i += 1
                multindeces[n] = i
                multvalues[n]  = x * _h[i]
        # cap the memoization
        mini = min(multindeces)
        if mini >= 1000:
            del _h[:mini]
            multindeces = [i - mini for i in multindeces]
        #
        yield h

def isHammingNumber(n, h=5):
    p = common.getPrimeFactors(n)
    for i in p:
        if i>h:
            return False
    return True

##n = 1 # including 1
##for i in range(2,10**9):
##    if isHammingNumber(i):
##        n+=1

##for i in common.eratosthenes():
##    if i>100:
##        break
##    print(str(i))

c = 0
for h in hamming100():
    if h > 10**9:
        break
    c += 1
    #print(str(h))

end = time.time()
#print("found in",str(end-start_t),"Answer is",str(agg))

