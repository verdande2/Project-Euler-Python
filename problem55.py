import time


def isPalindrome(num):
    temp = str(num)
    if temp[::-1] == temp:
        return True
    else:
        return False
    
def isLychrelNumber(num,iterations=50):
    current_iteration=0
    lychrelNumber = True
    for current_iteration in range(1,iterations+1):
        
        #print("iteration: "+str(current_iteration)+" step: "+str(num)+" + "+str(num)[::-1]+" = "+str(num+int(str(num)[::-1])))
        num = num + int(str(num)[::-1])
        if isPalindrome(num):
            lychrelNumber=False
            break
        
        
        
    return {"isLychrelNumber":lychrelNumber,"i":current_iteration}


start = time.time()
count = 0
for x in range(1,10000):
    y = isLychrelNumber(x,50)
    print("x: "+str(x)+" Lychrel: "+str(y["isLychrelNumber"])+" iterations: "+str(y["i"]))
    if y["isLychrelNumber"]:
        count += 1
        #print("Couldn't get palindrome in "+str(y["i"])+" iterations for starting number "+str(x))
end = time.time()
print("found in",str(end-start),"Answer is",str(count))
