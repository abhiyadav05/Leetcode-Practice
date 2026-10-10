class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        ans=0
        n=len(nums1)
        k=k1+k2
        sz=0
        for i in range(n):
            diff=abs(nums1[i]-nums2[i])
            sz=max(diff,sz)
        
        arr=[0]*(sz+1)
        for i in range(n):
            diff=abs(nums1[i]-nums2[i])
            arr[diff]+=1
        
        
        i=sz
        while(i>0 and k>0):
            op=min(k,arr[i])
            arr[i]-=op
            arr[i-1]+=op
            k-=op
            i-=1
        
        for i in range(len(arr)):
            ans=ans+(arr[i]*i*i)
        return ans



        