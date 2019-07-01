# https://leetcode.com/problems/longest-substring-without-repeating-characters
# Runtime: 92 ms, faster than 37.17% of Python3 online submissions for Longest Substring Without Repeating Characters.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_possible_len = len(set(s))
        if max_possible_len == len(s):
            return max_possible_len
        max_found_len = 0
        for i, c in enumerate(s):
            if max_found_len >= (len(s) - i):
                return max_found_len

            curr_sub = {c}
            curr_max_len = 1
            for j in range(i + 1, len(s)):
                c2 = s[j]
                if c2 not in curr_sub:
                    curr_sub.add(c2)
                    curr_max_len += 1
                else:
                    if curr_max_len > max_found_len:
                        max_found_len = curr_max_len
                        if max_found_len == max_possible_len:
                            return max_found_len
                    break
            else:
                if curr_max_len > max_found_len:
                    max_found_len = curr_max_len
                    if max_found_len == max_possible_len:
                        return max_found_len
        return max_found_len


if __name__ == '__main__':
    s = Solution()
    assert s.lengthOfLongestSubstring("abcabcbb") == 3
    assert s.lengthOfLongestSubstring("bbbbbbbb") == 1
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    assert s.lengthOfLongestSubstring(" ") == 1
    assert s.lengthOfLongestSubstring("aab") == 2
