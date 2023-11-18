class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans={}
        for i in nums:
            if i in ans:
                ans[i]+=1
            else:
                ans[i]=1
        for key in ans:
            if ans[key]>=len(nums)/2:
                return key