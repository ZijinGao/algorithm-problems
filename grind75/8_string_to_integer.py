class Solution:
    def myAtoi(self, s: str) -> int:
        # ignore leading whitespace
        s = s.lstrip()
        if not s: return 0

        sign = -1 if s[0] == '-' else 1
        s = s[1:] if (s[0] == '-' or s[0] == '+') else s
        res = 0
        for i in range(len(s)):
            if s[i].isdigit():
                res = res * 10 + int(s[i])
            else:
                break
        res = res * sign
        if res < -2147483648:
            res = -2147483648
        elif res > 2147483647:
            res = 2147483647
        return res
