# Difficulty:   Easy
# Topic: Linear traversal
# Problem: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated

def check(nums):
    count=0
    n=len(nums)
    for i in range(n-1):
        if nums[i-1]>nums[i]:
            count+=1
        
    if nums[n-1]>nums[0]:
        count+=1
    return count<=1

nums=[2,1,3,4]
print(check(nums))