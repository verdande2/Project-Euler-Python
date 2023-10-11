def gen_triangle():
    n = 2
    t = 1
    while 1:
	yield t
	t = t + n
	n += 1
 
def divisors(n):
    divisors = set([1])
    for i in range(1, math.ceil(n ** 0.5)+1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n/i)
    return divisors
 
start = time.time()
while 1:
    num = t.next()
    #print num
    if len(divisors(num)) > 500:
        print 'BINGO', num
        break
end = time.time()
print 'time taken',end-start
