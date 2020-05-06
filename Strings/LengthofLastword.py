class Solution(object):
    def lengthOfLastWord(self, s):
        lastword = s.split()
        if not lastword:
            return 0
        return len(lastword[-1])
        
