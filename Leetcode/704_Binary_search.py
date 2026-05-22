"""
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

 

Constraints:

    1 <= nums.length <= 104
    -104 < nums[i], target < 104
    All the integers in nums are unique.
    nums is sorted in ascending order.

"""
nums = [-1,0,3,5,9,12]
target = 2

def index_of_element(nums, target):
    left = 0
    right = len(nums)-1
    mid = (left+right)//2

    while left!=mid:
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid
            mid = (left+right)//2
        else:
            right = mid
            mid = (left+right)//2

    if target == nums[left]:
        return left
    elif target==nums[right]:
        return right
    else:
        return -1
    
new_val = index_of_element(nums, target)
print(new_val)