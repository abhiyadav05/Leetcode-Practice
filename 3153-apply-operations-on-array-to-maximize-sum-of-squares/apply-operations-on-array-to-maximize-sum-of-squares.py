class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        cnt=[0]*32

        for ele in nums:
            for i in range(32):
                if(ele&(1<<i)):
                    cnt[i]+=1
        
        ans=0
        M=10**9+7
        while k:
            cur=0
            for i in range(32):
                if(cnt[i]>0):
                    cnt[i]-=1
                    cur=cur|(1<<i)
            
            ans=(ans+(cur*cur))%M
            k-=1
        return ans
        