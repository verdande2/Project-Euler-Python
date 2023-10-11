import time, math
from common import isPandigital
    
start = time.time()
f_a = 1
f_b = 1

notFound = True
f_count = 1

while (notFound):
    f_c = f_a + f_b
    f_a = f_b
    f_b = f_c
    f_count += 1
    
    s = str(f_a)
    a = isPandigital(s[:9])
    b = isPandigital(s[::-1][:9])
    
    print(f_count)
    # note: f_a is the f_count-th fibonacci number

    if a and b:
        print('WINNER! --------------------------------------------')
        num = f_count
        break
    

end = time.time()
print("found in",str(end-start),"Answer is",str(num))
