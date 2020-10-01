class Solution:
    def reverseBits(self, n: int) -> int:
        original = bin(n)[2:]
        if len(original) < 32:
            original = '0'*(32-len(original)) + original
        return int('0b' + original[::-1], 2)
        
        
