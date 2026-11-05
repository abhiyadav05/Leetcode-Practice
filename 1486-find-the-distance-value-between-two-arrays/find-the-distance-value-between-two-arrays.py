class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ans=0
        for i in range(len(arr1)):
            ch=False
            for j in range(len(arr2)):
                temp=abs(arr1[i]-arr2[j])
                if(temp<=d):
                    ch=True
                    break
            
            if(not ch):
                ans+=1
        
        return ans