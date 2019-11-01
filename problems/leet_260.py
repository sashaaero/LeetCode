# https://leetcode.com/problems/single-number-iii/submissions/
# Runtime: 64 ms, faster than 96.20% of Python3 online submissions for Single Number III.

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = []
        num_dict = dict()
        for i in nums:
            if i not in num_dict:
                num_dict.update({i: 1})
            else:
                num_dict[i] += 1

        for k, v in num_dict.items():
            if v == 1:
                ans.append(k)

        return ans
