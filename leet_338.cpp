class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> ans = {0, 1};
        int n=2;
        int tot = 2;
        int j=0;
        if(num==0){
            vector<int> ans = {0};
            return ans;
        }
        if(num==1){
            vector<int> ans = {0, 1};
            return ans;
        }
        
        while(tot != num+1){
            ans.push_back(ans[j]+1);
            j+=1;
            if(j==n){
                j=0;
                n*=2;
            }
            tot+=1;
        }
        return ans;
    }
};
