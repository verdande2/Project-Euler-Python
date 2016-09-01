##Problem 75

## Notes:
## 

from timeit import default_timer as timer

def rprime(a,b):
    while b: #b != 0
        a,b = b, a%b
    return a == 1

def get_triplet(m,n,k=1):
    if m<=n:
        print("m cannot be <= n")
        return
    elif not rprime(m,n):
        print("m and n are not coprime. a primitive will not be generated")
        return
    else:
        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2

        t = [a,b,c]
        t = k*t # scale the primitive if needed
        return sort(t)        


# start timer
start = timer()


m = 0
n = 0

perimeter_max = 1.5 * 10**6


# looping through m,n 


end = timer()
print("Runtime: ",str(end-start)," s",sep="")
