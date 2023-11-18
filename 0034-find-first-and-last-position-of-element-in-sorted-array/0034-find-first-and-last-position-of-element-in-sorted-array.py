class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            if nums[i]==target:
                firstindex=i
                break
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==target:
                lastindex=i
                return [firstindex,lastindex]
        return [-1,-1]
        