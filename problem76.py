import time, itertools

indent = -4
def waysToSum(n):
    #global indent
    #indent+=4
    #whoami = "waysToSum("+str(n)+")"
    #print(indent*" ",whoami)
    
    if n == 1:
        #print(indent*" ",whoami,"exiting")
        #indent-=4
        return [1]
    solutions = []

    # add trivial solutions
    for a in range(2,n):
        temp = [a,n-a]
        temp.sort()
        if not temp in solutions:
            solutions.append(temp)

    # add nontrivial solutions
    for i in range(1,n):
        #print(indent*" ",whoami,"i",i)
        s=waysToSum(n-i)
        #print(indent*" ",whoami,"s",s)
        
        for w in s:
            temp = [i]
            #print(indent*" ",whoami,"temp is:",temp)
            #print(indent*" ",whoami,"w",w,type(w))
            if type(w) == type(3):
                #print(indent*" ",whoami,"single appending to temp:",w)
                temp.append(w)
            else:
                for e in w:
                    #print(indent*" ",whoami,"loop appending to temp:",e)
                    temp.append(e)
            temp.sort()
            #print(indent*" ",whoami,"temp is:",temp)
##            
##                
            if temp not in solutions:
                #print(indent*" ",whoami,"temp is being appended to solution set:",temp)
                solutions.append(temp)
            else:
                pass#print(indent*" ",whoami,"temp is already in solutionset:",temp)

    #print(indent*" ",whoami,"exiting")
    #indent-=4
    return solutions
start = time.time()

        
end = time.time()
print("found in",str(end-start),"Answer is",str(len(waysToSum(100))))
