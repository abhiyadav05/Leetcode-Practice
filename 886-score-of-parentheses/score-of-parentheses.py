class Solution:

    def mypow(self,val:int)->int:
        if(val==0):
            return 1
        ans=1
        while(val>0):
            ans=ans*2
            val-=1
        return ans
        
    def scoreOfParentheses(self, s: str) -> int:
        cnt=0
        ans=0
        for i in range(len(s)):
            if(s[i]=='('):
                cnt+=1
            else:
                cnt-=1
                if(s[i-1]=='('):
                    ans+=self.mypow(cnt)
        
        return ans



        