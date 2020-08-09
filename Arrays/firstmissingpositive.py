def firstmissingpositive(self,nums):
    nums.sort()
    result = 1
    for i in range(len(nums)):
        if nums[i]<result:
            continue
        if nums[i]==result:
            result+=1
        else:
            return result
    return result