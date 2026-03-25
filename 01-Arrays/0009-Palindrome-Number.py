# Difficulty: Easy
# Topic: Digit Extraction Pattern
# Problem: https://leetcode.com/problems/palindrome-number

def isPalindrome(x):
        temp=x
        rev=0
        while temp>0:
            digit=temp%10
            rev=rev*10+digit
            temp=temp//10
            
        if rev==x:
            return True
        else:
            return False

x = 123
print(isPalindrome(x))