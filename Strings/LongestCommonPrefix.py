class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        firstword = strs[0]
        for i in range(len(firstword)+1):
            for k in strs:
                try:
                    if firstword[i]!=k[i]:
                        return firstword[:i]
                except IndexError:
                    return firstword[:i]
