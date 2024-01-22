from collections import Counter, defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        p_table = Counter(p)
        s_table = defaultdict(int)
        res = []

        for i in range(len(s)):
            s_table[s[i]] += 1
            if i >= len(p):
                s_table[s[i-len(p)]] -= 1
                if s_table[s[i-len(p)]] == 0:
                    del s_table[s[i-len(p)]]
            if s_table == p_table:
                res.append(i-len(p) +1)

        return res