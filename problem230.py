import time, math

start = time.time()

sum_ans = 0

def d(a, b, n):
    aa = a
    bb = b
    while len(aa) < n:
        cc = aa+bb
        aa = bb
        bb = cc
    return aa[n-1]

def generateMoreD(a, b, n):
    ret = []
    ret.append(a)
    ret.append(b)
    while len(ret[end]):
        ret.append(a+b)
        

a = '1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
b = '8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196'

a='1415926535'
b='8979323846'
for n in range(0,17+1):
    num = 10**n * int(d(a, b, (127+19*n) * 7**n))
    
    print('Found s_' + str(n) + '...' + str(len(str(num))))
    sum_ans += num

end = time.time()
print("found in",str(end-start),"Answer is",str(sum_ans))
