# Difficulty: Medium
# Topic: Two pointers
# Problem: https://leetcode.com/problems/container-with-most-water

def maxArea(height):
    left=0
    right=len(height)-1
    count=0
    while left<right:
        width=right-left
        length=min(height[left],height[right])
        current_area=length*width
        count=max(count,current_area)

        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    return count

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))

