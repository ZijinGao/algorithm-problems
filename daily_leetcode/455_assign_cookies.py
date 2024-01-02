class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        g_ptr = 0
        s_ptr = 0
        out = 0

        while g_ptr < len(g) and s_ptr < len(s):
            if g[g_ptr] <= s[s_ptr]:
                out += 1
                s_ptr += 1
                g_ptr += 1
            else:
                s_ptr += 1

        return out