import time, math

start = time.time()

def hcf( n1, n2 ):
  while n1*n2:
    if n1 > n2:
      n1 %= n2
    else:
      n2 %= n1
  return max( n1, n2 )

def coprime( n1, n2 ):
  return hcf( n1, n2 ) == 1

prim_list = []

n = 1
while True:
    m = n+1
    
    first = True
    while True:
        a = m**2-n**2
        b = 2*m*n
        c = m**2+n**2
        
        if a+b+c >= 100000000:
            break
        if coprime(n,m) and (m-n)%2 == 1:
            if c%(b-a) == 0:
                prim_list.append((a, b, c))
                print("found primitive:",str(a),str(b),str(c))
                print("and it satisfies criteria!")
        first = False   
        
        m +=1
    if first:
        break
    n += 1
    
agg = 0
for tri in prim_list:
    p = tri[0] + tri[1] + tri[2]
    agg += math.floor(100000000/p)
    
print("found in",str(time.time()-start),"ans:",str(agg))


