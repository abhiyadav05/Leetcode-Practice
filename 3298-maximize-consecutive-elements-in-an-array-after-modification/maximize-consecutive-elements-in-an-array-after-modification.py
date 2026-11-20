class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        mx=max(nums)
        nums.sort()
        dp=[0]*(mx+2)
        ans=0
        for i,x in enumerate(nums):
            dp[x+1]=dp[x]+1
            dp[x]=dp[x-1]+1
            ans=max(ans,dp[x],dp[x+1])
        
        return ans
        