class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0 
        minimum = float("inf")
        total = 0 
        for right in range(len(nums)):
            total+=nums[right]
            while total >= target:
                minimum = min(minimum, right-left+1)
                total-=nums[left]
                left+=1
            
        if minimum == float("inf"):
            return 0 
        
        return minimum



