class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            if(nums[i]<0):
                nums[i]=-nums[i]
                
        nums.sort()
        mid=n-((n+1)//2)
        ans=0
        for i in range(n-1,-1,-1):
            if(i>=mid):
                ans=ans+(nums[i]*nums[i])
            else:
                ans=ans-(nums[i]*nums[i])

        return ans


        