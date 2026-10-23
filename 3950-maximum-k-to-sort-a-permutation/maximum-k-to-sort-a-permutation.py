class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k=-1
        for i in range(len(nums)):
            if(nums[i]!=i):
                k=(nums[i]&k)
            
        if(k==-1):
            return 0
        return k
        