from collections import defaultdict
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n=len(nums)
        rsum=0
        lsum=0
        freq=defaultdict(int)
        # ans=maxsize
        ans=float('inf')
        for i in range(n):
            rsum+=nums[i]
            if(rsum==x):
                ans=min(ans,i+1)
            freq[rsum]=i+1
        
        for i in range(n-1,-1,-1):
            lsum+=nums[i]
            if(lsum==x):
                ans=min(ans,n-i)
            temp=x-lsum
            if(temp in freq):
                val=freq[temp]
                if(val<=i):
                    ans=min(ans,(n-i+val))
        if(ans==float('inf')): return -1
        return ans

        