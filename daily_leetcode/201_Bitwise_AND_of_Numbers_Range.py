class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
    

'''
Problem: Given two integers left and right that represent the range [left, right], 
return the bitwise AND of all numbers in this range, inclusive.
e.g. 1: left = 5, right = 7, returns 4
e.g. 2: left = 6, right = 7, returns 6

5 in binary representation: 101
7 in binary representation: 111
right most same prefix:     ^
answer:                     100 -> 4


6 in binary representation: 110
7 in binary representation: 111
right most same prefix:      ^
answer:                     110 -> 6
'''