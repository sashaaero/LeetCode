#https://leetcode.com/problems/is-subsequence/
# Runtime 24.23 ms


def isSubSequence(s, t, m, n):
    if m == 0:
        return True
    if n == 0:
        return False
    if s[m - 1] == t[n - 1]:
        return isSubSequence(s, t, m - 1, n - 1)

    return isSubSequence(s, t, m, n - 1)


s = input()
t = input()

if isSubSequence(s, t, len(s), len(t)):
    print('TRUE')
else:
    print('FALSE')
