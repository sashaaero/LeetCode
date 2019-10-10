class Solution {
public:
    bool check(int m, int a[], int M, int n){
        for(int i=m;i<=n;i++){
            if(a[i]-a[i-m]<=M)
                return true;
        }
        return false;
    }
    int equalSubstring(string s, string t, int maxCost) {
        int n=s.length();
        int a[n+1];
        a[0]=0;
        for(int i=0;i<n;i++)
            a[i+1]=a[i]+abs(s[i]-t[i]);
        int l=0,r=n,ans=0;
        while(l<=r){
            int m = l+(r-l)/2;
            if(check(m,a,maxCost,n)){
                ans=m;
                l=m+1;
            }
            else 
                r=m-1;
        }
        return ans;
    }
};