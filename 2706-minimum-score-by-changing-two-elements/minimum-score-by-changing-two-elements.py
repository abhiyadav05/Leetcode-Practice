class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        ans1=nums[n-1]-nums[2]
        ans2=nums[n-3]-nums[0]
        ans3=nums[n-2]-nums[1]
        return min(ans1,ans2,ans3)
        