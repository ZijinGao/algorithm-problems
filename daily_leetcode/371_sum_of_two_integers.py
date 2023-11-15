class Solution:
    def getSum(self, a: int, b: int) -> int:
        ## a, b can be negative
        x = abs(a)
        y = abs(b)

        if y > x:
            return self.getSum(b, a)
        
        sign = 1 if a > 0 else -1

        if a * b >= 0:
            while y:
                answer = x ^ y
                carry = (x & y) << 1
                x = answer
                y = carry
    
        else:
            while y:
                answer = x ^ y
                borrow = ((~x) & y) << 1
                x = answer
                y = borrow
        
        return x * sign