class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        res=[0]*k
        preCnt=[0]*k
        for i in range(n):
            cur=[0]*k
            cur[nums[i]%k]+=1
            for old in range(k):
                nr=(old*nums[i])%k
                cur[nr]+=preCnt[old]
            
            preCnt=cur
            for x in range(k):
                res[x]+=preCnt[x]
            
        return res

        