class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        di=(sum+8)//9
        if(num<di):
            return ""
        
        ans=""
        while(sum>8):
            ans+='9'
            sum-=9
            num-=1
        if(sum>0):
            ans+=chr(ord('0')+sum)
            num-=1
        while(num):
            ans+='0'
            num-=1
        return ans

        