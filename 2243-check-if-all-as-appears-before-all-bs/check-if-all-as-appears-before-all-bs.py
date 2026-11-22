class Solution:
    def checkString(self, s: str) -> bool:
        ch=False
        for i in range(len(s)):
            if(s[i]=='b'):
                ch=True
            if(ch and s[i]=='a'):
                return False
        
        return True
        