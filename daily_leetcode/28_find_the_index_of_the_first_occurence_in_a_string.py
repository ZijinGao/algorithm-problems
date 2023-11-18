# KMP algorithm (knuth-morris-pratt)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)
        if m > n:
            return -1

        # PREPROCESSING
        longest_border = [0 for _ in range(m)]
        i = 1
        slow = 0
        while i < m:
            if needle[i] == needle[slow]:
                longest_border[i] = slow + 1
                slow += 1
                i += 1
            elif needle[i] != needle[slow]:
                if slow != 0:
                    slow = longest_border[slow - 1]
                else:
                    longest_border[i] = 0
                    i += 1

        # SEARCHING
        i = 0
        j = 0
        while j < len(needle) and i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j > 0:
                    j -= 1
                    j = longest_border[j]
                else:
                    i += 1
        if j < len(needle):
            return -1
        return i - len(needle)