nums = [2,2,2,4,5,6,6,8]
i = 0
val = 0

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        val = 0
        if len(nums) ==1:
            val = val + 1
            return val
        if len(nums)==2:
            left = nums[i]
            right = nums[i+1]
            if left == right:
                val = val + 1
                return val
            else:
                val = val+2
                return val
        while i <= len(nums)-2:
            left = nums[i]
            right = nums[i+1]
            if left != right and i!= len(nums)-2:
                nums[val] = left
                val = val + 1
            elif left != right and i == len(nums)-2:
                nums[val]= left
                nums[val+1] = right
                val = val+2
            elif left == right and i == len(nums)-2:
                nums[val]=left
                val = val + 1
            i = i + 1
        return val



##The above is very complex solutn that i wrote myself. The solution from chatgpt is below

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        val = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[val]=nums[i]
                val=val+1
        return val