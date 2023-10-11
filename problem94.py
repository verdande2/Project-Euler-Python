import time

hcf = lambda n1, n2: n1 if n2 == 0 else hcf( n2, n1 % n2 )
coprime = lambda n1, n2: True if hcf(n1, n2) == 1 else False        

##It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

##We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

##Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).

start = time.time()


u = 1
v = 0

max_p = 10**9

sumtotal = 0

while True:
    while True:
        #print("checking",str(u),str(v),u>v)
        
        a = 2*(u**2 - v**2)
        b = u**2 + v**2
        c = b

        p = 4*u**2

        
        if(coprime(u,v)): ## condition for heronian isosceles triangle (integral sides/area)
            #print("triangle ",str(a),str(b),str(c))
            if(a-b == 1 or b-a == 1): ## condition for "almost equilateral"
                print("match found!",str(b), "odd side: ",str(a),"perimeter: ",str(p))
                sumtotal += p
        if(p > max_p):
            break;
        u = u+1

    v = v+1 # increment v
    u = v+1 # make u 1 more than v, so that u>v always

    # recalculate perim from new values
    p = 4*u**2
    if(p > max_p):
        break;


end = time.time()
print("found in",str(end-start),"Answer is",str(sumtotal))
