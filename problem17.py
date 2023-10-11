import re, time

letterPattern = re.compile("[a-zA-Z]{1}")

def numToWords(num):
    SingleCases={1:"one",
                 2:"two",
                 3:"three",
                 4:"four",
                 5:"five",
                 6:"six",
                 7:"seven",
                 8:"eight",
                 9:"nine",
                 10:"ten",
                 11:"eleven",
                 12:"twelve",
                 13:"thirteen",
                 14:"fourteen",
                 15:"fifteen",
                 16:"sixteen",
                 17:"seventeen",
                 18:"eighteen",
                 19:"nineteen",
                 20:"twenty",
                 30:"thirty",
                 40:"forty",
                 50:"fifty",
                 60:"sixty",
                 70:"seventy",
                 80:"eighty",
                 90:"ninety",
                 100:"hundred",
                 1000:"thousand",
                 1000000:"million"
                 }
    if num<=20:
        return SingleCases[num]
    elif num>20 and num<100:
        if num%10==0:
            return SingleCases[num//10*10]
        else:
            return SingleCases[num//10*10]+"-"+SingleCases[num%10]
    elif num>=100 and num<1000:
        if num%100==0:
            return SingleCases[num//100] + " " + SingleCases[100]
        else:
            return SingleCases[num//100]+" "+SingleCases[100] + " and " + numToWords(num-(num//100)*100)
    elif num>=1000 and num<10000:
        if num%1000==0:
            return SingleCases[num//1000] + " " + SingleCases[1000]
        else:
            return SingleCases[num//1000]+" "+SingleCases[1000] + " " + numToWords(num-(num//1000)*1000)
    else:
        return "This function doesn't support any number over 10 thousand, but can be expanded to as far as needed with the current logic"

def countLetters(string):
    count = 0
    for char in string:
        result = letterPattern.match(char)
        if result != None:
            count +=1
    return count

start = time.time()
cumSum = 0
for i in range(1,1001):
    cumSum += countLetters(numToWords(i))

end = time.time()  
print(str(cumSum)+" found in",end-start,"seconds.")
