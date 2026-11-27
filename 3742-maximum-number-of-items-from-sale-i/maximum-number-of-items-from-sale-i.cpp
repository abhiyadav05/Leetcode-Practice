class Solution {
public:
    int dp[1001][1502];
    int findMax(int n,int budget,int minPrice,vector<vector<int>>& items,vector<int>& cp){
        if(n==0){
            return budget/minPrice;
        }
        if(dp[n-1][budget]!=-1){
            return dp[n-1][budget];
        }

        int take=0;
        int price=items[n-1][1];
        if(price<=budget){
            take=1+cp[n-1]+findMax(n-1,budget-price,minPrice,items,cp);
        }
        int skip=findMax(n-1,budget,minPrice,items,cp);
        return dp[n-1][budget]=max(skip,take);
    }
    int maximumSaleItems(vector<vector<int>>& items, int budget) {
        int n=items.size();
        int minPrice=INT_MAX;
        memset(dp,-1,sizeof(dp));
        vector<int>cp(n,0);
        for(int i=0;i<n;i++){
            int c=0;
            minPrice=min(minPrice,items[i][1]);
            for(int j=0;j<n;j++){
                if(i==j) continue;
                if(items[j][0]%items[i][0]==0){
                    c++;
                }

            }
            cp[i]=c;
        }

        return findMax(n,budget,minPrice,items,cp);
    }
};