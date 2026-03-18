# Difficulty: Medium
# Topic: Prefix Sum + Hashmap
# Problem: https://leetcode.com/problems/subarray-sum-equals-k

def subarraySum(nums, k):
    prefix_sum=0
    count=0
    dict={0:1}
    for num in nums:
        prefix_sum+=num

        if prefix_sum-k in dict:
            count+=dict[prefix_sum-k]

        dict[prefix_sum]=dict.get(prefix_sum,0)+1
    return count

nums=[1,1,1]
print(subarraySum(nums, 2))