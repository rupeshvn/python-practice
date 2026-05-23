"""
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

 

Constraints:

    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.


"""
nums = [-7,-3,2,3,11]

def square_of_list(nums):
    new_nums=[0]*len(nums)
    l=0
    r=len(nums)-1
    pos = len(nums)-1
    while pos>=0:
        left_sq = nums[l]**2
        right_sq = nums[r]**2
        #print(f"the right sq is {right_sq} and left sq is {left_sq} and pos is {pos}")
        if left_sq >= right_sq:
            new_nums[pos]=left_sq
            l = l+1
        else:
            new_nums[pos]=right_sq
            r=r-1
        pos = pos -1
    return new_nums

val = square_of_list(nums)
print(val)