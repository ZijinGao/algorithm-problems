from collections import defaultdict
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = defaultdict(int)
        for c in s:
            count[c] += 1

        res = ''
        for c in order:
            if count.get(c, 0) >= 1:
                res += c * count[c]
        
        for c in s:
            if c not in order:
                res += c

        return res