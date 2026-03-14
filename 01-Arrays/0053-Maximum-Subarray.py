# Difficulty: Medium
# Topic: Kaden's Algorithm
# Problem: https://leetcode.com/problems/maximum-subarray

def maximum_subarray(nums):
    n=len(nums)
    total=0
    maxi=float("-inf")
    for i in range(n):
        total+=nums[i]
        maxi=max(maxi,total)
        if total<0:
            total=0
    return maxi

nums = [5,4,-1,7,8]
print(maximum_subarray(nums))
