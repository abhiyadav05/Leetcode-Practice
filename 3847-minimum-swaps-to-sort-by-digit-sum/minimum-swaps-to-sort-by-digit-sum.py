class Solution:
    def getDig(self,val):
        sum=0
        while(val>0):
            sum=sum+(val%10)
            val//=10
        return sum

    def cmp(self,a,b):
        d1=self.getDig(a)
        d2=self.getDig(b)
        if(d1!=d2):
            return d1-d2
        return a-b
    def minSwaps(self, nums: List[int]) -> int:
        from collections import defaultdict
        from functools import cmp_to_key
        mp={}
        n=len(nums)
        arr=nums.copy()
        arr = [(self.getDig(x), x) for x in nums]
        arr.sort()
        arr = [x[1] for x in arr]
        for i in range(n):
            mp[nums[i]]=i

        ans=0
        for i in range(n):
            exp=arr[i]
            cur=nums[i]
            if(exp==cur) : continue
            idx=mp[exp]
            nums[i]=exp
            nums[idx]=cur
            mp[exp]=i
            mp[cur]=idx
            ans+=1

        return ans


        