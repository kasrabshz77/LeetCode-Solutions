class Solution(object):
    def isSubsequence(self, s, t):
        i = 0 
        for item in t:
            if i < len(s) and item == s[i]:
                i+=1
        return i == len(s)
