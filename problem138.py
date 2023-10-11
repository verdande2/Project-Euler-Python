import time, math

start = time.time()

## b L
##found one: 16 17
##found one: 272 305
##found one: 4896 5473
##found one: 87840 98209

def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer: 
        return True
    else:
        return False

def isSpecialIsosceles(b, L):
    return abs(math.sqrt(L**2 - (b/2)**2) - b) == 1

# b must be even.

##for L in range(1,1000000,1):
##    for b in range(2,2*L-1,2):
##        if isSpecialIsosceles(b,L):
##            print("found one:",str(b),str(L))

#where 5/4 * b**2 + 1 +/- 2b is a perfect square


##b 16 L 17.0
##b 272 L 305.0
##b 4896 L 5473.0
##b 87840 L 98209.0
##b 1576240 L 1762289.0
##b 28284464 L 31622993.0
##b 239629832 L 267914296.0
##b 485936718 L 543293768.0
##b 492613776 L 550758944.0
##b 931811100 L 1041796480.0
##b 958519324 L 1071657184.0
##b 1151409762 L 1287315248.0
##found in 2319.444000005722

f = open("prob138.txt", 'w')
c=0
b=2
while True:
    #print("trying",str(b))
    L2 = 5/4*b**2 + 1 + 2*b
    nL2 = 5/4*b**2 + 1 - 2*b
    if is_square(L2):
        L = math.sqrt(L2)
        print("b",str(b),"L",str(L))
        c+=1
        f.write("b: "+str(b)+" L: "+str(L)+"\n")
    if is_square(nL2):
        L = math.sqrt(nL2)
        print("b",str(b),"L",str(L))
        c+=1
        f.write("b: "+str(b)+" L: "+str(L)+"\n")
    if c == 12:
        break
    b+=2
f.close()
        
end = time.time()
print("found in",str(end-start))


