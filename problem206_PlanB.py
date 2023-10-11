import time, math, re

start = time.time()
regPattern = re.compile("1\d2\d\3\d4\d5\d6\d7\d8\d9\d0")

for a in range(0,10):
    print("a loop",str(a),str(time.time()-start),"seconds in")
    for b in range(0,10):
        print("b loop",str(b),str(time.time()-start),"seconds in")
        for c in range(0,10):
            print(str(int(math.floor((a*100+b*10+c)/10)))+" percent done. c loop",str(c),str(time.time()-start),"seconds in")
            for d in range(0,10):
                for e in range(0,10):
                    for f in range(0,10):
                        for g in range(0,10):
                            for h in range(0,10):
                                for i in range(0,10):
                                    num = int("1"+str(a)+"2"+str(b)+"3"+str(c)+"4"+str(d)+"5"+str(e)+"6"+str(f)+"7"+str(g)+"8"+str(h)+"9"+str(i)+"0")
                                    if num**(1/2) == math.floor(num**(1/2)):
                                        answer = num**(1/2)
                                        break
    
    
    
end = time.time()
print("found in",str(end-start),"Answer is",str(answer))


