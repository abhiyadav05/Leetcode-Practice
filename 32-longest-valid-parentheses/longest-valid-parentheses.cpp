class Solution {
public:
    int longestValidParentheses(string s) {
        int n=s.size();
        stack<int>st;
        vector<int>pre(n,0);
        for(int i=0;i<n;i++){
            if(s[i]=='('){
                st.push(i);
            }else{
                if(!st.empty()){
                    int tp=st.top();
                    st.pop();
                    pre[i]=1;
                    pre[tp]=1;
                }
            }
        }
        int cnt=0;
        int ans=0;
        for(int i=0;i<n;i++){
            if(pre[i]==1){
                cnt+=1;
            }else{
                cnt=0;
            }
            ans=max(ans,cnt);
        }
        return ans;
    }
};