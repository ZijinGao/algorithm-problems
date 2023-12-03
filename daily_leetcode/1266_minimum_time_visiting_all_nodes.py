class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        distance = 0
        for i in range(len(points)-1): # look at curr and next point
            p1 = points[i]
            p2 = points[i+1]
            delta_x = abs(p1[0] - p2[0])
            delta_y = abs(p1[1] - p2[1])
            distance += max(delta_x, delta_y)

        return distance