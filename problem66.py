import time
from math import floor



start = time.time()

max_x = 0
max_d = 0
d=2
d_max = 1000


while d<=d_max:
    if d in [z**2 for z in range(2,50000)]:
        d+=1
        continue
    x=0
    y=1

    print('testing d=',d)
    # while it isn't solved
    while x**2 - d*y**2 != 1:
        x+=1
        y=floor(((x**2-1)/d)**(1/2))
        if y==0: y=1
        while d*y**2+1 < x**2:
            if x**2 - d*y**2 == 1:
                break
            y+=1
        if x>10**7 and y>10**7:
            break
    if x>10**7 and y>10**7:
        print('for d=',d,'numbers both exceeded 10^7, failed to find solution')
        
    else:
        print(x,' ',d,' ',y)
        if x>max_x:
            max_x=x
            max_d=d
    d+=1
        
        




end = time.time()
print("found in",str(end-start),"Answer is",str(max_d))
