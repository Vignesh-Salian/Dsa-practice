# Difficulty: Easy
# Topic: Mathematical / Arithmetic (Summation) Pattern
# Problem: https://leetcode.com/problems/missing-number

def missingNumber(nums):
        n=len(nums)
        expected=n*(n+1)//2
        actual=sum(nums)
        return expected-actual

nums = [3,0,1]
print( missingNumber(nums))