def factorial(num):
    f=1
    while num!=1:
        #print("factorial is currently: "+str(f)+" and num: "+str(num))
        f*=num
        num-=1

    return f

sum_of_digits = 0
test = str(factorial(100))
for a in test:
    sum_of_digits+=int(a)
print(str(sum_of_digits))
