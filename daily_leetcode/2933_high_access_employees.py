from collections import defaultdict
class Solution:
    def findHighAccessEmployees(self, access_times: list[list[str]]) -> list[str]:
        when = defaultdict(list)
        for a in access_times:
            who, time = a
            time = 60*int(time[:2])+int(time[2:])
            when[who].append(int(time))

        out = []
        for x, lst in when.items():
            lst.sort()
            high = False
            for i in range(len(lst) - 2):
                if lst[i + 2] < lst[i] + 60:
                    high = True
                    break
            if high:
                out.append(x)
        return out