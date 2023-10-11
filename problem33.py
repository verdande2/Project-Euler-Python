for n in range(10,100):
    for d in range(10,100):
        if n/d>=1:
            continue
        sn = str(n)
        sd = str(d)
        #print("testing "+sn+" / "+sd)
        if int(sd)%10==0:
            continue
        if sn[1]==sd[0] and int(sn[0])/int(sd[1]) == int(sn)/int(sd):
            print(sn+" / "+sd)
