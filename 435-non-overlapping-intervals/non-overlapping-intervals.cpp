class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(),intervals.end());
        int ans=0;
        int n=intervals.size();
        int b=intervals[0][1];
        for(int i=1;i<n;i++){
            // cout << intervals[i][0] << " " << intervals[i][1] << endl;
            if(b>intervals[i][0]){
                // cout << "ye";
                ans+=1;
                b=min(b,intervals[i][1]);
            }else{
                b=intervals[i][1];
            }
        }
        return ans;
    }
};