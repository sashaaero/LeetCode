class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur = None    
        cnt=0
        for e in nums:
            if cnt == 0:
                cnt=1
                cur=e
            elif e == cur:
                cnt += 1
            else:
                cnt -= 1
        return cur
                
            
