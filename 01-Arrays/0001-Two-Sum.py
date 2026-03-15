# Difficulty: Easy
# Topic: Hash map
# Problem: https://leetcode.com/problems/two-sum

def twoSum(nums, target):
    n=len(nums)
    dict={}
    for i in range(0,n):
        remaining=target-nums[i]
        if remaining in dict:
            return [dict[remaining],i]
        dict[nums[i]]=i


nums= [3,3]
print(twoSum(nums, 6))