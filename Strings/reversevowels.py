class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = list(filter(lambda x : x in 'aeiouAEIOU', s))
        return ''.join(x if x not in 'aeiouAEIOU' else vowels.pop() for x in s)