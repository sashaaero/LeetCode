# https://leetcode.com/problems/expressive-words/


class Solution(object):
    def expressive_words(self, S, words):
        ans = 0
        keys, counts = self.get_count(S)
        for word in words:
            keys1, counts1 = self.get_count(word)
            if keys1 == keys:
                ans += all(c1 >= max(c2, 3) or c1 == c2
                           for c1, c2 in zip(counts, counts1))
        return ans

    @staticmethod
    def get_count(S):
        from itertools import groupby
        groups = groupby(S)
        keys = []
        counts = []
        for key, grp in groups:
            keys.append(key)
            counts.append(len(list(grp)))
        return keys, counts


s = Solution()
string = "aaa"
words = ["aaaa"]
res = s.expressive_words(string, words)
print(res)