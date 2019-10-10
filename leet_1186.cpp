class Solution {
public:
    int maximumSum(vector<int>& a) {
        const int n =a.size();
        int suf_del = 0;
        int suf_no_del = a[0];
        int ans=a[0];
        for(int i=1;i<n;i++){
            suf_del = max(suf_del + a[i], suf_no_del);
            suf_no_del = max(suf_no_del+a[i], a[i]);
            ans=max({ans,suf_del, suf_no_del});
        }
        return ans;
    }
};