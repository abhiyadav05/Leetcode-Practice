class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        cnt=0
        ch=-1
        cur=""
        ans=""
        for c in s:
            if(c=='('):
                cnt+=1
            else :
                cnt-=1
            if(ch==-1):
                ch=0
                continue
            if(cnt==0):
                ans+=cur
                cur=""
                ch=-1
                continue
            
            
            cur+=c
        
        return ans
        