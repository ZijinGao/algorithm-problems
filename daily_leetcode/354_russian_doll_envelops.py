from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)
        res = []
        for i in range(n):
            h = envelopes[i][1]
            if i == 0:
                res.append(h)                
            else:
                if h > res[-1]:
                    res.append(h)
                else:
                    idx = bisect_left(res, h)
                    res[idx] = h
        return len(res)
    

# connection to #300 longest increasing subsequence