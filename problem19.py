import time

start = time.time()
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

curr_day = 0
n=0
for year in range(1900,2001):
    #print("day was:",days[curr_day%7])
    for day in range(1,31+1): #jan
        if year>1900 and days[curr_day%7]=="Sunday" and day==1:
            n+=1
        curr_day+=1
    for day in range(1,28+1): #feb
        if year>1900 and days[curr_day%7]=="Sunday" and day==1:
            n+=1
        curr_day+=1

    # determine if leap year
    if year%4==0 or year%400==0:
        curr_day+=1 # add feb 29 in
        
    for day in range(1,31+1): #mar
        if year>1900 and days[curr_day%7]=="Sunday" and day==1:
            n+=1
        curr_day+=1
        
    for day in range(1,30+1): #apr
        if year>1900 and days[curr_day%7]=="Sunday" and day==1:
            n+=1
        curr_day+=1
    for day in range(1,31+1): #may
        if year>1900 and days[curr_day%7]=="Sunday" and day==1:
            n+=1
        curr_day+=1
    for day in range(1,30+1): #jun
        if year>1900 and days[curr_day%7]=="Sunday" and day==1:
            n+=1
        curr_day+=1
        
    for day in range(1,31+1): #jul
        if year>1900 and days[curr_day%7]=="Sunday" and day==1:
            n+=1
        curr_day+=1
    for day in range(1,31+1): #aug
        if year>1900 and days[curr_day%7]=="Sunday" and day==1:
            n+=1
        curr_day+=1
    for day in range(1,30+1): #sep
        if year>1900 and days[curr_day%7]=="Sunday" and day==1:
            n+=1
        curr_day+=1
        
    for day in range(1,31+1): #oct
        if year>1900 and days[curr_day%7]=="Sunday" and day==1:
            n+=1
        curr_day+=1
    for day in range(1,30+1): #nov
        if year>1900 and days[curr_day%7]=="Sunday" and day==1:
            n+=1
        curr_day+=1
    for day in range(1,31+1): #dec
        if year>1900 and days[curr_day%7]=="Sunday" and day==1:
            n+=1
        curr_day+=1
    

end = time.time()
print("found in",str(end-start),"Answer is",str(n))
