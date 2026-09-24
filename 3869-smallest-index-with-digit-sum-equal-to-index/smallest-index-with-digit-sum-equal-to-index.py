class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            val=nums[i]
            sm=0
            while(val>0):
                dig=(val%10)
                sm+=dig
                val//=10
            if(sm==i):
                return i
        
        return -1

        