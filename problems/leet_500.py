#  https://leetcode.com/problems/keyboard-row/
# Runtime: 32 ms, faster than 99.84% of Python3 online submissions for Keyboard Row.

keyboard = [
    {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'},
    {'a','s','d','f','g','h','j','k','l'},
    {'z','x','c','v','b','n','m'}
]

words = ["Hello", "Alaska", "Dad", "Peace"]
result = []
for word in words:
    for row in keyboard:
        if word[0].lower() in row:
            curr_row = row

    for char in word:
        if char.lower() not in curr_row:
            break
    else:
        result.append(word)

print(result)