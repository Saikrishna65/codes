class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        s=0
        i=0
        j=0
        while i<len(nums):
            s=0
            j=i+1
            while j<len(nums):
                s=nums[i]+nums[j]
                if s==target:
                    return [i,j]
                j+=1
            i+=1
        return -1