from common import * 

def fib():
    """returns the fibonacci series up to a max value of num"""
    a = 1
    b = 1
    yield {"i":1,"num":a} # cheap fix for forcing F1 and F2 = 1
    yield {"i":2,"num":b}
    c = a + b

    i = 3
    while True:
        c = a + b
        yield {"i":i,"num":c}
        a=b
        b=c
        i+=1

for n in fib():
    print(str(n["i"])+": "+str(n["num"])+" has "+str(countDigits(n["num"]))+" digits.")
    if countDigits(n["num"])>=1000:
        answer = n["num"]
        break

#print(str(answer))
