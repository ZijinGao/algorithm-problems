class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        if len(colors) == 1: return 0

        out = 0
        slow = 0
        fast = 0
        while fast < len(colors):
            while fast < len(colors) and colors[fast] == colors[slow]:
                fast += 1
            fast -= 1
            if fast == slow:
                fast += 1
                slow += 1
            else: # fast > slow
                temp_arr = neededTime[slow:fast+1]
                temp_min = max(temp_arr)
                temp_sum = sum(temp_arr) - temp_min
                out += temp_sum

                slow = fast + 1
                fast = slow
        return out