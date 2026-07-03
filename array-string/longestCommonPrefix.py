class Solution(object):
    def longestCommonPrefix(self, strs):
        for i in range(len(strs[0])):
            char = strs[0][i]
            for word in strs:
                if i == len(word) or char != word[i]:
                    return strs[0][:i]
        return strs[0]
