class Solution:
    def minInsertions(self, s: str) -> int:
        n=len(s)
        cnt1=0
        cnt2=0
        ans=0
        i=0
        while(i<n):
            if(s[i]=='('):
                cnt1+=1
            else :
                if((i+1)<n and s[i+1]==')'):
                    i+=1
                else:
                    ans+=1
                
                if(cnt1>0):
                    cnt1-=1
                else:
                    ans+=1
            i+=1
        return ans+(2*cnt1)
        