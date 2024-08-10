class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        ans=set()
        for i in range(n):
            ans.add(nums[i])
            i+=1
        if len(ans) != n:
            return True
        return False
        