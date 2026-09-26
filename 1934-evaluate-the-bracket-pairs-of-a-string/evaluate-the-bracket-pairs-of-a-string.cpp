class Solution {
public:
    string evaluate(string s, vector<vector<string>>& knowledge) {
        int n = s.length();
        unordered_map<string, string> mp;
        for(auto vec : knowledge) {
            mp[vec[0]] = vec[1];
        }
        string res = "";
        string temp = "";
        bool bo = false;
        int i = 0;
        while(i < n) {
            if(s[i] == '(') {
                bo = true;
            } else if(s[i] == ')') {
                res += mp.count(temp) ? mp[temp] : "?";
                bo = false;
                temp = "";
            } else if(bo) {
                temp.push_back(s[i]);
            } else {
                res.push_back(s[i]);
            }
            i++;
        }
        return res;
    }
};