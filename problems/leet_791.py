# https://leetcode.com/problems/custom-sort-string/
# Runtime: 36 ms, faster than 87.59% of Python3 online submissions for Custom Sort String.

from collections import defaultdict

S = "cba"
T = "abcd"

order = defaultdict(lambda: 100)
for i, char in enumerate(S):
    order[char] = i
result = ''.join(sorted(T, key=lambda x: order[x]))

print(result)