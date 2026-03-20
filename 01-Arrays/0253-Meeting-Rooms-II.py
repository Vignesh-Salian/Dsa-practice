# Difficulty: Medium
# Topic: prefix sum
# Problem:https://leetcode.com/problems/meeting-rooms-ii/

def minmeetingroom(intervals):
    p_s=0
    count=0
    hashmap={}
    for start,end in intervals:
        hashmap[start]=hashmap.get(start,0)+1
        hashmap[end]=hashmap.get(end,0)-1
    for time in sorted(hashmap):
        p_s+=hashmap[time]
        count=max(count,p_s)
    return count

intervals=[[0,40],[5,10],[15,20]] 
print( minmeetingroom(intervals))