def sumDigits(num):
    string = str(num)
    s = 0
    for digit in string:
        s += int(digit)
    return s


max_digital_sum = 0
for a in range(1,100):
    for b in range(1,100):
        x = sumDigits(a**b)
        if x > max_digital_sum:
            print("new max: "+str(a)+"**"+str(b)+" = "+str(x))
            max_digital_sum = x
