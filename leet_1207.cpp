class Solution {
public:
    bool uniqueOccurrences(vector<int>& v) {
        int a[1001],b[1001];
        set<int> S;
        int n=v.size();
        for(int i=0;i<=1000;i++){
            a[i]=0;
            b[i]=0;
        }
        for(int i=0;i<n;i++){
            if(v[i]>=0)a[v[i]]++;
            else b[-1*v[i]]++;
        }
        int count=0;
        for(int i=0;i<=1000;i++){
            if(a[i]!=0){
                count++;
                S.insert(a[i]);
            }
            if(b[i]!=0){
                count++;
                S.insert(b[i]);
            }
        }
        return S.size()==count;
        
    }
}; 