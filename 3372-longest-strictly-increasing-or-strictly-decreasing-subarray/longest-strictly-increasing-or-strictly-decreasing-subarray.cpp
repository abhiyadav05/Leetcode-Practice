class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int n=nums.size();
        int count=0;
        int j=0;
        int maxI=0;
        int ans=1;
        for(int i=1;i<n;i++){
            if(nums[i]>nums[i-1]){
                maxI=i-j+1;
            }else{
               j=i;
            }
            ans=max(ans,maxI);
        }
        int maxD=0;
        int k=0;
         for(int i=1;i<n;i++){
            if(nums[i]<nums[i-1]){
                maxD=i-k+1;
            }else{
               k=i;
            }
            ans=max(ans,maxD);
        }

        return ans;
    }
};