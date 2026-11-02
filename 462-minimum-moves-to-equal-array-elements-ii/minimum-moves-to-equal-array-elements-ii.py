class Solution:
    def findDif(self,nums:List[int],val:int)->int:
        sm=0
        for i in range(len(nums)):
            temp=abs(val-nums[i])
            sm+=temp
        return sm
    def minMoves2(self, nums: list[int]) -> int:
        n=len(nums)
        nums.sort()
        ans=self.findDif(nums,nums[n//2])
        return ans
        