# https://leetcode.com/problems/number-complement/

num = 1  # should return 2
i = 1
for _ in range(num.bit_length()):
    num ^= i
    i <<= 1

print(num)