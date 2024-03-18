class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort()
        count = 1
        curr_end = float('inf')
        for ballon in points:
            start = ballon[0]
            end = ballon[1]
            if start > curr_end:
                curr_end = end
                count += 1
            else:
                curr_end = min(end, curr_end)
        return count