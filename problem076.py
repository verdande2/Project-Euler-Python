##Problem 76
##It is possible to write five as a sum in exactly six different ways:
##
##4 + 1
##3 + 2
##3 + 1 + 1
##2 + 2 + 1
##2 + 1 + 1 + 1
##1 + 1 + 1 + 1 + 1
##
##How many different ways can one hundred be written as a sum of at least two
##positive integers?
## Notes:
##  This is essentially a partition problem, but the only difference between p(100)
##  and the answer is that the answer is the number of ways to sum TWO positive
##  integers, so we remove the single case of 100 as a way to partition 100,
##  and our answer becomes p(100)-1

from timeit import default_timer as timer

# generates the sequence of alternating sign integers:
# 0, 1, -1, 2, -2, 3, -3, 4, -4 ...
def gen_alternating_sign_integers(lim=10**12):
    n = 0
    while n<=lim:
        yield n
        if n>0:
            n = -n
        elif n<0:
            n = -n
            n += 1
        else:
            # n == 0
            n+=1

def generalized_pentagonal_number(lim=10**12):
    x = 0
    for n in gen_alternating_sign_integers(lim):

        # calculate new value of x
        x = int((3*n**2-n)/2)
        if x>lim:
            break
        else:
            yield x
            

cache = {}

def p(n):
    global cache
    
    if n==0:
        return 1
    elif n<0:
        return 0
    elif n in cache:
        return cache[n]
    else:
        s_total = 0
        for m in gen_alternating_sign_integers():
            sign = (-1)**(abs(m)-1)
            
            offset = int((3*m**2-m)/2)

            # if offset is zero, we don't want to infinitely recurse, so skip that case
            if offset == 0:
                continue
            
            index = n-offset
            
            # if the index of p is negative, we've gone too far
            if index<0:
                break
            else:
                s_total += sign * p(index)
                
        cache[n]=s_total
        return s_total
    
# start timer
start = timer()

i = 100
partitions = p(i)
print("p(",i,")=",partitions)

print("number of ways to sum 2+ pos ints to 100? a:",partitions-1)

end = timer()
print("Runtime: ",str(end-start)," s",sep="")
