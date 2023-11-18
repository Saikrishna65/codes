class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        greater=[]
        lesser=[]
        ans=[]
        for i in nums:
            if i<0:
                lesser.append(i)
            else:
                greater.append(i)
        for i in range(0,len(greater)):
            ans.append(greater[i])
            ans.append(lesser[i])
        return ans