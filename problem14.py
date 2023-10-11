answer = {"number":0, "chain_length":0}
for n in range(1,1000000):
    e = n
    chain_length=1
    while e!=1:
        if e%2==0:
            e/=2
        else:
            e=3*e+1
        chain_length+=1
    if chain_length > answer["chain_length"]:
        print(str(n)+" has a chain length of "+str(chain_length))
        answer["number"]=n
        answer["chain_length"]=chain_length

            
        
        
