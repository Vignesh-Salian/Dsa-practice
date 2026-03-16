# Difficulty: Medium
# Topic: Sliding Window
# Problem: https://leetcode.com/problems/max-consecutive-ones-iii

def longestOnes(nums, k):
    n=len(nums)
    left=0
    right=0
    zeros=0
    maxi=0
    while right<n:
        if nums[right]==0:
            zeros+=1
        
        if zeros>k:
            if nums[left]==0:
                zeros-=1
            left+=1
        
        if zeros<=k:
            maxi=max(maxi,right-left+1)
        right+=1
    return maxi

nums=[1,1,1,0,0,0,1,1,1,1,0]
print(longestOnes(nums, 2))
