import time, math

       

##It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

##We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

##Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).

start = time.time()



max_p = 10**9

sumtotal = 0

print("Trying triangles of form n x n x n+1")
for a in range(1, math.ceil(max_p/3+1)):
    sp = (a+a+(a+1))/2
    area = (sp*(sp-a)*(sp-a)*(sp-(a+1)))**(1/2)
    if math.floor(area) == area:
        ## integral area
        #print("match found!",str(a),str(a),str(a+1),"perimeter: ",str(2*sp))
        sumtotal += 2*sp
        
print("Trying triangles of form n x n x n-1")
for a in range(1, math.ceil(max_p/3+1)):
    sp = (a+a+(a-1))/2
    area = (sp*(sp-a)*(sp-a)*(sp-(a-1)))**(1/2)
    if math.floor(area) == area:
        ## integral area
        #print("match found!",str(a),str(a),str(a-1),"perimeter: ",str(2*sp))
        sumtotal += 2*sp
        

end = time.time()
print("found in",str(end-start),"Answer is",str(sumtotal))
