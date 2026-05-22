"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown 
index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], 
..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 

For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and 
become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, 
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:

Input: nums = [1], target = 0
Output: -1

 

Constraints:

    1 <= nums.length <= 5000
    -104 <= nums[i] <= 104
    All values of nums are unique.
    nums is an ascending array that is possibly rotated.
    -104 <= target <= 104

failing scenarios
nums = [3,1]
target = 1

nums = [1]
target = 1
    
"""


nums = [1,3]
target = 3

def return_valindex(nums,target):
    pivot_point = float('inf')
    for i in range(1,len(nums)):
        if nums[i]<nums[0]:
            pivot_point = i
            break
    print(f"The pivot point is {pivot_point}")
    if pivot_point!=float('inf'):
        if target > nums[len(nums)-1]:
            left =0
            right = pivot_point -1
        else:
            left = pivot_point
            right = len(nums)-1
    else:
        left = 0
        right = len(nums)-1

    # if left == right:
    #     if target == nums[left]:
    #         return left
    #     else:
    #         return -1
    
    mid = (left+right)//2
    i = 0

    while left <= right:
        print(f"the left is {left} and right is {right} and mid is {mid}")
        if target == nums[mid]:
            return mid
        elif target == nums[right]:
            return right
        elif mid == left or mid ==right:
            break
        elif target > nums[mid]:
            left = mid+1
        else:
            right = mid

        mid =(left+right)//2
    
    # if target == nums[left]:
    #     return left
    # elif target == nums[right]:
    #     return right

    return -1

val = return_valindex(nums,target)
print(val)
