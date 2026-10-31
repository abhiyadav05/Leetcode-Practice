class Solution:
    def findP(self,i:int,j:int,d:int,grid:List[List[int]]):
        # base case 
        n=len(grid)
        m=len(grid[0])
        if(i<0 or j<0 or j>=m or i>=n):
            return 0
        if(i==n-1 and j==m-1):
            return 1
        
        if(self.dp[i][j][d]!=-1):
            return self.dp[i][j][d]
        ans=0
        if(grid[i][j]==1):
            if(d==0):
                ans+=self.findP(i+1,j,1,grid)%self.md
            else:
                ans+=self.findP(i,j+1,0,grid)%self.md
        else:
            ans+=self.findP(i,j+1,0,grid)%self.md
            ans+=self.findP(i+1,j,1,grid)%self.md
        self.dp[i][j][d]=ans%self.md
        return ans%self.md
    def uniquePaths(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        self.md=(10**9)+7
        self.dp=[[[-1]*2 for _ in range(m)] for _ in range(n)]
        return self.findP(0,0,-1,grid)%self.md
        