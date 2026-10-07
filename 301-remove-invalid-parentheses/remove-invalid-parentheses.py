class Solution:

    def __init__(self):
        self.st=set()
        self.n=0
        self.maxLen=0
    
    def solve(self,i,s,cur,cnt):
        if(cnt<0):
            return
        
        if(i==self.n):
            if(cnt==0):
                if(len(cur)>self.maxLen):
                    self.st.clear()
                    self.maxLen=len(cur)
                
                if(len(cur)==self.maxLen):
                    self.st.add("".join(cur))
            
            return
        
        if(s[i]!='(' and s[i]!=')'):
            cur.append(s[i])
            self.solve(i+1,s,cur,cnt)
            cur.pop()
            return
        
        cur.append(s[i])

        self.solve(i+1,s,cur,cnt+(1 if s[i]=='(' else -1))

        cur.pop()

        self.solve(i+1,s,cur,cnt)
    


    def removeInvalidParentheses(self, s: str) -> list[str]:
        self.n=len(s)
        cur=[]
        cnt=0

        self.solve(0,s,cur,cnt)

        return list(self.st)
        