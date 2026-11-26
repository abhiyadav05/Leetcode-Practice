class Solution:
    def canAliceWin(self, n: int) -> bool:
        val=10
        ans=False
        while(n>=val):
            ans=not ans
            n-=val
            val=val-1
        return ans
            
        