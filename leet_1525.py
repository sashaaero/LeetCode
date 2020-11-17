import collections
class Solution:
    def numSplits(self, s: str) -> int:
        lc, rc = collections.Counter(), collections.Counter(s)
        
        res = 0
        for c in s:
            lc[c] += 1
            rc[c] -=1 
            
            if rc[c]==0:
                del rc[c]
            
            if len(lc) == len(rc):
                res +=1
        return res
