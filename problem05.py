test = 0
found = False
while not found:
    found = True
    test +=1
    if test%10000000==0:
        print(".")
    for x in range(1,21):
        if test%x!=0:
            found=False
            break
    
print(test)
    
