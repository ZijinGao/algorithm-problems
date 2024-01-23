class Solution:
    def maxLength(self, arr: list[str]) -> int:
        dp = [set()]
        for string in arr:
            if len(string) != len(set(string)): continue
            string = set(string)
            for c in dp:
                if c & string: continue
                dp.append(string | c)
        return max(len(a) for a in dp)