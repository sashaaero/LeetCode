class Solution {
public:
    int longestSubsequence(vector<int>& arr, int difference) {
        unordered_map<int,int> mp;
        int res=0;
        for(int i=0;i<arr.size();i++){
            res=max(res, mp[arr[i]]=mp[arr[i]-difference]+1);
        }
        return res;
    }
};