class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        if len(intervals) == 1:
            return intervals
        
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(intervals[i][1],result[-1][1])
            else:
                result.append(intervals[i])

        return result