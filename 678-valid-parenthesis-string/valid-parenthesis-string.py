class Solution:
    def checkValidString(self, s: str) -> bool:
        star=0
        l=0
        for c in s:
            if(c==')'):
                l+=1
            elif(c=='*'):
                star+=1
            else :
                l-=1
            
            if(l>0 and l>star):
                return False
        
        star=0
        l=0
        # k=''.join(reversed(s))
        # print(k)
        for c in reversed(s):
            if(c=='('):
                l+=1
            elif(c=='*'):
                star+=1
            else :
                l-=1
            
            if(l>0 and l>star):
                return False
        return True
        