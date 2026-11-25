class Solution:
    def check(self,l,nums):
        mp={}
        hs=0
        n=len(nums)
        for i in range(0,l):
            hs=(hs*self.base+nums[i])%self.M
        
        mp[hs]=mp.get(hs, 0) + 1
        highestP=self.power[l-1]
        for i in range(l,n):
            hs=(hs-nums[i-l]*highestP%self.M+self.M)%self.M
            hs=(hs*self.base+nums[i])%self.M
            mp[hs]=mp.get(hs, 0) + 1

        for key in mp:
            if(mp[key]==1):
                return True
        
        return False
        
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        self.base=100002
        self.power=[1]*(n+1)
        self.M=10**9+7
        for i in range(1,n+1):
            self.power[i]=(self.power[i-1]*self.base)%self.M
        
        low=1
        high=n
        ans=0
        while(low<=high):
            mid=low+(high-low)//2
            if(self.check(mid,nums)):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        
        return ans


        