# Runtime: 168 ms, faster than 96.08% of Python3 online submissions for Sum of Even Numbers After Queries.
# https://leetcode.com/problems/sum-of-even-numbers-after-queries/submissions/


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        prev_sum = sum(x for x in A if x % 2 == 0)
        for val, index in queries:
            cur_val = A[index]
            if cur_val % 2 == 0:
                prev_sum -= cur_val

            new_val = cur_val + val
            if new_val % 2 == 0:
                prev_sum += new_val

            A[index] = new_val
            result.append(prev_sum)

        return result