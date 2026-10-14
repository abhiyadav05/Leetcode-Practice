class Solution {
public:
    string maxSumOfSquares(int num, int sum) {

        int di=(sum+8)/9;
        if(num<di){
            return "";
        }
        string ans="";
        while(sum>=9){
            ans+='9';
            sum-=9;
            num-=1;
        }
        if(sum>0){
            ans+=('0'+sum);
            num--;
        }
        while(num--){
            ans+='0';
        }
        return ans;
        
    }
};