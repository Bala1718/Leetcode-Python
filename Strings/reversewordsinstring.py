class Solution(object):
    def reverseWords(self, s):
        s1 = list(s.split())
        s1 = s1[::-1]
        s_reversed = " ".join(s1)
        return s_reversed
