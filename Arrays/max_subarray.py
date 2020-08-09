def maxsubarray(self,nums):
    for i in xrange(1,len(nums)):
        nums[i] = max(nums[i-1]+nums[i],nums[i])
    return max(nums)
