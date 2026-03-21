# Difficulty: Easy
# Topic: Linear Traversal
# Problem: https://takeuforward.org/plus/dsa/problems/linear-search

def linearSearch(nums, target):
    for i in range(len(nums)):
        if nums[i]==target:
            return i
    return -1

nums= [2, 3, 4, 5, 3]
print(linearSearch(nums,3))
