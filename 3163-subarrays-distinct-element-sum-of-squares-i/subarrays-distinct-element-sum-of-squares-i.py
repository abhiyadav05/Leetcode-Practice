class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        for i in range(n):
            st=set()
            for j in range(i,n,1):
                st.add(nums[j])
                sz=len(st)
                ans=ans+(sz*sz)
        
        return ans

        