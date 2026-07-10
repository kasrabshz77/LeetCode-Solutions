class Solution(object):
    def majorityElement(self, nums):
        majority = (len(nums) - 1) / 2
        mp = {}
        for item in nums:
            if item in mp:
                mp[item]+=1
            else:
                mp[item] = 1
        
        for item in nums:
            if mp[item] > majority:
                return item
        
