class Solution:
    def dist(self, i: int, d: int, ans: list[int]):
        if(d%2==0):
            ans[i]=1
        else:
            ans[i]=0
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        n=len(seq)
        ans=[0]*n
        d=0
        for i in range(n):
            if(seq[i]=='('):
                d+=1
                self.dist(i,d,ans)
            else :
                self.dist(i,d,ans)
                d-=1
        return ans

        