def factorial(num):
    if num==0:
        return 1
    f=1
    while num!=1:
        #print("factorial is currently: "+str(f)+" and num: "+str(num))
        f*=num
        num-=1

    return f

def nCr(n,r):
    return (factorial(n))/(factorial(r)*factorial(n-r))

count = 0
for n in range(1,101):
    print("trying n: "+str(n))
    for r in range(1,n+1):
        print("trying r: "+str(r))
        ncr = nCr(n,r)
        if ncr > 1000000.0:
            count +=1
print(str(count))
