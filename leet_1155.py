class Solution:
    def toHex(self, num: int) -> str:
        mp = {}
        for i in range(10):
            mp[i] = str(i)
        for i in range(10, 16):
            mp[i] = chr(ord('a')+i-10)
        
        if num==0:
            return str(0)
        
        ans = ""
        neg = 1 if num < 0 else 0
        
        rev = {v:int(k) for k,v in mp.items()}
        num = num*-1 if neg else num
        while num:
            dig = num%16
            ans += mp[dig]
            num//=16
        ans = ans[::-1]
        if neg:
            mx = "ffffffff"
            ans = ''.join(["0"]*(8-len(ans))) + ans
            new_ans = ""
            assert(len(ans) == len(mx))
            for i in range(8):
                new_ans += mp[rev[mx[i]] - rev[ans[i]]]
            i=7
            
            print(new_ans, i)
            f=0
            while(i>0 and new_ans[i] == "f"):
                new_ans = new_ans[:i] + "0" + new_ans[i+1:]
                i-=1
                f=1
            new_ans = new_ans[:i] + mp[rev[new_ans[i]] + 1] + new_ans[i+1:]            
            return new_ans
                
        else:
            return ans
            
