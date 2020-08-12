class Solution:
    def findLengthOfLCIS(self, nums):

        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        i, j = 0, 0
        maxLen = 0

        while i < len(nums):
            while j < len(nums) - 1 and nums[j] < nums[j + 1]:
                j += 1
            maxLen = max(maxLen, j - i + 1)
            if j < len(nums):
                j += 1
                i = j

        return maxLen