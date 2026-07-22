class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        dic = {}
        for item in magazine:
            if item in dic:
                dic[item]+=1
            else:
                dic[item]=1
        
        for char in ransomNote:
            if char not in dic or dic[char] == 0:
                return False
            dic[char]-=1
        return True 
        
