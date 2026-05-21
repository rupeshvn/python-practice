"""
Given an array of positive integers nums and a positive integer target, 
return the minimal length of a whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1

Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

 

Constraints:

    1 <= target <= 109
    1 <= nums.length <= 105
    1 <= nums[i] <= 104

 
Follow up: If you have figured out the O(n) solution, 
try coding another solution of which the time complexity is O(n log(n)).
"""
s= [1,4,4]
target =4
# l = 0
# r = 1
# sum = s[l]
# min_l = len(s)+1
# print(f"The start min_l is {min_l}")
# while l < r:
#     print(f"The sum now is {sum}")
#     while sum >= target and l<= r-1:
#         print(f"Entering the target loop when sum is {sum} for r is {r}")
#         min_l = min(min_l, r-l+1)
#         sum = sum - s[l]
#         l = l + 1
#     if r< len(s)-1:
#         r = r+ 1
#         sum = sum + s[r]
#     else:
#         sum = sum - s[l]
#         l = l+ 1
        
# if min_l > len(s):
#     min_l = 0

#working code
nums = [1]
target = 4
l = 0
r = 0
min_l = len(nums)+1
while l<= r and r< len(nums):
    if l == r:
        sum = nums[r]
    while sum>= target:
        print(f"Entering the condition for l is {l} and r is {r}")
        min_l = min(min_l,r-l+1)
        sum = sum - nums[l]
        if l < r:
            l= l + 1
    if r<len(nums)-1:
        r = r+1
        sum = sum + nums[r]
    else:
        l = l + 1
        # sum = sum - nums[l]
    print(f"the sum is {sum} and l is {l} and r is {r}")
if min_l == len(nums)+1:
    min_l = 0


#####Optimized code
l=0
curr_sum = 0
min_l = float('inf')

for r in range(len(nums)):
    curr_sum = curr_sum + nums[r]
    
    while curr_sum>= target:
        min_l = min(min_l, r-l+1)
        curr_sum = curr_sum - nums[l]
        l = l + 1

if min_l == float('inf'):
    min_l = 0
   





print(min_l)
