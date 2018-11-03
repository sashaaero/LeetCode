# https://leetcode.com/problems/uncommon-words-from-two-sentences/
# Runtime: 36 ms, faster than 97.81% of Python3 online submissions for Uncommon Words from Two Sentences.

A = "s z z z s"
B = "s z ejt"


a_data = set()
b_data = set()

for word in A.split():
    if word not in a_data:
        a_data.add(word)
    else:
        b_data.add(word)

for word in B.split():
    if word not in b_data:
        b_data.add(word)
    else:
        a_data.add(word)


print(a_data.symmetric_difference(b_data))

