import time, math

start = time.time()

def u(n):
    return 1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10
    
for n in range(0,11):
    print('u_' + str(n) + ' => ' + str(u(n)))

# this problem boils down to writing a n-degree best fit line solver, and then using each fit line to find the first incorrect term predicted by each fit line    
end = time.time()
print("found in",str(end-start),"Answer is",str(num_hits))
