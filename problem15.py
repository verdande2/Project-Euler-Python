""" 1 denotes moving right, 0 denotes moving down"""
def findNumPaths(box_size=3):
    count = 0
    for x in range(1, 2**(box_size*2)):
        #print(binString(x,2*box_size))
        if isValidPath(binString(x,2*box_size),box_size):
            count+=1
    return count

def isValidPath(x,box_size):
    left=0
    top=0
    for i in x:
        if i=="1":
            left+=1
        elif i=="0":
            top+=1
        else:
            print("error reading binary value: "+i)
    if left==box_size and top==box_size:
        return True
    else:
        return False

def binString(num,padding=0):
    string = bin(num)[2:]
    if padding!=0 and len(string)<padding:
        while len(string)<padding:
            string = "0"+string
    return string

print(str(findNumPaths(4)))
