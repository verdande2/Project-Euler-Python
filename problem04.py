def isPalindrome(num):
    temp = str(num)
    if temp[::-1] == temp:
        return True
    else:
        return False
    
highest_palindrome = 0;

for x in range(1,1000):
    for y in range(1,1000):
        num = x*y
        if isPalindrome(num):
            if num>highest_palindrome:
                highest_palindrome = num
print(highest_palindrome)

