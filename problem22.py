import time

def nameScore(string):
    score = 0
    for char in string:
        score += ord(char)-64
    return score

start = time.time()
cumSum = 0
names_file = open('problem22_files/names.txt', 'r')
for line in names_file:
    names = line
names = names.split(",")
names = [name[1:-1] for name in names]
names.sort()
for i in range(0,len(names)):
    score = nameScore(names[i])
    sortedNameScore = score*(i+1)
    cumSum += sortedNameScore
    #print(str(i+1)+": "+names[i]+" nameScore is "+str(score)+" * "+str(i+1)+" = "+str(sortedNameScore))
end = time.time()  
print(str(cumSum)+" found in",end-start,"seconds.")
