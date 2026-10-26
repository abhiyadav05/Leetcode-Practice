class Solution:
    def dfs(self, i:int, j:int, vis:List[List[int]], grid:List[List[int]])->int:
        n=len(grid)
        m=len(grid[0])
        
        if(i<0 or j<0 or i>=n or j>=m or vis[i][j]==1 or grid[i][j]<=0):
            return 0
        
        vis[i][j]=1
        temp=grid[i][j]
        temp+=self.dfs(i+1,j,vis,grid)
        temp+=self.dfs(i-1,j,vis,grid)
        temp+=self.dfs(i,j+1,vis,grid)
        temp+=self.dfs(i,j-1,vis,grid)
        return temp

    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n=len(grid)
        m=len(grid[0])
        vis=[[0]*m for _ in range(n)]
        ans=0
        for i in range(n):
            for j in range(m):
                if(vis[i][j]==0 and grid[i][j]>0):
                    val=self.dfs(i,j,vis,grid)
                    # print(val)
                    if((val%k)==0):
                        ans+=1
        return ans
        