class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        if n == 1:
            return 1

        i = 0
        res = 0
        while i < len(chars):
            curr_length = 1
            while i + curr_length < len(chars) and chars[i+curr_length] == chars[i]:
                curr_length += 1
            chars[res] = chars[i]
            res += 1
            if curr_length > 1:
                count = str(curr_length)
                
                chars[res:res+len(count)] = list(count)
                res += len(count)
            i += curr_length
        return res