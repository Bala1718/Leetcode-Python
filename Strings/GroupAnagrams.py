class Solution(object):
    def groupAnagrams(self, strs):
        result = collections.defaultdict(list)
        for word in strs:
            result[tuple(sorted(word))].append(word)
        return result.values()
        
