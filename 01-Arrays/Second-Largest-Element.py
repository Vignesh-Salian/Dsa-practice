# Difficulty: Easy
# Topic: Linear Traversal
# Problem: https://takeuforward.org/plus/dsa/problems/second-largest-element

def sec_large(nums):
    large=nums[0]
    sec_large=float("-inf")
    for i in range(1,len(nums)):
        if nums[i]>large:
            sec_large=large
            large=nums[i]
        elif nums[i]<large and nums[i]>sec_large:
            sec_large=nums[i]
    return sec_large if sec_large!=float("-inf") else -1

nums = [8, 8, 7, 6, 5]
print(sec_large(nums))