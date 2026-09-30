class Solution {
public:
    void dist(int i,int d,vector<int>& ans){
        if(d%2==0){
            ans[i]=0;
        }else{
            ans[i]=1;
        }
    }
    vector<int> maxDepthAfterSplit(string seq) {
        int n=seq.size();
        vector<int>ans(n);
        int d=0;
        for(int i=0;i<n;i++){
            if(seq[i]=='('){
                d+=1;
                dist(i,d,ans);
            }else{
                dist(i,d,ans);
                d-=1;
            }
        }
        return ans;
    }
};