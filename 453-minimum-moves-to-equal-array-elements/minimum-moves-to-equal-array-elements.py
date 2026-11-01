class Solution:
    def minMoves(self, nums: list[int]) -> int:
        sm=sum(nums)
        mn=min(nums)
        n=len(nums)
        return (sm-(n*mn))


        