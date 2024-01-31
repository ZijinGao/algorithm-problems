from collections import deque
class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        if len(t) == 1:
            return [0]
        queue = deque()
        res = [0 for _ in t]
        for i in range(len(t)-1, -1, -1):
            if not queue:
                res[i] = 0
                queue.appendleft(i)
            else:
                while queue and t[i] >= t[queue[0]]:
                    queue.popleft()
                if not queue:
                    res[i] = 0
                else:
                    res[i] = queue[0] - i
                queue.appendleft(i)
        return res