# Difficulty: Medium
# Topic: Two pointers
# Problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted


def twoSum(nums, target):
    left=0
    right=len(nums)-1
    while left<right:
        total=nums[left]+nums[right]
        if total==target:
            return [left+1,right+1]
        elif total<target:
            left+=1
        else:
            right-=1

nums= [2,7,11,15]
print(twoSum(nums,9))