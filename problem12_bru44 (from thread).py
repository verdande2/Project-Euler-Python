from math import *
a=7
b=0
c=0
while 1:
    c=a*(a+1)/2
    for i in range(1,sqrt(c)):
        if c%i==0:
            b+=1
            a+=1
        if b>250:
            break
        else:
            b=0
    print c 
