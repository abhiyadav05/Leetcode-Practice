class Solution:
    def findMin(self,i:int,j:int,grid:List[List[int]],cur:int,dp):
        n=len(grid)
        m=len(grid[0])
        if(i>=n or j>=m):
            return 1025
        cur^=grid[i][j]
        if(i==n-1 and j==m-1):
            return cur
        if(dp[i][j][cur]!=-1):
            return dp[i][j][cur]
        
        left=self.findMin(i+1,j,grid,cur,dp)
        right=self.findMin(i,j+1,grid,cur,dp)
        dp[i][j][cur]=min(left,right)
        return dp[i][j][cur]

    def minCost(self, grid: list[list[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[[-1]*1025 for _ in range(m)] for _ in range(n)]
        return self.findMin(0,0,grid,0,dp)
        