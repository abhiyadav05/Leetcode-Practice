class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        int n=arr.size();
        int ans=0;
        int evc=1;
        int odc=0;
        int M=1e9+7;
        // vector<int>pre(n+1,0);
        // for(int i=1;i<=n;i++){
        //     pre[i]=pre[i-1]+arr[i-1];
        // }

        // we dont need for prefix
        int sum=0;
        for(int i=0;i<n;i++){
            sum+=arr[i];
            if(sum%2==0){
                evc++;
            }else{
                odc++;
            }
            if(sum%2){
                ans+=evc;
                ans%=M;
            }else{
                ans+=odc;
                ans%=M;
            }
        }
         
            
        return ans%M;
    }
};