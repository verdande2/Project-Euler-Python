def hasSameDigits(x):
    if countDigits(x)==countDigits(2*x)==countDigits(3*x)==countDigits(4*x)==countDigits(5*x)==countDigits(6*x):
        return True
    else:
        return False
    
def countDigits(x):
    string = str(x)
    digits={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    for digit in string:
        digits[int(digit)]+=1
    return digits

found = False

x = 0
while not found:
    x+=1
    if hasSameDigits(x):
        found = True
    
    
print(str(x))
