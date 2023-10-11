import time, math

start = time.time()


file = open('problem99_files/base_exp.txt', 'r')
line_number = 0
highest_exp = 0
for line in file:
    line_number += 1
    num_array = line.split(",")
    
    exp = int(num_array[0])**(int(num_array[1])/100000)
    if exp > highest_exp:
        highest_exp = exp
        highest_exp_line_number = line_number
        print(line_number,exp)

end = time.time()
print("found in",str(end-start),"Answer is",str(highest_exp_line_number))
