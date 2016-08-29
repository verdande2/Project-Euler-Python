##Problem 1
##If we list all the natural numbers below 10 that are multiples of 3 or 5,
##we get 3, 5, 6 and 9. The sum of these multiples is 23.
##
##Find the sum of all the multiples of 3 or 5 below 1000.

## Notes:
## See http://stackoverflow.com/questions/12106989/digital-sum-python for
## information about digitalSum function

## First method uses typical naive looping over each number and determining divisibility
## Second method calculates multiples for each number and performs much better

from timeit import default_timer as timer

# digitalSum computes the sum of the digits of the number passed to it
def digitalSum(n):
    if n < 10 :
        return n
    return n % 10 + digitalSum( n // 10 )

def divisibleByThree(n):
    return digitalSum(n)%3==0

def divisibleByFive(n):
    return n%10 in [0,5]

# start timer
start = timer()

acc = 0
# can safely skip 1, 2 because we're hunting multiple of 3 or 5
for n in range(3, 1000):
    if divisibleByFive(n) or divisibleByThree(n):
        acc += n
    
print(str(acc))
end = timer()
print("Runtime: ",str(end-start)," s",sep="")



# start timer
start = timer()

acc = 0
# compute multiples of 5
n = 5
while n<1000:
    if not divisibleByThree(n):
        acc += n
    n+=5
# compute multiples of 3
n = 3
while n<1000:
    acc+=n
    n+=3
    
print(str(acc))
end = timer()
print("Runtime: ",str(end-start)," s",sep="")
