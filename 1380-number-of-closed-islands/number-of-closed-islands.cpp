class Solution {
public:
    int closedIsland(vector<vector<int>>& grid) {
        int m=grid.size(),n=grid[0].size();
        if(m<=2 || n<=2)return 0;
        vector<vector<int>>vis(m,vector<int>(n,0));
        int delrow[]={-1,0,1,0};
        int delcol[]={0,1,0,-1};
        int cnt=0;
        for(int i=1;i<m-1;i++){
            for(int j=1;j<n-1;j++){
                if(grid[i][j]==0 && !vis[i][j]){
                    bool flag=false;
                    queue<pair<int,int>>q;
                    q.push({i,j});
                    vis[i][j]=1;
                    while(!q.empty()){
                        int row=q.front().first;
                        int col=q.front().second;
                        q.pop();
                        for(int k=0;k<4;k++){
                            int nrow=row+delrow[k];
                            int ncol=col+delcol[k];
                            if(ncol>=0 && ncol<n && nrow>=0 && nrow<m && grid[nrow][ncol]==0 && 
                            !vis[nrow][ncol]){
                                vis[nrow][ncol]=1;
                                q.push({nrow,ncol});
                                //special condition
                                if(ncol==0 || ncol==n-1 || nrow==0 || nrow==m-1)flag=true;
                            }
                        }
                    }
                    if(!flag)++cnt;
                }
            }
        }
        return cnt;
    }
};