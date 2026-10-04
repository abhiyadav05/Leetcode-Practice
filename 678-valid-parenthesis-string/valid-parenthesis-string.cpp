class Solution {
public:
    bool checkValidString(string s) {
        int n=s.size();
        stack<char>left;
        stack<char>right;
        int star=0;
        int l=0;
        int r=0;
        for(char c : s){
            if(c=='*'){
                star++;
            }else if(c==')'){
                l++;
            }else{
                l-=1;
            }
            if(l>0 && l>star) return false;
        }
        star=0;
        for(int i=n-1;i>=0;i--){
            if(s[i]=='*'){
                star++;
            }else if(s[i]=='('){
                r++;
            }else{
                r-=1;
            }
            if(r>0 && r>star) return false;

        }
        // if(!right.empty()) return false;
        // int size=left.size();
        // if(size>star) return false;
        return true;
    }
};