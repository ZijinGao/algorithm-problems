import bisect
class SummaryRanges:
    def __init__(self):
        self.vals = []
        
    def addNum(self, value: int) -> None:
        idx = bisect.bisect_left(self.vals, value)
        if idx >= len(self.vals):
            self.vals.append(value)
            return
        if self.vals[idx] != value: # no existing item of value in self.vals
            self.vals.insert(idx, value)

    def getIntervals(self) -> list[list[int]]:
        if not self.vals:
            return []
        if len(self.vals) == 1:
            return [[self.vals[0], self.vals[0]]]

        out = []
        prev = self.vals[0]
        for i in range(1, len(self.vals)):
            if self.vals[i-1] != self.vals[i] - 1:
                out.append([prev, self.vals[i-1]])
                prev = self.vals[i]
        out.append([prev, self.vals[-1]])
        return out