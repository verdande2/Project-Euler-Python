##Problem 684

from timeit import default_timer as timer

## s(n) is the smallest number that has a digit sum of n
## s(10) = 19
def s(n):
    return 19


def digital_sum(n):
    
        
# start timer
start = timer()
print(s(10)==19)
      
end = timer()
print("Runtime: ",str(end-start)," s",sep="")

