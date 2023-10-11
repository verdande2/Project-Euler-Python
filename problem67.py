import time

def displayTriangle(tri):
    l = len(tri)
    s = 0
    for row in tri:
        s+=1
        spacing = " "*((l-s)*3)
        data = ""
        for thing in row:
            data += str('%02d'%thing).center(6)


        print(spacing+data)

start = time.time()
# test data
file = []
file.append("03")
file.append("07 04")
file.append("02 04 06")
file.append("08 05 09 03")

file = open('problem67_files/triangle.txt', 'r')
triangle = [] # contains the actual triangle
for line in file:
    line = line.split(" ")
    num_array = []
    for i in line:
        num_array.append(int(i))
    triangle.append(num_array)
# triangle is loaded with correct data
triangle.reverse()



##for row in triangle:
##    print(row)

for r in range(len(triangle)-1,-1,-1):
    for c in range(0,len(triangle[r])-1):
        #print(triangle[r][c])
        triangle[r-1][c] += max(triangle[r][c],triangle[r][c+1])

end = time.time()
print("found in",str(end-start),"Answer is",str())
displayTriangle(triangle)
