import time, math

def solveTheProblem(r):
    # first, find some key points
    halfR = int(r / 2)
    fourthR = int(r / 4)

    count = 0
    lowcount = 0
    uppcount = 0
    tricount = 0
    points = []

    for x in range(- r, r + 1):
        for y in range(- r, r + 1):
            if abs(y) + abs(x) <= r:
                # it's a valid point, now check where the point is
                if y==x:
                    # fail
                    continue
                elif y >= 0 and x <= fourthR and x > y:
                    # in the little triangle area, not including hypoteneuse
                    #print('Testing x: ' + str(x) + ', y: ' + str(y))
                    if not (x == fourthR and y == 0):
                        tricount += 2 # doubled because this is only checking on the lower right triangle
                        #print('x: ' + str(x) + ', y: ' + str(y))
                        #points.append((x,y))
                elif y >= -x and y <= -x + halfR:
                    # in the dead zone
                    continue
                elif y > -x + halfR and y <= -x + r:
                    # upper area
                    uppcount += 1
                    #points.append((x,y))
                elif y < -x and y >=-x - r:
                    # lower area
                    lowcount += 1
                    #points.append((x,y))
                #print('.')
    return (lowcount, uppcount, tricount)#count #(count, points)
                

start = time.time()

def testAnswer(r):
    return int(3/2 * r**2 + tri(r))

def tri(r):
    t = 0
    for i in range(1,int(r/4)):
        t += 2+2*i
    return t

for n in [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]:
    answer = solveTheProblem(n)
    print(n,": ",str(answer), sum(answer), testAnswer(n))



answer = testAnswer(1000000000)

end = time.time()
print("found in",str(end-start),"Answer is",str(answer))


