class Solution {
public:
    unordered_set<string>st;
    int n;
    int maxLen=0;

    void solve(int i,string& s,string& cur,int cnt){
        if(cnt<0) return ;

        if(i==n){
            if(cnt==0){
                if(cur.length()>maxLen){
                    st.clear();
                    maxLen=cur.length();
                }
                if(cur.length()==maxLen){
                    st.insert(cur);
                }
            }
            return;
        }

        if(s[i]!='(' && s[i]!=')'){
            cur.push_back(s[i]);
            solve(i+1,s,cur,cnt);
            cur.pop_back();
            return ;
        }

        cur.push_back(s[i]);
        solve(i+1,s,cur,cnt+ (s[i]=='(' ? 1 : -1));
        cur.pop_back();
        
        solve(i+1,s,cur,cnt);
    }
    vector<string> removeInvalidParentheses(string s) {
        n=s.size();

        string cur="";
        int cnt=0;
        solve(0,s,cur,cnt);
        return vector<string>(st.begin(),st.end());
    }
};