import time



start = time.time()
# test data
file = []
file.append("131 673 234 103 18")
file.append("201 96 342 965 150")
file.append("630 803 746 422 111")
file.append("537 699 497 121 956")
file.append("805 732 524 37 331")

size = 5

#file = open('problem67_files/triangle.txt', 'r')
grid = [] # contains the actual triangle
for line in file:
    line = line.split(" ")
    num_array = []
    for i in line:
        num_array.append(int(i))
    grid.append(num_array)


for s in range(2, size):
    for r in range(1, size) # [1, size-1]
        for c in range(



##for row in triangle:
##    print(row)

##for r in range(len(triangle)-1,-1,-1):
##    for c in range(0,len(triangle[r])-1):
##        #print(triangle[r][c])
##        triangle[r-1][c] += max(triangle[r][c],triangle[r][c+1])

end = time.time()
print("found in",str(end-start),"Answer is",str(3))

