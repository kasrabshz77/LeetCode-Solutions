#Time complexity: O(n)
class Solution(object):
    def twoSum(self, nums, target):
        mp = {}
        for i in range(len(nums)):
            mp[nums[i]] = i 
        for i in range(len(nums)):
            need = target - nums[i]
            if need in mp and mp[need] != i:
                return [i, mp[need]]
        return -1
     
