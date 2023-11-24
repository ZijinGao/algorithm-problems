from collections import defaultdict
import bisect
class TimeMap:
    def __init__(self):
        self.timestamps = defaultdict(list) # {key1: [t1, t2, ... tn]}
        self.mapping = defaultdict(defaultdict) # {key1: {t1: v1, t2: v2, ... tn: vn}}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key][timestamp] = value
        self.timestamps[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        ts_idx = bisect.bisect_left(self.timestamps[key], timestamp)
        if len(self.timestamps[key]) == 0:
            return ''
        if ts_idx == 0 and self.timestamps[key][0] != timestamp:
            return ''
        if ts_idx == len(self.timestamps[key]):
            ts_idx -= 1
        elif self.timestamps[key][ts_idx] > timestamp:
            ts_idx -= 1
        ts = self.timestamps[key][ts_idx]
        return self.mapping[key][ts]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)