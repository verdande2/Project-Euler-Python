import time
from common import *

start = time.time()
count = 0
nums=[]
for index, triangle_num in genTri(True):
    if triangle_num == 1:
        continue
    if isPentagonalNum(triangle_num) and isHexagonalNum(triangle_num):
        print(str(triangle_num))
        nums.append(triangle_num)
        count +=1
        
    if count == 2:
        # just want the second one
        break

end = time.time()  
print(str(nums[1])+" found in",end-start,"seconds.")
