a=b=c=0

found = False
for a in range(1,1001):
    for b in range(1,1001):
        c = (a**2+b**2)**.5
        if (a**2 + b**2 == c**2):
            if a+b+c==1000:
                p = [a, b, int(c)]
                found = True
                break
    if found:
        break
        pass

print("pythagorean triple that sums to 1000 's product: "+str(p[0]*p[1]*p[2]))
