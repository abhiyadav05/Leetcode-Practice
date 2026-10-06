class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cn1=0
        cn2=0
        ans=0
        for c in s:
            if(c=='('):
                cn1+=1
            else:
                if(cn1>0):
                    cn1-=1
                else:
                    ans+=1
        
        return ans+cn1
        