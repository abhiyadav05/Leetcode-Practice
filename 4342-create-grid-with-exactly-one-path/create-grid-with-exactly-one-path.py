class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid=[['#']*n for _ in range(m)]
        for i in range(m):
            grid[i][0]='.'
        
        for j in range(n):
            grid[m-1][j]='.'
        
        ans=[]
        for i in range(m):
            temp=""
            for j in range(n):
                temp+=grid[i][j]
            ans.append(temp)


        return ans