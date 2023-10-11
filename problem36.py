def isPalindrome(num): # in decimal AND in binary
    temp = str(num)
    btemp = bin(num)
    if btemp[2:][::-1] == btemp[2:] and temp[::-1] == temp:
        return True
    else:
        return False

sum_of_palindromes = 0
x = 1
while x<1000000:
    if isPalindrome(x):
        sum_of_palindromes += x
    x+=1
print(str(sum_of_palindromes))
    
