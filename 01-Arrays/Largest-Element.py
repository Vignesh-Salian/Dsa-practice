# Difficulty: Easy
# Topic: Linear Traversal
# Problem: https://takeuforward.org/plus/dsa/problems/largest-element


def largest_element(nums):
    large=nums[0]
    for i in range(len(nums)):
        if nums[i]>large:
            large=nums[i]
    return large

nums= [3, 3, 0, 99, -40]
print(largest_element(nums))