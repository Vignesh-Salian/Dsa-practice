# Difficulty: Easy
# Topic: Arrays
# Problem: https://leetcode.com/problems/contains-duplicate/

def containsDuplicate(nums):
    return len(nums) != len(set(nums))
