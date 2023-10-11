from math import *
 
def product(l): return reduce(lambda a, b:a*b,l)
 
def cumsum(l):
        sum=1
        for x in l:
                sum+=x
                yield sum
 
table={1:{}}
def factors(n):
        if n in table:
                return table[n]
        for i in range(2,int(ceil(sqrt(n)))+1)+[n]:
                if n % i == 0:
                        k=factors(n/i)
                        d = factors(n/i).copy()
                        if i in d:
                                d[i]=d[i]+1
                        else:
                                d[i]=1
                        table[n]=d
                        return d
 
i=1
m=0
for t in cumsum(range(2,100000)):
        a=list(factors(t).values())
        i+=1
        a=product(map((lambda x:x+1),a))
        m=max(m,a)
        if a > 500:
                print i,t,a
                break
