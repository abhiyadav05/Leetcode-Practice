class Solution {
public:
    int minOperations(string s) {
        int n=s.size();
        string temp=s;
        sort(temp.begin(),temp.end());
        if(temp==s){
            return 0;
        }
        if(n==2){
            return -1;
        }
        char first='z';
        char last='a';
        for(char c : s){
            if(c<=first){
                first=c;
            }
            if(c>=last){
                last=c;
            }
        }
        if(first==s[0] || last==s[n-1]){
            return 1;
        }
        char mmin=*min_element(s.begin()+1,s.end()-1);
        char mmax=*max_element(s.begin()+1,s.end()-1);
        if(s[0]>mmax && mmin>s[n-1]){
            return 3;
        }
        
        return 2;
    }
};