from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s): return []
        p_table = Counter(p)
        s_table = Counter(s[:len(p)])
        res = []
        i = 0
        j = len(p)

        while j <= len(s):
            if p_table == s_table:
                res.append(i)
            
            s_table[s[i]] -= 1
            if s_table[s[i]] < 0:
                del s_table[s[i]]
            
            if j < len(s):
                s_table[s[j]] += 1
            
            i += 1
            j += 1
        return res