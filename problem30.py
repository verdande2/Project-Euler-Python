def sumExponentDigits(num,exp):
    string = str(num)
    s = 0
    for digit in string:
        s += int(digit)**exp
    return s

cumSum = 0
for i in range(2,100000000): # 100mil
    #print(str(i) + " = " + str(sumExponentDigits(i,5)))
    if i == sumExponentDigits(i,5):
        print("match found "+str(i))
        cumSum += i
print(str(cumSum))
