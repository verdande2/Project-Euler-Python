import time

def nameScore(string):
    score = 0
    for char in string:
        score += ord(char)-64
    return score

# yields triangle numbers up to a max of num
def triangle(num=200):
    t=1
    i=1
    while True:
        t=int(1/2*i*(i+1))
        if t<=num:
            yield t
        else:
            break
        i+=1

start = time.time()


count = 0

words_file = open('problem42_files/words.txt', 'r')
for line in words_file:
    words = line
words = words.split(",")
words = [word[1:-1] for word in words]
words = [nameScore(word) for word in words]

for word in words:
    if word in triangle():
        count += 1

end = time.time()  
print(str(count)+" found in",end-start,"seconds.")
