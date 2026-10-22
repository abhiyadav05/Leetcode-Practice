class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        ac=0
        dc=0
        for i in range(1,n):
            if(nums[i]==(nums[i-1]+1)%n):
                ac+=1
            if((nums[i]+1)%n==nums[i-1]):
                dc+=1
        
        if(ac==n-1 and nums[0]==0):
            return 0
        
        if(ac==n-1):
            right=1+(nums[n-1]+1)+1
            left=n-nums[0]
            return min(right,left)
        
        if(dc==n-1):
            right=(nums[0]+1)%n+1
            left=n-nums[n-1]+1
            return min(right,left)
        
        return -1
        
        