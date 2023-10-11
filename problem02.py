0def fib(num):
    """returns the fibonacci series up to a max value of num"""
    a = [1,2]
    while(a[-1]+a[-2]<num):
        a.append(a[-1]+a[-2])
    return a

def isEven(num):
    return num%2==0

total = 0
for x in fib(4000000):
    if isEven(x):
        total+=x
print total
