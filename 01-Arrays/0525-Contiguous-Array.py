# Difficulty: Medium
# Topic: Prefix Sum + Hashmap
# Problem: https://leetcode.com/problems/contiguous-array


def findMaxLength(nums):
       hash_map={0:-1}
       prefix_sum=0
       count=0
       for i in range(len(nums)):
        if nums[i]==0:
            prefix_sum+=1
        else:
            prefix_sum-=1
        if prefix_sum in hash_map:
            count=max(count,i-hash_map[prefix_sum])
        else:
            hash_map[prefix_sum]=i
       return count

nums=[0,0,0,0,0,1,1]
print(findMaxLength(nums))   