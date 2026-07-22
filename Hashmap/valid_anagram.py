class Solution(object):
    def isAnagram(self, s, t):
        mp1 = {}
        mp2 ={}
        
        for item in s:
            if item in mp1:
                mp1[item]+=1
            else:
                mp1[item]=1
        
        for item in t:
            if item in mp2:
                mp2[item]+=1
            else:
                mp2[item]=1
        
        return mp1==mp2
        
