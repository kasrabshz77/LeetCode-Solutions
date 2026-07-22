class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
        if len(words)!= len(pattern):
            return False
        
        word_to_letter = {}
        letter_to_word = {}

        for i in range(len(pattern)):
            char_p = pattern[i]
            char_w = words[i]

            if char_p in letter_to_word and letter_to_word[char_p] != char_w:
                return False
            if char_w in word_to_letter and word_to_letter [char_w] != char_p:
                return False
            word_to_letter[char_w] = char_p
            letter_to_word[char_p] = char_w
        
        return True 
