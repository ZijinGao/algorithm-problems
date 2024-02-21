class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (n & 1) | (res << 1)
            n >>= 1
        return res
    
'''
Problem: Reverse bits of a given 32 bits unsigned integer.

Idea: use (n & 1) to get the last bit of the original number, left shift the result and add the (n & 1) to the result,
and then right shift n. Until we exhaust the 32 bits.
'''