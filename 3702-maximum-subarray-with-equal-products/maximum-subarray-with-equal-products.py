class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans=0
        import math
        for i in range(len(nums)):
            p=1
            lc=nums[i]
            gc=nums[i]
            for j in range(i,len(nums)):
                lc=math.lcm(lc,nums[j])
                gc=math.gcd(gc,nums[j])
                p*=nums[j]
                if(p==(lc*gc)):
                    ln=j-i+1
                    ans=max(ans,ln)
        
        return ans


        