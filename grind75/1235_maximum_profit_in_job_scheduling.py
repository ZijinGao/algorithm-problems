## DP and binary search
## use of bisect.bisect_right

import bisect
class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        bundle = [(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))]
        bundle.sort(key = lambda x:x[1])
        dp = {}
        dp[0] = 0
        for endtime in endTime:
            dp[endtime] = 0
        
        curr_max = 0
        sorted_end_time = sorted(endTime)
        for start, end, profit in bundle:
            prev = 0
            if start >= sorted_end_time[0]:
                prev = sorted_end_time[ bisect.bisect_right(sorted_end_time, start)-1 ]
            curr_max = max(curr_max, dp[prev] + profit)
            dp[end] = curr_max
        return curr_max