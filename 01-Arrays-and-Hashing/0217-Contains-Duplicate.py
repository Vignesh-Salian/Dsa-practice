# Difficulty: Easy
# Topic: Hash map
# Problem: https://leetcode.com/problems/contains-duplicate

def containsDuplicate(nums):
    hash_map={}
    for i in range(len(nums)):
        number=nums[i]
        if number in hash_map:
            return True
        else:
            hash_map[number]=1
    return False

nums=[1,2,3,4,2]
print(containsDuplicate(nums))