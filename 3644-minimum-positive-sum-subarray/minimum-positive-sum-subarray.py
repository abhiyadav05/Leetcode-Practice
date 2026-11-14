class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ans=float('inf')
        n=len(nums)
        for i in range(n):
            s=0
            for j in range(i,n):
                s+=nums[j]
                sz=j-i+1
                if(l<=sz and sz<=r and s>0):
                    ans=min(ans,s)
        if(ans==float('inf')):
            return -1
        return ans

        