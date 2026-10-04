class Solution:
    def maximumHappinessSum(self, h: List[int], k: int) -> int:
        arr=[]
        n=len(h)
        cnt=0
        h.sort()
        ans=0
        for i in range(n-1,-1,-1):
            h[i]-=cnt
            cnt+=1
            if(h[i]<0):
                h[i]=0
            if(k>0):
                ans+=h[i]
                k-=1
      
        return ans


        