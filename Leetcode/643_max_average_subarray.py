"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

Input: nums = [5], k = 1
Output: 5.00000

 

Constraints:

    n == nums.length
    1 <= k <= n <= 105
    -104 <= nums[i] <= 104

"""

nums = [1,12,-5,-6,50,3]
k = 4
def max_sub_avg(nums,k):
    l = 0
    r= 0
    max_avg = -float("inf")
    sum = 0
    while r<=len(nums)-1:
        sum = sum + nums[r]          
        if r - l == k-1:
            if max_avg != -float("inf"):
                max_avg = max(max_avg,sum/k)
                    
            else:
                max_avg = sum/k
            sum = sum - nums[l]
            l=l+1
            r=r+1
        else:
            r = r+1
    return max_avg

val = max_sub_avg(nums,k)
print(val)


############optimized code

def max_sub_avg_opt(nums,k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for r in range(k, len(nums)):
        window_sum += nums[r]-nums[r-k]
        max_sum = max(max_sum,window_sum)
    return max_sum/k

val = max_sub_avg_opt(nums,k)
print(val)