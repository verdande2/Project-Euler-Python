count = 0
for a in range(0,201):
    for b in range(0,101):
        for c in range(0,41):
            for d in range(0,21):
                for e in range(0,11):
                    for f in range(0,5):
                        for g in range(0,3):
                            for h in range(0,2):        
                                if a+2*b+5*c+10*d+20*e+50*f+100*g+200*h==200:
                                    count += 1
print(str(count))
