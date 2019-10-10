class Solution {
public:
    void dfs(int s,map<int,set<int>>&m,set<int> &visited,set<int>& store)
    {
        for(auto a:m[s])
        {
            if(visited.find(a)==visited.end())
            {
                visited.insert(a);
                store.insert(a);
                dfs(a,m,visited,store);
            }
        }
    }
    string smallestStringWithSwaps(string str, vector<vector<int>>& pairs) 
    {
        string ans=str;
        map<int,set<int>> m;
        for(auto a:pairs)
        {
            m[a[0]].insert(a[1]);
            m[a[1]].insert(a[0]);
        }
        vector<set<int>> comp;
        set<int> visited;
        for(int a=0;a<str.size();a++)
        {
            if(visited.find(a)==visited.end())
            {
                set<int>store;
                visited.insert(a);
                store.insert(a);
                dfs(a,m,visited,store);
                comp.push_back(store);
            }
        }
        for(auto a:comp)
        {
            vector<int> index;
            vector<char> chars;
            for(auto b:a)
            {
                chars.push_back(str[b]);
                index.push_back(b);
            }
            sort(chars.begin(),chars.end());
            for(int i=0;i<index.size();i++)
            {
                ans[index[i]]=chars[i];
            }
        }
        return ans;
    }
};