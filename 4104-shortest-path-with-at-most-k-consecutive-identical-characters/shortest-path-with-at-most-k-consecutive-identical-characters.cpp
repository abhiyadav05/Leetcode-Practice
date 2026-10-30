class Solution {
public:
    int shortestPath(int n, vector<vector<int>>& edges, string lb, int k) {
        vector<vector<pair<int,int>>>adj(n);
        for(auto ele : edges){
            int u=ele[0];
            int v=ele[1];
            int wt=ele[2];
            adj[u].push_back({v,wt});
        }
        set<pair<int,pair<int,int>>>st;
        st.insert({0,{0,1}});
        vector<vector<int>>dist(n,vector<int>(k+1,INT_MAX));
        dist[0][1]=0;
        
        while(!st.empty()){
            auto it =*st.begin();
            int d=it.first;
            int u=it.second.first;
            int cnt=it.second.second;
            st.erase(it);
            if(d!=dist[u][cnt]) continue;
            if(u==n-1){
                return d;
            }
            for(auto ele : adj[u]){
                int v=ele.first;
                int wt=ele.second;
                int ncnt=(lb[u]==lb[v]) ? cnt+1 : 1;
                if(ncnt>k) continue;

                if(d+wt<dist[v][ncnt]){
                    dist[v][ncnt]=d+wt;
                    st.insert({dist[v][ncnt],{v,ncnt}});
                }
            }
        }
        return -1;
    }
};