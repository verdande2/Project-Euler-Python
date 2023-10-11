import time, math

class Point:
    pass


def areaOfTriangle(a, b, c):
    det1 = a.x * b.y + a.y * c.x + b.x * c.y
    det2 = b.y * c.x + a.y * b.x + a.x * c.y

    return abs(det1 - det2)/2
    
start = time.time()


file = open('problem102_files/triangles.txt', 'r')
line_number = 0
num_hits = 0

# origin point
o = Point()
o.x = 0
o.y = 0

for line in file:
    line_number += 1

    #print(line)
    a = Point()
    b = Point()
    c = Point()
    (a.x, a.y, b.x, b.y, c.x, c.y) = [int(tem) for tem in line.split(',')]

    # now we have our 3 points, the method used to
    # find if the origin is in the triangle is testing
    # the area of the triangle against the area of the 3
    # triangles formed by (A,B,O), (B,C,O), (A,C,O) where
    # O represents the origin

    if areaOfTriangle(a,b,o)+areaOfTriangle(b,c,o)+areaOfTriangle(a,c,o) == areaOfTriangle(a,b,c):
        num_hits = num_hits + 1
        print('HIT HIT HIT!')
    

end = time.time()
print("found in",str(end-start),"Answer is",str(num_hits))
