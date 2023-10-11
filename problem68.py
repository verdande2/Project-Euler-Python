import time, itertools

start = time.time()


solutionSets = []
#c=0
for p in itertools.permutations([1,2,3,4,5,6,7,8,9,10],10):
    #print(str(p))
    a = []
    a.append((p[5],p[0],p[1]))
    a.append((p[6],p[1],p[2]))
    a.append((p[7],p[2],p[3]))
    a.append((p[8],p[3],p[4]))
    a.append((p[9],p[4],p[0]))
    if sum(a[0]) == sum(a[1]) == sum(a[2]) == sum(a[3]) == sum(a[4]):
        # they all sum to same number, find lowest and shift so a[0][0] is lowest
        lowest = min([a[0][0],a[1][0],a[2][0],a[3][0],a[4][0]])
        while a[0][0]!=lowest:
            temp = [a[1],a[2],a[3],a[4],a[0]]
            a = temp
        if not a in solutionSets:
            solutionSets.append(a)
            #print("Found a solution: "+str(a[0])+str(a[1])+str(a[2])+str(a[3])+str(a[4]),str(time.time()-start))
    #c+=1
    #if c%10**5==0:
        #print(c,p,str(time.time()-start))
        
#print("found all solutions. Concatting strings and finding max value. "+str(time.time()-start))
values = []   
for i in solutionSets:
    concat = ""
    for s in i:
        concat+=str(s[0])
        concat+=str(s[1])
        concat+=str(s[2])
        # check if it is 16 digits
        if len(str(int(concat)))==16:
            values.append(int(concat))
    #print(i,concat,sum(i[0]))


print("Answer is",str(max(values)))
print("Time taken(secs):", time.time() - start) 
