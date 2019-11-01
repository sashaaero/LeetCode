# https://leetcode.com/problems/shortest-distance-to-a-character/

S = "loveleetcode"
C = 'e'
indexes = []
prev = None
size = len(S)

for i, char in enumerate(S):
    if char == C:
        indexes.append(i)

indexes.append(20000)
j = 0
next = indexes[j]
indexes_len = len(indexes)
results = []
for i, char in enumerate(S):
    if i > next:
        j += 1
        prev = next
        next = indexes[j]
    if prev is None:
        results.append(next - i)
    else:
        results.append(min(i - prev, next - i))
